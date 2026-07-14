#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from tools.validate_public_artifacts import PUBLIC_FILES, Validator


def valid_feed() -> dict:
    now = datetime.now(timezone.utc).replace(microsecond=0)
    array = {
        "azimuth_deg": 180,
        "bifacial": True,
        "efficiency_pct": 50.0,
        "label": "South array",
        "mppt": "A",
        "name": "Array A",
        "panel_count": 10,
        "panel_watts": 400,
        "peak_today_efficiency_pct": 70.0,
        "peak_today_time_central": "Jul 14, 2026, 12:00 PM Central Time",
        "peak_today_w": 3000,
        "power_w": 1200,
        "rated_w": 4000,
        "season_best_w": 3900,
        "tilt_deg": 25.0,
    }
    total = dict(array)
    total.update({"azimuth_deg": None, "bifacial": None, "label": None, "mppt": None, "name": None, "panel_count": None, "panel_watts": None, "tilt_deg": None})
    day = {
        "cloud_cover": 40,
        "confidence": "medium",
        "date": "2026-07-14",
        "day": "Tue",
        "expected_peak_w": 4000,
        "expected_solar_kwh": 18.0,
        "expected_solar_kwh_high": 22.0,
        "expected_solar_kwh_low": 14.0,
        "high_f": 90,
        "historical_days_used": 12,
        "icon": "partly-cloudy",
        "low_f": 70,
        "precip_in": 0.0,
    }
    return {
        "arrays": {"array_1": array, "array_2": array, "total": total, "insight": "Public array summary."},
        "feed_status": "ok",
        "forecast": {"confidence": "medium", "expected_sunrise_soc": 70.0, "samples": 12},
        "historical_model": {"available": True, "avg_peak_pv_w": 4200, "best_solar_kwh": 24.0, "confidence": "medium", "expected_solar_kwh": 18.0, "historical_basis_days": 12, "worst_solar_kwh": 8.0},
        "now": {"battery_power_w": 100, "battery_soc": 80, "battery_temp_f": 92.0, "generator_w": 0, "load_w": 900, "mode": "Solar/Battery", "solar_w": 1200},
        "performance": {"actual_solar_w": 1200, "peak_trend": {"avg_peak_30d_w": 4000, "best_peak_30d_w": 5000, "days": 30, "today_peak_w": 4200, "today_vs_avg_peak_pct": 105.0, "worst_peak_30d_w": 2000}, "similar_avg_solar_w": 1100},
        "privacy_boundary": "public allowlist",
        "production_tracking": {"available": True, "confidence": "medium", "expected_so_far_kwh": 10.0, "expected_today_kwh": 18.0, "historical_basis_days": 12, "produced_so_far_kwh": 11.0, "progress_of_expected_day_pct": 61.0, "tracking_vs_expected_so_far_pct": 110.0},
        "public_notes": {"boundary": "allowlist_only", "cadence": "Dashboard schedule."},
        "public_reserve": {"battery_soc": 80, "confidence": "medium", "reserve_level": "strong", "summary": "Public reserve summary."},
        "schema_version": "public-solar-feed-v1",
        "solar": {"grading_enabled": True, "operational_message": "Public solar status.", "peak_established": True, "state": "green"},
        "solar_intelligence": {"actual_now_w": 1200, "available": True, "basis_days": 12, "confidence": "medium", "expected_now_w": 1000, "grade": "A", "performance_pct": 120.0, "variance_pct": 20.0},
        "status": "GREEN",
        "sunset_projection": {"available": True, "basis_days": 12, "confidence": "medium", "projected_sunset_soc": 85.0},
        "timestamp": now.isoformat().replace("+00:00", "Z"),
        "timestamp_central": "Jul 14, 2026, 1:13 PM Central Time",
        "today": {"avg_load_w": 800, "consumed_kwh": 7.0, "generator_kwh": 0.0, "lowest_soc": 70, "peak_generator_w": 0, "peak_load_w": 1500, "peak_solar_w": 4200, "produced_kwh": 11.0},
        "weather": {"class": "partly cloudy", "cloud_cover": 40, "forecast_7day": {"days": [dict(day) for _ in range(7)]}, "humidity": 55, "temperature_f": 88.0},
    }


class PublicArtifactValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp(prefix="public-artifact-test-"))
        for rel in PUBLIC_FILES:
            path = self.tmp / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            if rel == "solarstatus.json":
                path.write_text(json.dumps(valid_feed()), encoding="utf-8")
            elif rel == "CNAME":
                path.write_text("www.cognitiveworkstead.com\n", encoding="utf-8")
            elif rel.endswith(".html"):
                body = "public_reserve schema_version solarstatus.json" if rel == "mckenzie-solar.html" else ""
                path.write_text(f"<html><body><a href='solarstatus.json'>feed</a>{body}</body></html>", encoding="utf-8")
            elif rel.endswith(".md"):
                path.write_text("Public change log.\n", encoding="utf-8")
            else:
                path.write_bytes(b"fake-public-asset")

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def assert_fails(self, mutator, category: str) -> None:
        mutator()
        findings = Validator(self.tmp).validate()
        categories = {f.category for f in findings}
        self.assertIn(category, categories, [f"{f.category}:{f.path}" for f in findings])

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual([], Validator(self.tmp).validate())

    def test_current_truth_filename_fails(self) -> None:
        self.assert_fails(lambda: (self.tmp / "COLBY_PROJECT_CURRENT_TRUTH.md").write_text("synthetic", encoding="utf-8"), "unexpected-file")

    def test_knowledge_transfer_filename_fails(self) -> None:
        self.assert_fails(lambda: (self.tmp / "knowledge_transfer.json").write_text("{}", encoding="utf-8"), "unexpected-file")

    def test_backup_filename_fails(self) -> None:
        self.assert_fails(lambda: (self.tmp / "index.html.bak").write_text("backup", encoding="utf-8"), "unexpected-file")

    def test_occupancy_key_fails(self) -> None:
        self.mutate_feed(lambda d: d["now"].update({"occupancy": "synthetic"}))
        self.assertIn("phone-or-device-presence", {f.category for f in Validator(self.tmp).validate()})

    def test_person_presence_key_fails(self) -> None:
        self.mutate_feed(lambda d: d.update({"person.alex_example": "synthetic"}))
        categories = {f.category for f in Validator(self.tmp).validate()}
        self.assertTrue({"person-identifiers", "phone-or-device-presence"} & categories)

    def test_camera_metadata_fails(self) -> None:
        self.mutate_feed(lambda d: d["weather"].update({"skycam_source": "synthetic"}))
        self.assertIn("camera-or-skycam", {f.category for f in Validator(self.tmp).validate()})

    def test_private_path_fails(self) -> None:
        self.mutate_feed(lambda d: d["public_notes"].update({"boundary": "/home/example/private"}))
        self.assertIn("private-infrastructure", {f.category for f in Validator(self.tmp).validate()})

    def test_internal_ip_fails(self) -> None:
        self.mutate_feed(lambda d: d["public_notes"].update({"boundary": "192.168.1.5"}))
        self.assertIn("private-infrastructure", {f.category for f in Validator(self.tmp).validate()})

    def test_unexpected_json_key_fails(self) -> None:
        self.assert_fails(lambda: self.mutate_feed(lambda d: d.update({"unexpected_public_extension": True})), "schema")

    def test_invalid_schema_version_fails(self) -> None:
        self.assert_fails(lambda: self.mutate_feed(lambda d: d.update({"schema_version": "bad"})), "schema")

    def test_malformed_timestamp_fails(self) -> None:
        self.assert_fails(lambda: self.mutate_feed(lambda d: d.update({"timestamp": "not-a-date"})), "timestamp")

    def test_invalid_numeric_range_fails(self) -> None:
        self.assert_fails(lambda: self.mutate_feed(lambda d: d["now"].update({"battery_soc": 150})), "range")

    def test_missing_required_public_metric_fails(self) -> None:
        self.assert_fails(lambda: self.mutate_feed(lambda d: d["now"].pop("solar_w")), "schema")

    def test_nested_private_object_fails(self) -> None:
        self.mutate_feed(lambda d: d["solar"].update({"private": {"occupancy": "synthetic"}}))
        categories = {f.category for f in Validator(self.tmp).validate()}
        self.assertIn("schema", categories)
        self.assertIn("phone-or-device-presence", categories)

    def mutate_feed(self, mutator) -> None:
        path = self.tmp / "solarstatus.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        mutator(data)
        path.write_text(json.dumps(data), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
