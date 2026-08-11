#!/usr/bin/env python3
"""Validate the exact public GitHub Pages artifact before deployment."""

from __future__ import annotations

import argparse
import ipaddress
import json
import math
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


EXPECTED_SCHEMA = "public-solar-feed-v1"
APPROVED_DOMAIN = "www.cognitiveworkstead.com"
MAX_FILE_BYTES = 8 * 1024 * 1024

PUBLIC_FILES = {
    "CNAME",
    "COL-B.png",
    "about.html",
    "ask-colb.html",
    "contact.html",
    "dashboard.png",
    "focus-areas.html",
    "index.html",
    "mckenzie-solar-change-log.md",
    "mckenzie-solar.html",
    "mckenzie-solar-status.png",
    "partnerships.html",
    "progress-log-01.html",
    "progress.html",
    "projects.html",
    "solarstatus.json",
    "updates.html",
    "assets/mckenzie-real.jpg",
    "assets/site.css",
    "assets/site.js",
}

TEXT_SUFFIXES = {".html", ".htm", ".js", ".css", ".json", ".md", ".txt", ""}
BLOCKED_NAME_PATTERNS = [
    re.compile(r"^COLBY_PROJECT_CURRENT_TRUTH\.md$", re.I),
    re.compile(r"^knowledge_transfer\.json$", re.I),
    re.compile(r"^solarstatus_private\.json$", re.I),
    re.compile(r".*\.bak(?:\..*)?$", re.I),
    re.compile(r".*\.pre-.*$", re.I),
    re.compile(r".*~$", re.I),
    re.compile(r".*\.sw[opx]$", re.I),
    re.compile(r".*\.tmp$", re.I),
    re.compile(r".*\.log$", re.I),
    re.compile(r".*\.(?:db|sqlite|sqlite3|bundle|tar|tgz|gz|zip|7z|xz)$", re.I),
    re.compile(r"(^|/)\.env(?:\.|$)", re.I),
]

PROHIBITED_PATTERNS = {
    "person-identifiers": [
        r"\bgreg(?:ory)?\b|greg[_-]",
        r"\bmel(?:issa)?\b|mel[_-]",
        r"\bperson\.[a-z0-9_-]+",
    ],
    "phone-or-device-presence": [
        r"\bphone\b",
        r"\bdevice_tracker\b",
        r"\bwi-?fi\b",
        r"\bnot_home\b",
        r"\bhome[_ -]?assistant\b",
        r"\bha[_ -]?presence\b",
        r"\bpresence\b|[_-]presence\b",
        r"\boccup(?:ancy|ied|y|ant)",
    ],
    "camera-or-skycam": [
        r"\bskycam\b|skycam[_-]",
        r"\bcamera\b|camera[_-]",
        r"\bsnapshot\b",
        r"\bstream\b",
        r"\bimage_path\b",
        r"\banalysis_image\b",
        r"\bmodel_host\b",
    ],
    "private-infrastructure": [
        r"/home/[A-Za-z0-9_.-]+",
        r"/opt/colby",
        r"\bsolar-collector\b",
        r"\bcolby-bridge\b",
        r"\b127\.0\.0\.1\b",
        r"\blocalhost\b",
        r"\b100\.114\.\d{1,3}\.\d{1,3}\b",
        r"\b192\.168\.\d{1,3}\.\d{1,3}\b",
        r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",
        r"\b172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}\b",
        r"\b[a-z0-9_-]+\.local\b",
    ],
    "credentials": [
        r"\btoken\b",
        r"\bsecret\b",
        r"\bpassword\b",
        r"\bcredential\b",
        r"\bauthorization\b",
        r"\bbearer\s+[A-Za-z0-9._-]+",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    ],
    "colb-current-truth": [
        r"\bCOLBY_PROJECT_CURRENT_TRUTH\b",
        r"\bknowledge_transfer\b",
        r"\bCurrent Truth\b",
        r"\bCOL-B operational\b",
        r"\bcolby\b",
    ],
    "private-survivability": [
        r"\bsurvivability\b",
        r"\bzero_solar_days\b",
        r"\bsimilar_weather_days\b",
        r"\brisk_analysis\b",
    ],
    "security-status": [
        r"\bsecurity[_ -]?system\b",
        r"\balarm[_ -]?state\b",
    ],
}

ALLOWED_TEXT_EXCEPTIONS = {
    ("index.html", "colb-current-truth", "colby"): "Public COL-B/Colby brand, public feature copy, and public contact address only.",
    ("ask-colb.html", "colb-current-truth", "colby"): "Public Ask COL-B/Colby brand and public feature copy only.",
    ("index.html", "private-infrastructure", "remote"): "Public-page phrase, not a hostname or endpoint.",
    ("contact.html", "colb-current-truth", "colby"): "Public contact address only; no Current Truth export or private COL-B details.",
    ("progress-log-01.html", "colb-current-truth", "colby"): "Public COL-B/Colby brand and public contact address only.",
    ("progress-log-01.html", "phone-or-device-presence", "presence"): "Public website-presence phrase, not household telemetry.",
    ("mckenzie-solar.html", "colb-current-truth", "colby"): "Public dashboard label/identifier only; no Current Truth export or private bridge path.",
    ("mckenzie-solar-change-log.md", "camera-or-skycam", "camera"): "Historical public change note, no source metadata or private path.",
}

TOP_LEVEL_SCHEMA = {
    "arrays",
    "feed_status",
    "forecast",
    "historical_model",
    "now",
    "performance",
    "privacy_boundary",
    "production_tracking",
    "public_notes",
    "public_reserve",
    "schema_version",
    "solar",
    "solar_intelligence",
    "status",
    "sunset_projection",
    "timestamp",
    "timestamp_central",
    "today",
    "weather",
}

SCHEMA_SHAPE: dict[str, Any] = {
    "arrays": {
        "array_1": "array_metrics",
        "array_2": "array_metrics",
        "total": "array_total",
        "insight": str,
    },
    "feed_status": str,
    "forecast": {"confidence": str, "expected_sunrise_soc": (int, float), "samples": int},
    "historical_model": {
        "available": bool,
        "avg_peak_pv_w": int,
        "best_solar_kwh": (int, float),
        "confidence": str,
        "expected_solar_kwh": (int, float),
        "historical_basis_days": int,
        "worst_solar_kwh": (int, float),
    },
    "now": {
        "battery_power_w": int,
        "battery_soc": int,
        "battery_temp_f": (int, float),
        "generator_w": int,
        "load_w": int,
        "mode": str,
        "solar_w": int,
    },
    "performance": {
        "actual_solar_w": int,
        "peak_trend": {
            "avg_peak_30d_w": int,
            "best_peak_30d_w": int,
            "days": int,
            "today_peak_w": int,
            "today_vs_avg_peak_pct": (int, float),
            "worst_peak_30d_w": int,
        },
        "similar_avg_solar_w": int,
    },
    "privacy_boundary": str,
    "production_tracking": {
        "available": bool,
        "confidence": str,
        "expected_so_far_kwh": (int, float),
        "expected_today_kwh": (int, float),
        "historical_basis_days": int,
        "produced_so_far_kwh": (int, float),
        "progress_of_expected_day_pct": (int, float),
        "tracking_vs_expected_so_far_pct": (int, float),
    },
    "public_notes": {"boundary": str, "cadence": str},
    "public_reserve": {"battery_soc": int, "confidence": str, "reserve_level": str, "summary": str},
    "schema_version": str,
    "solar": {"grading_enabled": bool, "operational_message": str, "peak_established": bool, "state": str},
    "solar_intelligence": {
        "actual_now_w": int,
        "available": bool,
        "basis_days": int,
        "confidence": str,
        "expected_now_w": (int, type(None)),
        "grade": str,
        "performance_pct": (int, float, type(None)),
        "variance_pct": (int, float, type(None)),
    },
    "status": str,
    "sunset_projection": {
        "available": bool,
        "basis_days": int,
        "confidence": str,
        "projected_sunset_soc": (int, float),
    },
    "timestamp": str,
    "timestamp_central": str,
    "today": {
        "avg_load_w": int,
        "consumed_kwh": (int, float),
        "generator_kwh": (int, float),
        "lowest_soc": int,
        "peak_generator_w": int,
        "peak_load_w": int,
        "peak_solar_w": int,
        "produced_kwh": (int, float),
    },
    "weather": {
        "class": str,
        "cloud_cover": int,
        "forecast_7day": {"days": "forecast_days"},
        "humidity": int,
        "temperature_f": (int, float),
    },
}

ARRAY_METRICS = {
    "azimuth_deg": (int, float),
    "bifacial": bool,
    "efficiency_pct": (int, float),
    "label": str,
    "mppt": str,
    "name": str,
    "panel_count": int,
    "panel_watts": int,
    "peak_today_efficiency_pct": (int, float),
    "peak_today_time_central": str,
    "peak_today_w": int,
    "power_w": int,
    "rated_w": int,
    "season_best_w": int,
    "tilt_deg": (int, float),
}

ARRAY_TOTAL = {
    "azimuth_deg": (int, float, type(None)),
    "bifacial": (bool, type(None)),
    "efficiency_pct": (int, float),
    "label": (str, type(None)),
    "mppt": (str, type(None)),
    "name": (str, type(None)),
    "panel_count": (int, type(None)),
    "panel_watts": (int, type(None)),
    "peak_today_efficiency_pct": (int, float),
    "peak_today_time_central": str,
    "peak_today_w": int,
    "power_w": int,
    "rated_w": int,
    "season_best_w": int,
    "tilt_deg": (int, float, type(None)),
}

FORECAST_DAY = {
    "cloud_cover": int,
    "confidence": str,
    "date": str,
    "day": str,
    "expected_peak_w": int,
    "expected_solar_kwh": (int, float),
    "expected_solar_kwh_high": (int, float),
    "expected_solar_kwh_low": (int, float),
    "high_f": int,
    "historical_days_used": int,
    "icon": str,
    "low_f": int,
    "precip_in": (int, float),
}


@dataclass
class Finding:
    severity: str
    category: str
    path: str
    detail: str


class Validator:
    def __init__(self, root: Path, source: Path | None = None) -> None:
        self.root = root.resolve()
        self.source = source.resolve() if source else None
        self.findings: list[Finding] = []

    def fail(self, category: str, path: str, detail: str) -> None:
        self.findings.append(Finding("FAIL", category, path, detail))

    def validate(self) -> list[Finding]:
        self.validate_inventory()
        self.validate_integrity()
        self.validate_solar_json()
        self.validate_text_artifacts()
        return self.findings

    def validate_inventory(self) -> None:
        seen: set[str] = set()
        for path in sorted(self.root.rglob("*")):
            rel = path.relative_to(self.root).as_posix()
            if path.is_symlink():
                self.fail("symlink", rel, "symlinks are not allowed in the public artifact")
                continue
            if path.is_dir():
                continue
            seen.add(rel)
            if rel not in PUBLIC_FILES:
                self.fail("unexpected-file", rel, "file is not in the approved public artifact inventory")
            if path.stat().st_size > MAX_FILE_BYTES:
                self.fail("file-size", rel, "file exceeds reviewed size threshold")
            for pattern in BLOCKED_NAME_PATTERNS:
                if pattern.match(Path(rel).name) or pattern.match(rel):
                    self.fail("blocked-file", rel, "filename matches a prohibited publication pattern")
        for rel in sorted(PUBLIC_FILES - seen):
            self.fail("missing-file", rel, "required public artifact is missing")

    def validate_integrity(self) -> None:
        cname = self.root / "CNAME"
        if cname.exists() and cname.read_text(encoding="utf-8").strip() != APPROVED_DOMAIN:
            self.fail("cname", "CNAME", "CNAME does not match the approved domain")
        for required in ("index.html", "progress-log-01.html", "mckenzie-solar.html", "solarstatus.json"):
            if not (self.root / required).is_file():
                self.fail("required-page", required, "required public page/feed is absent")
        for rel in ("index.html", "progress-log-01.html", "mckenzie-solar.html"):
            path = self.root / rel
            if path.exists():
                self.validate_links(rel, path.read_text(encoding="utf-8", errors="ignore"))

    def validate_links(self, rel: str, text: str) -> None:
        for target in re.findall(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", text, re.I):
            parsed = urlparse(target)
            if parsed.scheme in {"http", "https", "mailto", "tel"} or target.startswith("#"):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean or clean.startswith("data:"):
                continue
            if clean.startswith("/"):
                clean = clean.lstrip("/")
            if ".." in Path(clean).parts:
                self.fail("link", rel, f"local link escapes artifact: {target}")
                continue
            if not (self.root / clean).exists():
                self.fail("link", rel, f"local link target missing: {target}")

    def validate_solar_json(self) -> None:
        path = self.root / "solarstatus.json"
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            self.fail("json", "solarstatus.json", f"malformed JSON: {exc}")
            return
        if not isinstance(data, dict):
            self.fail("schema", "solarstatus.json", "root must be an object")
            return
        if set(data) != TOP_LEVEL_SCHEMA:
            extra = sorted(set(data) - TOP_LEVEL_SCHEMA)
            missing = sorted(TOP_LEVEL_SCHEMA - set(data))
            if extra:
                self.fail("schema", "solarstatus.json", "unexpected top-level keys: " + ", ".join(extra))
            if missing:
                self.fail("schema", "solarstatus.json", "missing top-level keys: " + ", ".join(missing))
        if data.get("schema_version") != EXPECTED_SCHEMA:
            self.fail("schema", "solarstatus.json", "schema version is not public-solar-feed-v1")
        self.check_shape("solarstatus.json", data, SCHEMA_SHAPE)
        self.check_ranges(data)
        self.scan_json(data)

    def check_shape(self, path: str, obj: Any, shape: Any) -> None:
        if shape == "array_metrics":
            return self.check_shape(path, obj, ARRAY_METRICS)
        if shape == "array_total":
            return self.check_shape(path, obj, ARRAY_TOTAL)
        if shape == "forecast_days":
            if not isinstance(obj, list) or len(obj) != 7:
                self.fail("schema", path, "forecast days must be a seven-item list")
                return
            for idx, item in enumerate(obj):
                self.check_shape(f"{path}[{idx}]", item, FORECAST_DAY)
            return
        if isinstance(shape, dict):
            if not isinstance(obj, dict):
                self.fail("schema", path, "expected object")
                return
            extra = sorted(set(obj) - set(shape))
            missing = sorted(set(shape) - set(obj))
            for key in extra:
                self.fail("schema", f"{path}.{key}", "unexpected key")
            for key in missing:
                self.fail("schema", f"{path}.{key}", "missing required key")
            for key, subshape in shape.items():
                if key in obj:
                    self.check_shape(f"{path}.{key}", obj[key], subshape)
            return
        if not isinstance(obj, shape):
            expected = getattr(shape, "__name__", str(shape))
            if isinstance(shape, tuple):
                expected = " or ".join(getattr(s, "__name__", str(s)) for s in shape)
            self.fail("schema", path, f"expected {expected}")

    def check_ranges(self, data: dict[str, Any]) -> None:
        checks = {
            "now.battery_soc": (0, 100),
            "today.lowest_soc": (0, 100),
            "public_reserve.battery_soc": (0, 100),
            "weather.cloud_cover": (0, 100),
            "weather.humidity": (0, 100),
            "sunset_projection.projected_sunset_soc": (0, 100),
            "forecast.expected_sunrise_soc": (0, 100),
        }
        solar_intelligence = data.get("solar_intelligence", {})
        solar_available = solar_intelligence.get("available") is True
        solar_numeric_fields = {
            "expected_now_w": (int,),
            "performance_pct": (int, float),
            "variance_pct": (int, float),
        }

        if solar_available:
            for key, expected_types in solar_numeric_fields.items():
                value = solar_intelligence.get(key)
                if (
                    isinstance(value, bool)
                    or not isinstance(value, expected_types)
                    or not math.isfinite(value)
                ):
                    self.fail(
                        "schema",
                        f"solar_intelligence.{key}",
                        "expected finite numeric value when available is true",
                    )

            expected_now = solar_intelligence.get("expected_now_w")
            if (
                isinstance(expected_now, (int, float))
                and not isinstance(expected_now, bool)
                and expected_now < 0
            ):
                self.fail(
                    "range",
                    "solar_intelligence.expected_now_w",
                    "expected nonnegative power when available is true",
                )
        else:
            for key in solar_numeric_fields:
                if solar_intelligence.get(key) is not None:
                    self.fail(
                        "schema",
                        f"solar_intelligence.{key}",
                        "must be null when available is false",
                    )

        progress = get_path(
            data,
            "production_tracking.progress_of_expected_day_pct",
        )
        if (
            isinstance(progress, bool)
            or not isinstance(progress, (int, float))
            or not math.isfinite(progress)
            or progress < 0
        ):
            self.fail(
                "range",
                "production_tracking.progress_of_expected_day_pct",
                "expected finite nonnegative production progress",
            )

        nonnegative = [
            "now.load_w",
            "now.solar_w",
            "now.generator_w",
            "arrays.array_1.power_w",
            "arrays.array_2.power_w",
            "arrays.total.power_w",
            "today.produced_kwh",
            "today.consumed_kwh",
        ]
        for path, (lo, hi) in checks.items():
            value = get_path(data, path)
            if not isinstance(value, (int, float)) or not lo <= value <= hi:
                self.fail("range", path, f"value outside reviewed range {lo}..{hi}")
        for path in nonnegative:
            value = get_path(data, path)
            if not isinstance(value, (int, float)) or value < 0:
                self.fail("range", path, "expected nonnegative numeric public metric")
        try:
            parsed = datetime.fromisoformat(str(data["timestamp"]).replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                self.fail("timestamp", "timestamp", "timestamp must include timezone")
            elif (
                str(data.get("feed_status", "")).lower() != "stale"
                and (datetime.now(timezone.utc) - parsed.astimezone(timezone.utc)).total_seconds() > 24 * 3600
            ):
                self.fail("timestamp", "timestamp", "timestamp is older than 24 hours")
        except Exception:
            self.fail("timestamp", "timestamp", "timestamp is malformed")
        if not re.match(r"^[A-Z][a-z]{2} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M Central Time$", str(data.get("timestamp_central", ""))):
            self.fail("timestamp", "timestamp_central", "Central timestamp has unexpected format")

    def scan_json(self, obj: Any, path: str = "solarstatus.json") -> None:
        if isinstance(obj, dict):
            for key, value in obj.items():
                current = f"{path}.{key}"
                self.scan_value(current, key, is_key=True)
                self.scan_json(value, current)
        elif isinstance(obj, list):
            for idx, value in enumerate(obj):
                self.scan_json(value, f"{path}[{idx}]")
        elif isinstance(obj, str):
            self.scan_value(path, obj, is_key=False)

    def validate_text_artifacts(self) -> None:
        for path in sorted(self.root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            rel = path.relative_to(self.root).as_posix()
            text = path.read_text(encoding="utf-8", errors="ignore")
            self.scan_value(rel, text, is_key=False, whole_file=True)
            if rel.endswith(".html"):
                if re.search(r"\bconsole\.(?:log|debug|dir|table)\b", text):
                    self.fail("debug-output", rel, "console debug output is not allowed in public HTML")
                for target in re.findall(r"fetch\(\s*[\"']([^\"']+)[\"']", text):
                    if not target.startswith("solarstatus.json"):
                        self.fail("fetch", rel, f"unexpected fetch destination: {target}")
                if rel == "mckenzie-solar.html":
                    required = ["public_reserve", "schema_version", "solarstatus.json"]
                    for token in required:
                        if token not in text:
                            self.fail("dashboard", rel, f"dashboard missing public schema reference: {token}")

    def scan_value(self, path: str, value: str, *, is_key: bool, whole_file: bool = False) -> None:
        text = str(value)
        for category, patterns in PROHIBITED_PATTERNS.items():
            for pattern in patterns:
                for match in re.finditer(pattern, text, re.I):
                    sample = match.group(0).lower()
                    rel = path[:-8] if path.endswith(":content") else path
                    if rel not in PUBLIC_FILES and "." in rel:
                        rel = rel.split(".", 1)[0]
                    if (rel, category, sample) in ALLOWED_TEXT_EXCEPTIONS:
                        continue
                    if category == "private-infrastructure" and looks_public_url(sample):
                        continue
                    location = path if not whole_file else f"{path}:content"
                    noun = "key" if is_key else "content"
                    self.fail(category, location, f"prohibited {noun} category matched")


def looks_public_url(value: str) -> bool:
    return value.startswith("https://www.cognitiveworkstead.com")


def get_path(data: dict[str, Any], path: str) -> Any:
    cur: Any = data
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def stage_artifact(source: Path, artifact: Path) -> None:
    if artifact.exists():
        shutil.rmtree(artifact)
    artifact.mkdir(parents=True)
    for rel in sorted(PUBLIC_FILES):
        src = source / rel
        dst = artifact / rel
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", nargs="?", default=".", help="artifact directory to validate")
    parser.add_argument("--source", default=".", help="source repository when staging an artifact")
    parser.add_argument("--stage", action="store_true", help="stage the explicit public artifact before validation")
    args = parser.parse_args()

    artifact = Path(args.artifact)
    if args.stage:
        stage_artifact(Path(args.source), artifact)

    validator = Validator(artifact)
    findings = validator.validate()
    print("=== PUBLIC ARTIFACT PRIVACY GATE ===")
    print("Artifact:", artifact)
    print("Allowed public files:", len(PUBLIC_FILES))
    if findings:
        print("Result: FAIL")
        for finding in findings[:80]:
            print(f"{finding.severity}: {finding.category}: {finding.path}: {finding.detail}")
        if len(findings) > 80:
            print(f"... {len(findings) - 80} additional findings suppressed")
        return 1
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
