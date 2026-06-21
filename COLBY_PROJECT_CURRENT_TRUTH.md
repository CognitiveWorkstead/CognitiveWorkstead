# COLBY PROJECT CURRENT TRUTH

Generated Local Time: 2026-06-21T16:42:22-05:00

Source System: AsusAI /opt/colby

Status: PASS

Authority Rule:
AsusAI /opt/colby generated reports and memory files are source material. External ChatGPT/COL-B consumes this as read-only context.

Operating Boundaries:
- This export is read-only for external consumers.
- Do not write back to AsusAI Colby unless Greg explicitly approves it.
- Do not treat hypotheses as facts.
- Do not treat observations as verified state.
- Do not invent solar values, device states, or live system status.
- For McKenzie Solar, verified API or bridge data outranks assumptions.

Export Validation:
- Required missing files: 0
- Source file count: 32

## Current Truth Publishing Architecture

### Pipeline

- AsusAI /opt/colby is the source material for COL-B Current Truth.
- AsusAI runs /opt/colby/services/sync/auto_sync_orchestrator.py to regenerate derived Colby reports.
- AsusAI runs /opt/colby/services/export/current_truth_export.py to generate COLBY_PROJECT_CURRENT_TRUTH.md and knowledge_transfer.json.
- AsusAI runs /opt/colby/services/export/publish_current_truth.sh to publish Current Truth.
- publish_current_truth.sh transfers exports to Pi4 using passwordless SSH.
- Pi4 stores the public website repo at /home/cothrang/CognitiveWorkstead.
- Pi4 commits and pushes Current Truth files to GitHub.
- GitHub Pages serves the files at cognitiveworkstead.com.

### Automation

- Systemd Service: colby-current-truth.service
- Systemd Timer: colby-current-truth.timer
- Frequency: Hourly

### Commit-Spam Prevention

- Mechanism: Semantic hash
- Semantic Hash File: /opt/colby/export/current_truth.semantic.sha
- Last Published Hash File: /opt/colby/export/last_published.semantic.sha
- Behavior: If the semantic hash is unchanged, publish_current_truth.sh skips Pi4 copy, Git commit, and GitHub push.

### System Roles

- AsusAI: Source of truth and Current Truth generator.
- Pi4: Publisher node for GitHub Pages.
- GitHub Pages: Public read-only delivery layer.
- COL-B Executive Node: Cloud reasoning layer that consumes Current Truth as read-only context.

### Public Current Truth URLs

- https://www.cognitiveworkstead.com/COLBY_PROJECT_CURRENT_TRUTH.md
- https://www.cognitiveworkstead.com/knowledge_transfer.json

## Source Manifest

### Colby System Architecture
- Path: /opt/colby/docs/COLBY_SYSTEM_ARCHITECTURE.md
- Required: True
- Exists: True
- Size Bytes: 12991
- Modified Time: 2026-06-10T09:41:47-05:00
- SHA256: 8686f6c510a3708c5a5e2e82a6c1225bd662eb540a06b260ff7e22e30fb1e02d

### Colby Code Capability Registry
- Path: /opt/colby/docs/COLBY_CODE_CAPABILITY_REGISTRY.md
- Required: True
- Exists: True
- Size Bytes: 3774
- Modified Time: 2026-06-09T14:35:21-05:00
- SHA256: 23fbc1edfcededf068783547a91cae31f7210adf6be89844e0c24be3d1c13238

### Code Capability Registry Active
- Path: /opt/colby/memory/operational/code_capability_registry_active.md
- Required: True
- Exists: True
- Size Bytes: 19846
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: e3b4efeec555849e6c0cbcc222af5617c5ff795b9e5521d927ccf99726faa5ec

### Infrastructure Inventory
- Path: /opt/colby/memory/core/infrastructure_inventory.md
- Required: False
- Exists: True
- Size Bytes: 4684
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: 23c8ce5887484e1722c1a6dd80edb09c4a85ada3743fa7f617dfb542e2631692

### Current State
- Path: /opt/colby/state/current_state.md
- Required: True
- Exists: True
- Size Bytes: 1811
- Modified Time: 2026-05-31T08:15:21-05:00
- SHA256: 61203da21658af4c8985e178e3e9bf9f1968cfa27ae664dfa6de90046573b538

### Current Priorities
- Path: /opt/colby/memory/core/current_priorities.md
- Required: True
- Exists: True
- Size Bytes: 391
- Modified Time: 2026-06-21T06:22:34-05:00
- SHA256: 71124a6ebc0bc3344f50ded113cce49675849f32604cee0921d28526bcd27066

### Goals
- Path: /opt/colby/memory/core/goals.md
- Required: True
- Exists: True
- Size Bytes: 389
- Modified Time: 2026-05-29T08:01:23-05:00
- SHA256: 2c31d511d0645130688e64d449efa72d8ff625165f9b373a46d722ac896ca7e6

### Current Capabilities Memory
- Path: /opt/colby/memory/core/current_capabilities.md
- Required: True
- Exists: True
- Size Bytes: 19679
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: c0112a3885d4ba387326d7c6a3c1a8d5489cd40cb1ad9a1f761ec4e75a5f84bb

### Current Project Status
- Path: /opt/colby/reports/projects/current_project_status.md
- Required: True
- Exists: True
- Size Bytes: 3152
- Modified Time: 2026-06-21T16:42:21-05:00
- SHA256: e87e2351caff39d585197932f8f2cb57f9600af4f6e164835387196130682c23

### Current Milestone Status
- Path: /opt/colby/reports/projects/current_milestone_status.md
- Required: True
- Exists: True
- Size Bytes: 2863
- Modified Time: 2026-06-21T16:42:21-05:00
- SHA256: 264d4dd87513edf7768a33815974165eefff6e5b1a2c88900732bb2240c4f30b

### Current Dependency Status
- Path: /opt/colby/reports/projects/current_dependency_status.md
- Required: True
- Exists: True
- Size Bytes: 2434
- Modified Time: 2026-06-21T16:42:21-05:00
- SHA256: 36a99605670dadd7177b7c7141394f232756614cdbfa1b23ee85fe4af755df88

### Current Critical Path
- Path: /opt/colby/reports/projects/current_critical_path.md
- Required: True
- Exists: True
- Size Bytes: 1893
- Modified Time: 2026-06-21T16:42:21-05:00
- SHA256: 47a218fb9910381ac32424085580992f769e88a405669809fb711410898e4fed

### Current Capability Status
- Path: /opt/colby/reports/capabilities/current_capability_status.md
- Required: True
- Exists: True
- Size Bytes: 5914
- Modified Time: 2026-06-21T16:42:21-05:00
- SHA256: 8fea1541869fa178b1688c0a77a6b0b0887048d77b4e09544ce12bc0f5ea24f5

### McKenzie Solar Data Bridge
- Path: /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- Required: True
- Exists: True
- Size Bytes: 10967
- Modified Time: 2026-06-21T05:50:11-05:00
- SHA256: ef44e460590f8ca79e1414277067aa843a0de39bbff1b28d7fb48f59d31992fe

### Home Assistant Read-Only Access
- Path: /opt/colby/memory/operational/home_assistant_readonly_colby_access.md
- Required: True
- Exists: True
- Size Bytes: 2394
- Modified Time: 2026-06-09T14:17:21-05:00
- SHA256: 5cdf15eb0b2bac8af81a4957577835f91d601d0fa268ba2cc29f4f76d6cd92fe

### Constraints
- Path: /opt/colby/memory/core/constraints.md
- Required: True
- Exists: True
- Size Bytes: 834
- Modified Time: 2026-05-30T08:01:16-05:00
- SHA256: 139b6d1eb790a694673792c180dcc6e6ca4c57dc01a05adf9774fc5e4288cd03

### Limitations
- Path: /opt/colby/memory/core/limitations.md
- Required: True
- Exists: True
- Size Bytes: 1220
- Modified Time: 2026-06-01T20:19:11-05:00
- SHA256: e52fea43fc7148cc8bdf472782d92d128e43603b238885d756efc86cd26941ce

### COS Status
- Path: /opt/colby/reports/cos/COS_STATUS.md
- Required: True
- Exists: True
- Size Bytes: 4965
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: 8fe4db714948396451e560f6254348cb25cbc9625dd4d29e77c7a2980b3fe243

### Governed Action Audit Log
- Path: /opt/colby/reports/cos/GOVERNED_ACTION_AUDIT_LOG.md
- Required: True
- Exists: True
- Size Bytes: 21616
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: fc91f72d0df03b2a91f964be37cbf594d16a70ff30538c75bb9defff1ead87d8

### Governed Action Dashboard
- Path: /opt/colby/reports/cos/GOVERNED_ACTION_DASHBOARD.md
- Required: True
- Exists: True
- Size Bytes: 8445
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: ee9fe74de53207b56d33ceb7cb75a73f0f0297202c428d4ecd81de5e44addadf

### Housekeeping Agenda
- Path: /opt/colby/reports/cos/HOUSEKEEPING_AGENDA.md
- Required: True
- Exists: True
- Size Bytes: 2078
- Modified Time: 2026-06-21T16:42:20-05:00
- SHA256: 3bde9ffa700e18cd2361d849c00e21907c4bdbc716382f2c444692b111f0bad0

### Approval Required Capability Review
- Path: /opt/colby/reports/cos/approval_required_capability_review.md
- Required: True
- Exists: True
- Size Bytes: 21505
- Modified Time: 2026-06-21T06:01:57-05:00
- SHA256: b56160f70f92187c297528c37991b577c182b40f30886f78355dde21df9831fc

### OpenWebUI Persona Integration Plan
- Path: /opt/colby/reports/cos/OPENWEBUI_PERSONA_INTEGRATION_PLAN.md
- Required: True
- Exists: True
- Size Bytes: 5099
- Modified Time: 2026-06-21T07:05:14-05:00
- SHA256: f20804b9480e5c372645f02b1a1a8742208833c87cb62509d56a57eaf45fdcc9

### OpenWebUI Persona Routing Contract
- Path: /opt/colby/reports/cos/OPENWEBUI_PERSONA_ROUTING_CONTRACT.md
- Required: True
- Exists: True
- Size Bytes: 473
- Modified Time: 2026-06-21T07:05:14-05:00
- SHA256: b82d0edab497e837054cb8969e17f326f5db1a469414accfcee48c3708ad384e

### Current Persona Status
- Path: /opt/colby/reports/personas/current_persona_status.md
- Required: True
- Exists: True
- Size Bytes: 860
- Modified Time: 2026-06-21T16:03:02-05:00
- SHA256: 444dbe344efd2f61e12fd3e3a0601c03fd30d0a526ba284df80809e402ab53ad

### Persona Route Audit
- Path: /opt/colby/reports/personas/persona_route_audit.md
- Required: True
- Exists: True
- Size Bytes: 2557
- Modified Time: 2026-06-21T07:09:55-05:00
- SHA256: 082522cce5930092f2d3e8cadfd2d7d57623f3ba99e0f953cefdfce1a7dac86e

### Persona Memory Isolation Contract
- Path: /opt/colby/reports/personas/persona_memory_isolation_contract.md
- Required: True
- Exists: True
- Size Bytes: 4224
- Modified Time: 2026-06-21T07:13:02-05:00
- SHA256: 4ec00c24234067295e80c2f3f68d5c9bad29b7cc561a5602bce23c3227a11717

### Proxy Persona Route Validation
- Path: /opt/colby/reports/personas/proxy_persona_route_validation.md
- Required: True
- Exists: True
- Size Bytes: 1858
- Modified Time: 2026-06-21T15:16:04-05:00
- SHA256: 9ca0e35c2cc7cbce765632247624ab65b10047bcd9317bfa3723268d571b3687

### Fleet Discovery Snapshot
- Path: /opt/colby/reports/discovery/current_infrastructure_discovery.md
- Required: False
- Exists: True
- Size Bytes: 17483
- Modified Time: 2026-06-05T14:00:34-05:00
- SHA256: d95c0bb3f443cb4555937e562008afd1be6bec9e8b7e6149245bb7e61b687c20

### Executive Daily Review
- Path: /opt/colby/reports/executive/current_day_summary.md
- Required: False
- Exists: True
- Size Bytes: 4652
- Modified Time: 2026-06-21T16:42:22-05:00
- SHA256: cc8a58f01aba75542299672c4fd931ed6667ea06e1247d7322dd50dbf0d30a72

### Recent Investigations
- Path: /opt/colby/reports/investigations
- Required: False
- Exists: True
- Size Bytes: 4096
- Modified Time: 2026-06-16T16:23:20-05:00
- SHA256: a5ae4a62f10d8fe43e0552c296315e047c1ecc55183b5971db0ba787190cecec

### Latest Sync Report
- Path: /opt/colby/reports/sync/latest_sync.md
- Required: False
- Exists: True
- Size Bytes: 2294
- Modified Time: 2026-06-21T16:42:22-05:00
- SHA256: 0c7e3adb07e0279f1800059b8b915773f84d0df0002d3ccbff7bb2cbce312f82

## Colby System Architecture

Source: `/opt/colby/docs/COLBY_SYSTEM_ARCHITECTURE.md`

# COLBY SYSTEM ARCHITECTURE

Status: draft doctrine
Authority: architecture guidance
Created: 2026-06-09
Host: ASUSAI
Scope: Local Colby, Open WebUI Colby, Current Truth export, ChatGPT/COL-B continuity

## Purpose

This document defines how Colby is structured, how evidence flows through the system, and where reasoning should occur.

Colby must not evolve by accidental script accumulation. Each component should have a known layer, authority level, input, output, risk class, and owner boundary.

## Core Principle

Evidence collection, memory, retrieval, reasoning, and action are separate layers.

A script that collects data should not decide what the answer means.

A proxy route should not become the long-term reasoning engine.

A truth transfer file should not be treated as the only local memory authority.

## Architectural Layers

### Layer 1: Evidence Collection

Purpose:
- Read real systems.
- Collect facts.
- Avoid interpretation.

Examples:
- Home Assistant read-only puller.
- Solar data pullers.
- Discovery scripts.
- API health checks.

Rules:
- Prefer read-only.
- Store raw or lightly normalized facts.
- Do not write durable memory directly.
- Do not call control endpoints unless explicitly authorized.

### Layer 2: State Normalization

Purpose:
- Convert raw evidence into structured operational state.

Examples:
- /home/cothrang/colby-ha/ha_state_snapshot.json
- solar status JSON files
- generated daily reports
- normalized discovery reports

Rules:
- Preserve timestamps.
- Preserve source references.
- Label Central Time when used.
- Separate McKenzie and RiVi.
- Do not infer system health without evidence.

### Layer 3: Memory and Knowledge

Purpose:
- Store durable facts, decisions, constraints, goals, capabilities, and lessons.

Examples:
- /opt/colby/memory
- /opt/colby/state
- /opt/colby/reports
- approved decisions
- current priorities
- capability records

Rules:
- Stale records must be superseded, not silently erased.
- Failed experiments must not become durable truth.
- Observations become candidates before durable memory.
- Current user instruction outranks memory.

### Layer 4: Retrieval and Context Assembly

Purpose:
- Select relevant, authority-ranked information for the current question.

Examples:
- /opt/colby/services/context/relationship_context_loader.py
- workspace memory search
- workspace summaries
- future RAG/context assembler

Rules:
- Retrieve facts, not conclusions.
- Enforce authority order.
- Prefer current operational state over stale planning notes.
- Include source and timestamp when freshness matters.
- Avoid brittle keyword routing when a retrieval strategy is possible.

### Layer 5: Reasoning

Purpose:
- Let the model answer from supplied evidence.

Examples:
- Open WebUI Colby through colby_proxy.py
- ChatGPT/COL-B using Current Truth and project context
- local Ollama model behind Colby proxy

Rules:
- The model should reason from context.
- The answer should separate fact, inference, assumption, and recommendation.
- The model should not invent live system status.
- The model should not treat stale context as current when newer evidence exists.

### Layer 6: Action

Purpose:
- Change systems, files, services, devices, automations, or external repositories.

Examples:
- systemctl restart
- docker changes
- Home Assistant service calls
- GitHub publish
- memory promotion
- file edits

Rules:
- Explicit approval required.
- Back up before changes.
- Validate after changes.
- Log what changed.
- Prefer scripts/automations with audit trails over uncontrolled model action.
- Home Assistant remains the sensor/control plane.
- Colby remains the reasoning/reporting layer unless Greg explicitly authorizes control.

## Authority Order

1. Current user instruction.
2. Current live operational evidence.
3. Current Truth sources.
4. Approved local memory and decisions.
5. Generated reports.
6. Historical investigations.
7. Hypotheses and observations.
8. Old chat history.

When sources conflict, identify the conflict and prefer the higher authority source.

## Current Truth Role

Current Truth files are transfer artifacts for continuity across ChatGPT/COL-B sessions.

They are not the sole source of local Colby memory.

Current Truth should summarize the best known state from local Colby, but local Colby must still enforce authority order internally.

Files:
- /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md
- /opt/colby/export/knowledge_transfer.json
- /opt/colby/export/current_truth.semantic.sha

Public continuity endpoints:
- https://www.cognitiveworkstead.com/COLBY_PROJECT_CURRENT_TRUTH.md
- https://www.cognitiveworkstead.com/knowledge_transfer.json

## Home Assistant Boundary

Home Assistant is active as the operational sensor/control plane.

Colby has read-only HA snapshot access through ASUSAI.

Approved read-only files:
- /home/cothrang/colby-ha/ha_state_pull.py
- /home/cothrang/colby-ha/ha_state_snapshot.json
- /home/cothrang/.config/colby-ha/ha.env

Security:
- The HA token must never be placed in prompts, Current Truth, GitHub, model memory, logs, or chat transcripts.
- Colby may summarize facts from the snapshot.
- Colby must not call HA services unless explicitly approved by Greg.
- HA control must be approval-gated and auditable.

## McKenzie / RiVi Separation

McKenzie fixed-site operations and RiVi RV Victron operations are separate operational domains.

McKenzie:
- Fixed site.
- EG4 / SolarAssistant / Home Assistant bridge.
- Farm/property operations.

RiVi:
- RV Victron system.
- Cerbo GX / MultiPlus / SmartShunt / solar chargers.
- Dashboard should remain executive/watts-focused unless building a technical dashboard.

Colby must not blend McKenzie conclusions into RiVi or RiVi conclusions into McKenzie without evidence.

## Known Architectural Concern

The current system contains some hardcoded keyword routes.

Hardcoded routes are acceptable only for:
- safety gating
- authorization
- deterministic tool dispatch
- explicit user-requested commands

Hardcoded routes are not acceptable as the primary reasoning layer.

Future design should move toward:
- evidence retrieval
- authority-ranked context assembly
- model reasoning from supplied facts
- auditable action approval

## Architecture Inventory Source

Latest generated inventory:
- /opt/colby/reports/architecture/latest_colby_architecture_inventory.md

This inventory is a discovery report, not doctrine. This document is the doctrine.

## 2026-06-10 Open WebUI v0.9.6 runtime update

Status:
Operational and validated on ASUSAI.

Runtime facts:
- Open WebUI container: `open-webui`
- Image: `ghcr.io/open-webui/open-webui:v0.9.6`
- Port mapping: `3002 -> 8080`
- Data volume: `open-webui:/app/backend/data`
- Host gateway mapping: `host.docker.internal:host-gateway`
- Local OpenAPI tool servers reachable from Open WebUI container:
  - `host.docker.internal:5055`
  - `host.docker.internal:7077`

Validation:
- Docker health: healthy
- HTTP root: 200
- API version: 0.9.6
- No recent Open WebUI error patterns after host-gateway fix
- Colby proxy smoke test passed
- Combined McKenzie/RiVi source selection verified after upgrade

Operational lesson:
Open WebUI upgrades should use explicit known-good Docker settings instead of dynamic container reconstruction.

Known-good requirements:
- Preserve `open-webui:/app/backend/data`
- Preserve environment file
- Preserve `-p 3002:8080`
- Preserve `--add-host=host.docker.internal:host-gateway`
- Preserve `--restart always`

Change record:
`4e6df9607453`

## 2026-06-10 Open WebUI upgrade lessons learned

Context:
Open WebUI was upgraded on ASUSAI from `ghcr.io/open-webui/open-webui:v0.9.5` to `ghcr.io/open-webui/open-webui:v0.9.6`.

Final validated runtime:
- Container: `open-webui`
- Image: `ghcr.io/open-webui/open-webui:v0.9.6`
- Port mapping: `3002 -> 8080`
- Data volume: `open-webui:/app/backend/data`
- Host gateway: `host.docker.internal:host-gateway`
- Docker health: healthy
- Tool servers reachable from container:
  - `host.docker.internal:5055`
  - `host.docker.internal:7077`

Failure modes observed:
1. Dynamic Docker container reconstruction failed to preserve required runtime settings.
   - Lost `-p 3002:8080`
   - Lost `open-webui:/app/backend/data`
   - Lost `--restart always`
   - Lost `host.docker.internal:host-gateway`
2. Missing host gateway caused Open WebUI tool-server DNS errors:
   - `host.docker.internal:5055`
   - `host.docker.internal:7077`
3. After successful upgrade, browser-side stale session/auth state caused old chats to appear unavailable.
   - Open WebUI returned `401` for valid chat IDs.
   - Database still contained the chats.
   - Greg's user still owned the chats.
   - No database restore was needed.

Correct upgrade doctrine:
- Do not dynamically reconstruct Open WebUI containers.
- Use explicit known-good Docker run settings.
- Always preserve:
  - `--restart always`
  - `--add-host=host.docker.internal:host-gateway`
  - `-p 3002:8080`
  - `-v open-webui:/app/backend/data`
  - existing environment file
- Always back up the Docker volume before upgrade.
- Keep the prior container renamed and stopped for rollback.
- Validate before declaring success:
  - Docker health is healthy.
  - HTTP root returns 200.
  - `/api/version` returns expected version.
  - `host.docker.internal` resolves inside container.
  - Tool servers return OpenAPI from inside container.
  - Colby proxy smoke test passes.
  - Existing chat history opens in browser.

History/auth troubleshooting doctrine:
- If chat history appears missing after upgrade, do not restore the database first.
- Check browser/session state first.
- Inspect Open WebUI logs for `401` versus `404`.
- `401` against valid chat IDs usually indicates stale auth/session, not lost history.
- Verify database ownership before any restore:
  - `user`
  - `auth`
  - `chat`
  - `chat_message`
- If database contains the chats and user ownership is correct, clear browser site data for `ai.gregcothran.com` and log back in.
- Database restore is a last resort only when live DB rows are actually missing or corrupt.

Validated resolution:
- Cleared site data / reset browser session for `ai.gregcothran.com`.
- Logged back in as Greg.
- Chat history access was restored.
- No DB restore was performed.

Rollback references retained temporarily:
- `open-webui-pre-explicit-v096-20260610_083526`
- `open-webui-pre-hostgateway-v096-20260610_083845`
- `open-webui-pre-hostgateway-fix-20260602_142638`

Related change records:
- `4e6df9607453`

## 2026-06-10 RiVi battery power direction validation

RiVi / RV Victron battery power sign convention was validated using Home Assistant read-only sensor data and Victron VRM visual confirmation.

Validated rule:
- Positive `sensor.battery_monitor_power` watts means RiVi battery is charging.
- Negative `sensor.battery_monitor_power` watts means RiVi battery is discharging.
- Near zero, within approximately +/-25 W, means idle or balanced.

Evidence:
- During solar surplus, HA showed positive battery watts while SOC increased.
- During controlled A/C load, HA showed negative battery watts.
- Victron VRM simultaneously showed `Discharging` while battery power was negative.

Code update:
- `/opt/colby/tools/energy_systems_evidence.py`
- `rivi_rv.best_current_snapshot` now includes:
  - `battery_power_direction`
  - `battery_power_sign_convention`
  - `battery_power_sign_rule`
  - `battery_power_direction_confidence`
  - `battery_power_interpretation`

Governance:
- This is read-only evidence interpretation.
- No Home Assistant write access was added.
- No Victron control was added.
- McKenzie fixed-site solar and RiVi RV Victron remain separate systems.

## 2026-06-10 RiVi routing fix

Issue:
Open WebUI question `What is RiVi doing right now?` initially routed to the McKenzie-only solar evidence path because the phrase `right now` matched the McKenzie current-solar route. The combined McKenzie/RiVi route required both a RiVi/RV/Victron term and an energy metric term, so plain RiVi status questions were missed.

Fix:
- Updated `/opt/colby/services/proxy/colby_proxy.py`.
- Added `doing`, `right now`, `now`, and `state` to combined-energy metric trigger terms.
- Blocked the McKenzie-only current-solar route when the user question contains `rivi`, `rv`, or `victron`.
- Updated the combined-energy synthesis prompt to use validated RiVi battery direction fields:
  - `battery_power_direction`
  - `battery_power_interpretation`
  - `battery_power_sign_rule`

Validated behavior:
- Open WebUI now routes `What is RiVi doing right now?` through the combined energy evidence path.
- Colby correctly answered that RiVi was discharging.
- Evidence source was `home_assistant_readonly_snapshot_rivi_allowlist`.
- Freshness state was current.
- McKenzie and RiVi remain separate systems.

Governance:
- Routing change only.
- Read-only evidence access only.
- No Home Assistant write/service-call access was added.
- No Victron control was added.

## Colby Code Capability Registry

Source: `/opt/colby/docs/COLBY_CODE_CAPABILITY_REGISTRY.md`

# COLBY CODE CAPABILITY REGISTRY

Status: draft doctrine
Authority: architecture guidance
Created: 2026-06-09
Scope: Code monitoring, capability tracking, and memory candidate generation

## Purpose

The Code Capability Registry tracks what Colby code can do, what changed, and whether that change should become memory.

Code changes must create reviewable memory candidates.

Code changes must not automatically update durable memory.

## Core Principle

Implementation is not truth until reviewed.

A code file can exist.
A script can run.
A capability can work.
But Colby should not treat it as durable truth until the change is reviewed, classified, and approved.

## Change Flow

Code file changes
→ inventory scanner
→ hash/change registry
→ capability impact report
→ memory candidate
→ Greg review
→ approved memory update
→ Current Truth export
→ ChatGPT/COL-B continuity

## What the Registry Tracks

For every script, service, tool, and important file:

- path
- component name
- architecture layer
- purpose
- inputs
- outputs
- files read
- files written
- databases touched
- network calls
- external services touched
- secrets touched
- called by
- calls out to
- risk class
- last hash
- last modified time
- capability exposed
- operational status
- known stale notes
- rollback path

## Risk Classes

### READ_ONLY

Reads files, APIs, or system status.
Does not modify state.

Examples:
- HA state puller when using GET-only calls.
- discovery scripts.
- inventory scanners.

### WRITES_LOCAL

Writes local reports, generated files, local memory candidates, or local state.
Does not control systems.

Examples:
- Current Truth exporter.
- architecture inventory generator.
- memory candidate writer.

### WRITES_SYSTEM

Changes services, containers, packages, permissions, system files, prompts, or code.

Examples:
- patching colby_proxy.py.
- systemd unit edits.
- Docker compose changes.
- service restarts.

### EXTERNAL_CONTROL

Controls external systems or publishes externally.

Examples:
- GitHub publish.
- Home Assistant service calls.
- inverter control.
- climate control.
- relay control.
- external API actions.

## Memory Candidate Rules

The registry may create candidates for:
- new capability added
- capability removed
- capability changed
- stale memory detected
- code contradicts memory
- new risk introduced
- new external control surface added
- authority order conflict detected

The registry must not:
- auto-promote memory
- delete stale memory
- overwrite decisions
- publish Current Truth
- restart services
- call Home Assistant services

## Candidate Format

Each candidate should include:

- candidate ID
- generated time
- changed files
- old hash
- new hash
- detected capability change
- evidence
- affected architecture layer
- risk class
- recommended memory update
- recommended Current Truth update
- approval status
- rollback reference

## Approval States

- proposed
- reviewed
- approved
- rejected
- superseded

Only approved candidates should update durable memory.

## Desired Future Scripts

Suggested future paths:

- /opt/colby/services/architecture/code_inventory_scanner.py
- /opt/colby/services/architecture/code_change_detector.py
- /opt/colby/services/architecture/capability_registry_builder.py
- /opt/colby/services/architecture/memory_candidate_generator.py

Suggested outputs:

- /opt/colby/state/code_registry/code_inventory.json
- /opt/colby/state/code_registry/code_hashes.json
- /opt/colby/reports/architecture/code_capability_report.md
- /opt/colby/learning/review_required/code_change_*.md

## Operating Rule

Every code change should answer:

What changed?
What capability changed?
What risk changed?
What memory might now be stale?
What memory candidate should be reviewed?

## Code Capability Registry Active

Source: `/opt/colby/memory/operational/code_capability_registry_active.md`

# Code Capability Registry Active

Status: active
Approved: 2026-06-09
Approved by: Greg
Source Candidate: /opt/colby/learning/review_required/code_change_20260609T1444010500.md

## Confirmed Capability

The Code Capability Registry scanner is active on ASUSAI.

Scanner:
- /opt/colby/services/architecture/code_capability_scanner.py

State outputs:
- /opt/colby/state/code_registry/code_inventory.json
- /opt/colby/state/code_registry/code_hashes.json

Report output:
- /opt/colby/reports/architecture/code_capability_report.md

Candidate output:
- /opt/colby/learning/review_required/code_change_*.md

## Operating Boundary

The scanner inventories Colby code, prompts, docs, config, selected tools, and selected Home Assistant read-only support files.

The scanner may write local registry files, local reports, and proposed review candidates.

The scanner must not:
- promote durable memory automatically
- publish Current Truth
- restart services
- call Home Assistant services
- control external systems
- delete stale memory
- overwrite decisions

## Approval Rule

Code changes may create proposed memory candidates.

Only Greg-approved candidates may become durable memory.

## Current Baseline

Baseline created:
- 2026-06-09 14:42 Central Time

Scanner v0.2 confirmed:
- 2026-06-09 14:44 Central Time

The v0.2 scan detected one code change to the scanner itself and created a review candidate, proving the loop works:

code change -> registry detects change -> candidate created -> no auto-promotion

## Architectural Role

Layer:
- Layer 2/3: Architecture Registry

Purpose:
- Monitor code and capability-supporting files.
- Detect capability drift.
- Create review candidates when implementation changes may affect memory, Current Truth, risk, or architecture.

This subsystem is part of Colby governance, not the reasoning layer.

## OpenAI API / COLBY CLI Integration

Status: Operational  
Date Confirmed: 2026-06-16  
Host: ASUSAI  

ASUSAI has working OpenAI API access through a dedicated Python virtual environment at:

`/opt/colby/openai/venv`

The GPT-5 Responses API connectivity was verified with:

`/opt/colby/openai/test_gpt.py`

A global command-line wrapper is operational at:

`/usr/local/bin/colby`

Purpose:
- Provide targeted OpenAI API access from ASUSAI.
- Support future COLBY automation, agent workflows, executive review, and command-line reasoning.
- Keep ChatGPT Business as the primary human executive interface.
- Use OpenAI API selectively for high-value automation, not bulk chat replacement.
- Control API costs with low monthly limits and usage monitoring.

Architecture note:
- ChatGPT Business, OpenAI API, and ASUSAI local models are separate layers.
- ChatGPT Business remains the main interactive interface.
- OpenAI API is the automation and agent layer.
- ASUSAI local models remain the preferred bulk-processing layer.


## OpenAI API / COLBY CLI Integration

Status: Operational  
Date Confirmed: 2026-06-16  
Host: ASUSAI  

ASUSAI has working OpenAI API access through a dedicated Python virtual environment at:

`/opt/colby/openai/venv`

The GPT-5 Responses API connectivity was verified with:

`/opt/colby/openai/test_gpt.py`

A global command-line wrapper is operational at:

`/usr/local/bin/colby`

Purpose:
- Provide targeted OpenAI API access from ASUSAI.
- Support future COLBY automation, agent workflows, executive review, and command-line reasoning.
- Keep ChatGPT Business as the primary human executive interface.
- Use OpenAI API selectively for high-value automation, not bulk chat replacement.
- Control API costs with low monthly limits and usage monitoring.

Architecture note:
- ChatGPT Business, OpenAI API, and ASUSAI local models are separate layers.
- ChatGPT Business remains the main interactive interface.
- OpenAI API is the automation and agent layer.
- ASUSAI local models remain the preferred bulk-processing layer.


## 2026-06-21 COS Control Plane Registry v2

Status: Approved by Greg for promotion.

Colby now has a reviewable COS control-plane registry prototype promoted into the local Colby tree.

Artifacts:
- /opt/colby/state/cos/cos_capability_registry_v2.json
- /opt/colby/reports/cos/COS_CAPABILITY_REGISTRY_V2.md
- /opt/colby/state/cos/cos_status.json
- /opt/colby/reports/cos/COS_STATUS.md

Confirmed prototype results:
- 150 capability/source entries.
- 23 approval-required entries.
- 84 unclassified or unknown entries requiring future triage.
- Current Truth local export PASS at time of review.
- Persona boundary report passed workspace and public-user checks.
- Route trace prototype does not expose private content and does not call live tools.

Operating rule:
Capability-impacting changes must update durable Colby memory and be reflected in Current Truth before the work is considered complete.


## 2026-06-21 COS Capability Classification Complete

Status: Approved staged classification installed.

The COS Capability Registry v2 was triaged from 84 unclassified/unknown entries to 0.

Final counts:
- Entries: 150
- READ_ONLY: 68
- WRITES_LOCAL: 55
- WRITES_SYSTEM: 10
- EXTERNAL_CONTROL: 17
- Approval required: 27
- Unclassified or unknown: 0

Report:
- /opt/colby/reports/cos/cos_capability_classification_report.md

Registry:
- /opt/colby/state/cos/cos_capability_registry_v2.json

## 2026-06-21 Approval Surface Review

- Approval-required capability review installed for 27 entries.
- Risk counts: {'EXTERNAL_CONTROL': 17, 'WRITES_SYSTEM': 10}.
- Contract counts: {'block_execution': 6, 'future_approval_required': 4, 'governed_action_required': 8, 'read_only_preflight': 9}.
- Active read-only checks may be used only for evidence collection. Memory promotion, Current Truth publishing, prompt edits, proxy-mediated external actions, and system-changing paths require explicit Greg approval plus backup and validation.
- Report: /opt/colby/reports/cos/approval_required_capability_review.md

## 2026-06-21 Governed Action Preflight

- Installed read-only governed action preflight at /opt/colby/services/cos/action_preflight.py.
- The preflight classifies proposed actions as read_only, local_write, system_write, external_control, memory_promotion, publish, blocked_historical, or future_approval_required before execution.
- It emits a decision, approval requirement, required contract, mapped risk class, matched capability, evidence, and draft governed-action contract.
- Memory promotion, Current Truth publish, prompt edits, proxy external actions, and system-control paths require explicit Greg approval plus backup and validation.

## 2026-06-21 Governed Action Preflight Enforcement

- Governed action preflight enforcement installed into proxy, memory promotion, memory update apply, and Current Truth publish paths.
- Unapproved memory promotion, memory update apply, and Current Truth publish now block before mutation or external publication.
- Approval token for an explicitly approved governed run: COLBY_GOVERNED_ACTION_APPROVED=Greg.
- The proxy file was updated on disk; restarting the proxy remains a separate governed system action.
- Report: /opt/colby/reports/cos/GOVERNED_ACTION_PREFLIGHT_ENFORCEMENT.md

## 2026-06-21 Governed Proxy Restart

- colby-proxy.service was restarted and is active after governed preflight enforcement install.
- Repaired classifier validation so natural-language service restart requests classify as system_write / WRITES_SYSTEM, while read-only status checks remain READ_ONLY.
- Running proxy validation passed: /v1/models returned Colby models and a system-admin prompt was blocked by proxy preflight with no action executed.
- Current Truth timer points at the guarded publish script; unattended publishes require explicit COLBY_GOVERNED_ACTION_APPROVED=Greg and otherwise block before publishing.
- Report: /opt/colby/reports/cos/GOVERNED_PROXY_RESTART.md

## 2026-06-21 Fresh Context Correction

- Corrected context freshness behavior: current operational reports are now loaded ahead of older/default memory for natural-language status, accomplishment, priority, and planning questions.
- Removed old Right Turn business context from active current priorities. It remains historical memory only and should not be volunteered as current work unless Greg explicitly asks about historical context.
- Executive daily review now samples recent COS, project, capability, and executive reports first, excluding historical Right Turn noise from current summaries.
- This is a source/context fix, not a phrase-triggered answer route.

## 2026-06-21 Governed Action Audit Log

- Installed governed action audit log at /opt/colby/state/cos/governed_action_audit_log.jsonl.
- Installed recorder/report generator at /opt/colby/services/cos/governed_action_audit_recorder.py.
- Seeded 7 validated governed events from today's COS control-plane work.
- Future governed installers should append one event covering decision, action class, risk class, approval, validation, backups, touched paths, memory update status, publish status, and Current Truth semantic hash.
- Report: /opt/colby/reports/cos/GOVERNED_ACTION_AUDIT_LOG.md

## 2026-06-21 Governed Audit Wiring

- Wired governed action audit recorder into proxy denied-action path, memory promotion block, memory update apply block, and Current Truth publish block.
- Installed /opt/colby/services/cos/record_governed_action.sh helper for future governed installers.
- Audit ledger now contains 12 events including validated denied-path events.
- Denied action recording is fail-open for recording only: safety blocks still execute even if audit recording has a problem.

## 2026-06-21 Governed Action Dashboard
- Installed governed action dashboard generator and reports.
- Dashboard combines governed action audit events, COS status, and approval-required capability review.
- Current operational context now includes /opt/colby/reports/cos/GOVERNED_ACTION_DASHBOARD.md so natural-language answers about blocked, denied, approved, or approval-needed work use fresh governed sources before older memories.
- Publication remains separate and approval-gated.

## 2026-06-21 Housekeeping Agenda
- Installed Housekeeping Brief agenda generator.
- Colby now has a source-backed housekeeping queue from governed action dashboard, COS status, critical path, current priorities, and Greg corrections.
- Conversation policy: at natural pauses, Colby may offer housekeeping; if Greg says yes, she walks items highest priority first with context, recommendation, and options.
- This is not phrase-triggered routing; it is current-context driven and deferrable.

## 2026-06-21 Current Truth COS Governance Sections
- Current Truth exporter now includes COS Status, Governed Action Audit Log, Governed Action Dashboard, Housekeeping Agenda, and Approval Required Capability Review as required source sections.
- This makes external COL-B / ChatGPT Current Truth aware of governance, approval queue, and housekeeping state.
- This repair followed a successful publish where the public files updated, but validation showed the new COS reports were not yet included by the exporter.

## 2026-06-21 Housekeeping Publish Priority Repair
- Housekeeping agenda now treats any approved, validated publish-class action as satisfying the prior blocked Current Truth publish item.
- This prevents a stale denied publish test from remaining top priority after Greg approved and validated a successful Current Truth publish.

## 2026-06-21 Memory Promoter Two-Step Governance
- memory_promoter.py now defaults to proposal-only mode and writes no memory files.
- Durable hypothesis creation requires --apply plus COLBY_GOVERNED_ACTION_APPROVED=Greg.
- This converts the prior blunt block into a safer two-step model: read-only proposal generation first, governed memory promotion second.

## 2026-06-21 Memory Promotion Proposal Review
- Reviewed the first memory_promoter.py proposal-only batch.
- Proposal mode scanned records safely, but no candidates were approved for hypothesis creation.
- Rationale: candidates were already represented by stronger Current Truth/memory sources or were too generic.
- Memory promoter remains useful in proposal mode; apply mode remains approval-gated.

## 2026-06-21 Proxy Denied Test Closeout
- Closed the prior proxy denied restart event as a completed governance validation test.
- Outcome: proxy correctly blocked an unapproved system-write request; no restart was approved or needed.
- Housekeeping now suppresses closed validation denials so they do not appear as live approval requests.

## 2026-06-21 Memory Promoter Denied Closeout
- Closed old memory-promoter denied events as completed validation/review outcomes.
- The original block is superseded by two-step governance.
- Apply mode remains gated; the reviewed proposal batch approved zero hypothesis writes.

## 2026-06-21 Memory Update Denied Closeout
- Closed the old memory update apply denied event as completed validation evidence.
- The denied event was an intentional audit-wiring test against a temporary file.
- Real memory update apply remains governed and requires Greg approval.

## 2026-06-21 Proxy Approval Policy Decision
- colby_proxy.py is classified as governed-active, not broadly approved.
- Normal chat routing, read-only context assembly, model listing, and answer generation remain allowed.
- Service control, Docker/systemd actions, publishing, memory writes, filesystem writes, and external-control actions require governed approval and audit evidence.
- This clears the proxy capability from live housekeeping while preserving safety boundaries.

## 2026-06-21 OpenWebUI Persona Integration Plan
- OpenWebUI Persona Integration now has a controlled implementation plan.
- The plan preserves existing personas: colby-greg, colby-mel, colby-dj, and colby-public.
- Next phase is read-only persona route audit before any OpenWebUI, Docker, service, or proxy changes.
- Risky actions remain governed and approval-gated.

## 2026-06-21 Persona Route Audit
- Phase 1 OpenWebUI Persona Integration read-only route audit passed.
- Validated model-to-user routing, workspace route matrix, public-safe boundary checks, and active persona registry presence.
- Private memory content was not printed.
- Next phase is persona memory isolation contract.

## 2026-06-21 Persona Memory Isolation Contract
- Phase 2 OpenWebUI Persona Integration memory isolation contract passed.
- Validated allowed and denied memory prefixes for Greg, Mel, DJ, and Public.
- Public cannot access private user/workspace memory. Mel and DJ cannot access Greg-private memory unless shared. Greg owner access remains relationship-scoped unless explicitly listed.
- Private memory content was not printed.
- Next phase is proxy route validation.

## 2026-06-21 Current Truth Publish Denied Closeout
- Closed stale Current Truth publish denied events as superseded by later Greg-approved governed publishes.
- Current Truth publish remains approval-gated.
- Housekeeping suppresses old denied publish artifacts so they do not reappear as live work.

## 2026-06-21 Phase 3 Proxy Service Ready
- colby-proxy.service was validated for OpenWebUI Persona Integration Phase 3.
- Service action: already_active.
- /v1/models returned colby, colby-greg, colby-mel, colby-dj, and colby-public.
- Phase 3 proxy route validation may proceed.

## 2026-06-21 Proxy Persona Route Validation
- Phase 3 OpenWebUI Persona Integration proxy route validation passed.
- Validated /v1/models, persona status routes, and public private-workspace denial.
- Validation reports include route result shapes only; full private response content was not printed.
- Next phase is OpenWebUI configuration review.

## Phase 3 Current Truth publish retry completed
- Recorded: 2026-06-21T15:20:57-05:00
- Phase 3 proxy persona route validation passed locally and Current Truth publish retry completed.

## Phase 3 Current Truth closeout publish
- Recorded: 2026-06-21T15:22:11-05:00
- Purpose: publish the retry-success memory/audit delta created after commit `8e09299`.
- Phase 3 proxy persona route validation remains PASS.

## Colby Codex Bridge
- Recorded: 2026-06-21T15:47:05-05:00
- Codex CLI path: `/home/cothrang/.local/bin/codex`.
- Codex version: `codex-cli 0.141.0`.
- Bridge: `/opt/colby/services/codex/colby_codex_bridge.py`.
- Colby may prepare Codex job proposals.
- Codex execution requires explicit Greg approval.
- Write-capable Codex jobs require `COLBY_GOVERNED_ACTION_APPROVED=Greg` and `--allow-write`.
- Codex is a supervised engineering tool for Colby; it is not a replacement for Colby's private ASUSAI runtime, memory, services, or governance.

## OpenWebUI Persona Integration Phase 4
- Recorded: 2026-06-21T15:54:06-05:00
- Status: `pass_no_upstream_change_required`.
- Report: `/opt/colby/reports/openwebui_persona_config_review.md`.
- Read-only OpenWebUI configuration review completed without Docker restart, service change, proxy change, or private content exposure.

## OpenWebUI Persona Production Readiness
- Recorded: 2026-06-21T15:57:07-05:00
- Status: `production_ready_read_only`.
- Phase 1-4 validations passed.
- Phase 5 upstream implementation is not required by the current review.
- Report: `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.md`.

## OpenWebUI Persona Project Closeout
- Recorded: 2026-06-21T16:03:02-05:00
- Status: Operational.
- Completion: 100%.
- Phase 5 implementation is future-only if new requirements create a governed change need.

## Current Truth Health Generated Service
- Recorded: 2026-06-21T16:07:15-05:00
- Status: `PASS`.
- Service: `/opt/colby/services/cos/current_truth_health.py`.
- Report: `/opt/colby/reports/cos/current_truth_health.md`.
- Current Truth health is now generated by a repeatable local service/report instead of a one-off prototype.

## Operational Rule: Tailscale-First Infrastructure Access
- Updated: 2026-06-21T16:13:03-05:00
- For mobile operations, Colby should prefer Tailscale IPs/aliases for ASUSAI, PI4, PI500, GCSnapDragon, and Home Assistant when available.
- Do not make home-LAN-only routes the primary path for Current Truth publishing, cross-device SSH, or travel-sensitive automation.

## Operational Security: server.key Handling
- Updated: 2026-06-21T16:20:44-05:00
- Security-sensitive file triage must avoid printing contents.
- `/home/cothrang/server.key` is owner-restricted and documented in `/opt/colby/reports/security/server_key_triage.json`.
- Do not delete, rotate, or publish file contents without Greg approval and consumer mapping.

## Route Context Trace Debug Integration
- Updated: 2026-06-21T16:23:02-05:00
- `/opt/colby/services/context/relationship_context_loader.py --debug-trace <user> [workspace] [question]` emits safe JSON route trace metadata.
- Normal context loader behavior remains unchanged unless the debug flag is provided.
- Report: `/opt/colby/reports/cos/route_context_trace_report.md`.

## Single-Command Remote Execution Pattern
- Updated: 2026-06-21T16:27:37-05:00
- Continue using staged scripts in `/home/cothrang` with one command from Greg for governed operations.
- For remote hosts, prefer SSH over Tailscale aliases and explicit keys.
- For Home Assistant, prefer authenticated API/read-only diagnostics for inventory and status; write/control operations require governed approval.

## Right Turn Final Archive Rule
- Updated: 2026-06-21T16:37:25-05:00
- Treat OpenWebUI DB/vector backup matches for Right Turn as archived historical evidence, not active context.
- Report: `/opt/colby/reports/cos/RIGHT_TURN_HISTORICAL_ONLY_SCAN.md`.

## Remote Control Validation Pattern
- Updated: 2026-06-21T16:42:20-05:00
- Use read-only probes before remote operations.
- Use single-command SSH/API paths where inventory status is ready or partial.
- Do not use Telnet unless Greg approves a specific legacy exception.

## Infrastructure Inventory

Source: `/opt/colby/memory/core/infrastructure_inventory.md`

# Infrastructure Inventory

Purpose:
Authoritative durable inventory for stable infrastructure facts. This file is the source of truth for hostnames, LAN IPs, roles, and key system locations.

Governance:
- Stable infrastructure facts belong here.
- Live telemetry does not belong here.
- Greg corrections to hostnames, IPs, roles, or device identity should update this file.
- Current Truth should export this file.

## ASUSAI

Role:
Primary AI Server / Colby source system

Hostname:
ASUSAI

LAN IP:
192.168.86.185

Known Functions:
- Hosts /opt/colby
- Runs Colby OpenAI-compatible proxy on port 5056
- Runs Ollama / local AI stack
- Generates Current Truth exports
- Source of truth for COL-B project memory and reports

## PI4

Role:
McKenzie Solar Bridge / Publisher Node

Hostname:
pi4

LAN IP:
192.168.86.79

Known Functions:
- McKenzie Solar collector host
- Solar Assistant MQTT integration host path
- SQLite solar.db analytics host
- GitHub Pages publishing node for CognitiveWorkstead public files

## GCSnapDragon

Role:
Windows Control Node / PowerShell Operator Workstation

Hostname:
GCSnapDragon

LAN IP:
192.168.86.110

Known Functions:
- Runs PowerShell control commands
- Collects remote audit files
- Used by Greg for upload workflows into ChatGPT

## Home Assistant / SolarAssistant MQTT Bridge - Confirmed

- HAOS runs on Raspberry Pi 5 at 192.168.86.222.
- Public endpoint: https://ha.gregcothran.com.
- Tailscale remote access confirmed.
- SolarAssistant is at 192.168.86.69:1883.
- Home Assistant MQTT integration stays on core-mosquitto:1883.
- SolarAssistant is bridged into HA Mosquitto using /share/mosquitto/solar_assistant.conf.
- MQTT discovery is enabled and working.
- McKenzie Solar MQTT entities/devices were created successfully.
- Do not connect HA MQTT integration directly to SolarAssistant.

## PI500 access parity partial
- Recorded: 2026-06-21T15:32:49-05:00
- ASUSAI can SSH to PI500 over Tailscale at `100.108.205.70`.
- PI500 public key has been authorized on PI4.
- PI500 cannot yet reach PI4 over tested LAN paths while traveling/off-LAN.
- Likely next fix: approve Tailscale subnet routing to the home LAN or install Tailscale directly on PI4.

## PI500 Tailscale subnet route acceptance
- Recorded: 2026-06-21T15:34:27-05:00
- PI500 accepts Tailscale subnet routes while traveling/off-LAN.
- PI500-to-PI4 access status: `blocked`.
- Remaining fix: approve Home Assistant subnet routes or install Tailscale directly on PI4.

## PI4 direct Tailscale access
- Recorded: 2026-06-21T15:37:55-05:00
- PI4 Tailscale IP: `100.114.132.97`.
- ASUSAI has `pi4-ts` / `collector-ts` SSH aliases for direct Tailscale access.
- PI500-to-PI4 Tailscale SSH status: `pass`.
- Direct Tailscale is preferred for travel/off-LAN access because local WiFi subnets may overlap home LAN ranges.

## PI500 route blocker closeout
- Recorded: 2026-06-21T15:39:51-05:00
- PI500 Tailscale subnet-route blocker is closed as superseded.
- Direct PI4 Tailscale access validates PI500-to-PI4 SSH while traveling/off-LAN.
- PI4 Tailscale IP: `100.114.132.97`.

## Travel-Safe Tailscale-First Access Rule
- Updated: 2026-06-21T16:13:03-05:00
- Greg travels frequently; Colby infrastructure access must prefer stable Tailscale endpoints over home LAN addresses whenever a machine has Tailscale.
- Current Truth publishing uses PI4 Tailscale endpoint `100.114.132.97` so it works at McKenzie and while traveling, as long as ASUSAI/PI4 are logged into Tailscale.
- LAN addresses such as `192.168.86.79` are secondary/local diagnostics only and must not be the primary publish route.

## server.key Security Triage
- Updated: 2026-06-21T16:20:44-05:00
- `/home/cothrang/server.key` was triaged without printing contents.
- Result: `restricted_small_text_no_private_marker`.
- Private-key marker detected: `False`.
- PEM marker detected: `False`.
- Permissions were restricted to `cothrang:cothrang` with mode `0600`.
- Report: `/opt/colby/reports/security/SERVER_KEY_TRIAGE.md`.

## Remote Execution Control Model
- Updated: 2026-06-21T16:27:37-05:00
- Preferred control path is Tailscale plus SSH/API with single-command staged scripts.
- Telnet is not preferred because it lacks modern authentication/security unless constrained by a specific legacy device.
- UI control may be useful when available, but repeatable scripts/API calls are preferred for Colby operations.

## Single-Command Control Surfaces
- Updated: 2026-06-21T16:42:20-05:00
- Report: `/opt/colby/reports/cos/REMOTE_ACCESS_CONTROL_INVENTORY.md`.
- ASUSAI local staged scripts remain the primary control pattern.
- PI4/PI500/GCSnapDragon/Home Assistant are tracked by readiness in the inventory report.

## Current State

Source: `/opt/colby/state/current_state.md`

# Current State

Date:
2026-05-31

Phase:
Foundation Build - Conversation Intelligence Layer

Memory:
Operational

Observation Router:
Operational

Memory Search:
Operational

Reflection Engine:
Operational

Memory Promotion Engine:
Operational

Journal:
Operational

Hermes:
Installed
Operational

Letta:
Not Installed

Home Assistant:
Deferred

Solar Assistant:
Deferred

Open WebUI:
Operational

Context Loader:
Operational

ask_colby:
Operational

Conversation Inventory:
Operational

Conversation Exporter:
Operational

External ChatGPT Import Staging:
Operational

External ChatGPT Import Review:
Operational

Decision/Lesson Retrieval:
Operational

Primary Focus:
Build the conversation review generator for exported OpenWebUI markdown conversations.

Current Approved Next Step:
Create a review-only generator that reads exported conversation markdown and creates candidate files for manual review.

Current Guardrails:
- Do not auto-promote conversation content into memory.
- Do not modify Colby proxy unless required.
- Do not modify OpenWebUI unless required.
- Do not replace the current file-based memory system.
- Back up before edits.
- Prefer read-only discovery before modification.
- Keep changes reversible.

Deferred Focus:
Open WebUI persona integration is deferred until conversation intelligence review workflow is proven.

## Latest After-Action: Governed conversation learning pipeline

Timestamp:
2026-05-31T09:15:21

Summary:
Built and validated a governed pipeline for OpenWebUI conversation inventory, export, review, validation, promotion candidate generation, task-only application, source attribution, and authority validation.

Validation:
Colby-greg correctly identified the conversation review generator as the highest priority and OpenWebUI persona integration as deferred.

## Current Priorities

Source: `/opt/colby/memory/core/current_priorities.md`

# Current Priorities

Priority 1
Move permanently to McKenzie.

Priority 2
Develop Cognitive Workstead.

Priority 3
Build Colby into a cognitive operating system.

Priority 4
Establish sustainable retirement income.

Priority 5
Automate repetitive operational tasks.

Deferred:
Home Assistant read-only Colby integration is active; next priority is proxy/tool wiring and governed summaries.

## Goals

Source: `/opt/colby/memory/core/goals.md`

# Active Goals

Priority 1
Permanent move to McKenzie.

Priority 2
Build Cognitive Workstead.

Priority 3
Develop Colby into a cognitive operating system.

Priority 4
Create sustainable retirement income.

Priority 5
Increase automation and reduce repetitive work.

Priority 6
Preserve institutional knowledge.

Priority 7
Integrate AI with infrastructure, energy systems, and operations.

## Current Capabilities Memory

Source: `/opt/colby/memory/core/current_capabilities.md`

# Current Capabilities

Generated: 2026-06-05T12:07:34

Purpose: Give Colby an accurate operational inventory of what exists now.

## Operational Services

- Conversation Inventory: Operational
  - Path: /opt/colby/services/conversation_indexer/conversation_inventory.py
- Conversation Exporter: Operational
  - Path: /opt/colby/services/conversation_indexer/conversation_exporter.py
- Conversation Review Generator: Operational
  - Path: /opt/colby/services/conversation_review/review_generator.py
- Conversation Review Validator: Operational
  - Path: /opt/colby/services/conversation_review/review_validator.py
- Promotion Candidate Builder: Operational
  - Path: /opt/colby/services/promotion/promotion_candidate_builder.py
- Task Promotion Applier: Operational
  - Path: /opt/colby/services/promotion/apply_task_candidate.py
- Authority Scanner: Operational
  - Path: /opt/colby/services/decision_engine/authority_scan.py
- Authority Validator: Operational
  - Path: /opt/colby/services/decision_engine/authority_validator.py
- After-Action Recorder: Operational
  - Path: /opt/colby/services/state/after_action_recorder.py
- Capability Inventory Generator: Operational
  - Path: /opt/colby/services/state/capability_inventory_generator.py
- Relationship Context Loader: Operational
  - Path: /opt/colby/services/context/relationship_context_loader.py
- Colby Proxy: Operational
  - Path: /opt/colby/services/proxy/colby_proxy.py
- Reality Scan: Operational
  - Path: /opt/colby/services/reality/reality_scan.sh
- Workspace Dashboard: Operational
  - Path: /opt/colby/services/dashboard/workspace_dashboard.py

## Operational Artifacts

- Current Authority Summary: Operational
  - Path: /opt/colby/reports/decision_engine/current_authority_summary.md
- After-Action Reports: Operational (4 item(s))
  - Path: /opt/colby/reports/after_action
- Conversation Exports: Operational (4 item(s))
  - Path: /opt/colby/conversations/exported
- Review Candidates: Operational (4 item(s))
  - Path: /opt/colby/conversations/review_required
- Validated Reviews: Operational (1 item(s))
  - Path: /opt/colby/conversations/validated_review
- Promotion Candidates: Operational (2 item(s))
  - Path: /opt/colby/promotions/candidates
- Applied Promotions: Operational (1 item(s))
  - Path: /opt/colby/promotions/applied

## Deferred / Not Yet Operational

- Open WebUI Persona Integration: Deferred / Not Operational
- Home Assistant OS rebuild: Deferred / Not Operational
- Solar Assistant integration: Deferred / Not Operational
- MQTT architecture: Deferred / Not Operational
- Voice integration: Deferred / Not Operational
- Letta integration: Deferred / Not Operational
- Knowledge graph: Deferred / Not Operational
- Autonomous operations: Deferred / Not Operational

## Operating Interpretation

- Colby can inventory, export, review, validate, and stage conversation-derived learning.
- Colby can generate promotion candidates and apply TASK promotions only.
- Colby can record after-action updates and maintain capability awareness.
- Colby can validate authority conflicts and load the current authority summary.
- Colby should not execute self-modifying commands or apply non-task memory promotions yet.

## 2026-06-21 COS Control Plane

Status: Operational prototype promoted after Greg approval.

New capabilities:
- COS Capability Registry v2 prototype.
- Current Truth health report.
- Persona/workspace boundary test report.
- Safe route/context trace prototype.
- Evidence packet schema.
- Governed action schema.
- COS status object.

Primary locations:
- /opt/colby/state/cos
- /opt/colby/reports/cos
- /opt/colby/services/cos

Boundary:
These are control-plane and reporting capabilities. They do not grant autonomous write/control authority. Governed action remains approval-gated.


## 2026-06-21 Capability Classification Complete

Status: Operational control-plane improvement.

Colby's COS Capability Registry v2 now has zero unclassified or unknown capability entries.

Impact:
- Colby can more reliably describe her own capabilities by layer and risk class.
- Approval-required surfaces are clearer.
- Future routing, dashboards, and governed action checks can use the registry with less ambiguity.

## 2026-06-21 Approval Surface Review

- Approval-required capability review installed for 27 entries.
- Risk counts: {'EXTERNAL_CONTROL': 17, 'WRITES_SYSTEM': 10}.
- Contract counts: {'block_execution': 6, 'future_approval_required': 4, 'governed_action_required': 8, 'read_only_preflight': 9}.
- Active read-only checks may be used only for evidence collection. Memory promotion, Current Truth publishing, prompt edits, proxy-mediated external actions, and system-changing paths require explicit Greg approval plus backup and validation.
- Report: /opt/colby/reports/cos/approval_required_capability_review.md

## 2026-06-21 Governed Action Preflight

- Installed read-only governed action preflight at /opt/colby/services/cos/action_preflight.py.
- The preflight classifies proposed actions as read_only, local_write, system_write, external_control, memory_promotion, publish, blocked_historical, or future_approval_required before execution.
- It emits a decision, approval requirement, required contract, mapped risk class, matched capability, evidence, and draft governed-action contract.
- Memory promotion, Current Truth publish, prompt edits, proxy external actions, and system-control paths require explicit Greg approval plus backup and validation.

## 2026-06-21 Governed Action Preflight Enforcement

- Governed action preflight enforcement installed into proxy, memory promotion, memory update apply, and Current Truth publish paths.
- Unapproved memory promotion, memory update apply, and Current Truth publish now block before mutation or external publication.
- Approval token for an explicitly approved governed run: COLBY_GOVERNED_ACTION_APPROVED=Greg.
- The proxy file was updated on disk; restarting the proxy remains a separate governed system action.
- Report: /opt/colby/reports/cos/GOVERNED_ACTION_PREFLIGHT_ENFORCEMENT.md

## 2026-06-21 Governed Proxy Restart

- colby-proxy.service was restarted and is active after governed preflight enforcement install.
- Repaired classifier validation so natural-language service restart requests classify as system_write / WRITES_SYSTEM, while read-only status checks remain READ_ONLY.
- Running proxy validation passed: /v1/models returned Colby models and a system-admin prompt was blocked by proxy preflight with no action executed.
- Current Truth timer points at the guarded publish script; unattended publishes require explicit COLBY_GOVERNED_ACTION_APPROVED=Greg and otherwise block before publishing.
- Report: /opt/colby/reports/cos/GOVERNED_PROXY_RESTART.md

## 2026-06-21 Fresh Context Correction

- Corrected context freshness behavior: current operational reports are now loaded ahead of older/default memory for natural-language status, accomplishment, priority, and planning questions.
- Removed old Right Turn business context from active current priorities. It remains historical memory only and should not be volunteered as current work unless Greg explicitly asks about historical context.
- Executive daily review now samples recent COS, project, capability, and executive reports first, excluding historical Right Turn noise from current summaries.
- This is a source/context fix, not a phrase-triggered answer route.

## 2026-06-21 Governed Action Audit Log

- Installed governed action audit log at /opt/colby/state/cos/governed_action_audit_log.jsonl.
- Installed recorder/report generator at /opt/colby/services/cos/governed_action_audit_recorder.py.
- Seeded 7 validated governed events from today's COS control-plane work.
- Future governed installers should append one event covering decision, action class, risk class, approval, validation, backups, touched paths, memory update status, publish status, and Current Truth semantic hash.
- Report: /opt/colby/reports/cos/GOVERNED_ACTION_AUDIT_LOG.md

## 2026-06-21 Governed Audit Wiring

- Wired governed action audit recorder into proxy denied-action path, memory promotion block, memory update apply block, and Current Truth publish block.
- Installed /opt/colby/services/cos/record_governed_action.sh helper for future governed installers.
- Audit ledger now contains 12 events including validated denied-path events.
- Denied action recording is fail-open for recording only: safety blocks still execute even if audit recording has a problem.

## 2026-06-21 Governed Action Dashboard
- Installed governed action dashboard generator and reports.
- Dashboard combines governed action audit events, COS status, and approval-required capability review.
- Current operational context now includes /opt/colby/reports/cos/GOVERNED_ACTION_DASHBOARD.md so natural-language answers about blocked, denied, approved, or approval-needed work use fresh governed sources before older memories.
- Publication remains separate and approval-gated.

## 2026-06-21 Housekeeping Agenda
- Installed Housekeeping Brief agenda generator.
- Colby now has a source-backed housekeeping queue from governed action dashboard, COS status, critical path, current priorities, and Greg corrections.
- Conversation policy: at natural pauses, Colby may offer housekeeping; if Greg says yes, she walks items highest priority first with context, recommendation, and options.
- This is not phrase-triggered routing; it is current-context driven and deferrable.

## 2026-06-21 Current Truth COS Governance Sections
- Current Truth exporter now includes COS Status, Governed Action Audit Log, Governed Action Dashboard, Housekeeping Agenda, and Approval Required Capability Review as required source sections.
- This makes external COL-B / ChatGPT Current Truth aware of governance, approval queue, and housekeeping state.
- This repair followed a successful publish where the public files updated, but validation showed the new COS reports were not yet included by the exporter.

## 2026-06-21 Housekeeping Publish Priority Repair
- Housekeeping agenda now treats any approved, validated publish-class action as satisfying the prior blocked Current Truth publish item.
- This prevents a stale denied publish test from remaining top priority after Greg approved and validated a successful Current Truth publish.

## 2026-06-21 Memory Promoter Two-Step Governance
- memory_promoter.py now defaults to proposal-only mode and writes no memory files.
- Durable hypothesis creation requires --apply plus COLBY_GOVERNED_ACTION_APPROVED=Greg.
- This converts the prior blunt block into a safer two-step model: read-only proposal generation first, governed memory promotion second.

## 2026-06-21 Memory Promotion Proposal Review
- Reviewed the first memory_promoter.py proposal-only batch.
- Proposal mode scanned records safely, but no candidates were approved for hypothesis creation.
- Rationale: candidates were already represented by stronger Current Truth/memory sources or were too generic.
- Memory promoter remains useful in proposal mode; apply mode remains approval-gated.

## 2026-06-21 Proxy Denied Test Closeout
- Closed the prior proxy denied restart event as a completed governance validation test.
- Outcome: proxy correctly blocked an unapproved system-write request; no restart was approved or needed.
- Housekeeping now suppresses closed validation denials so they do not appear as live approval requests.

## 2026-06-21 Memory Promoter Denied Closeout
- Closed old memory-promoter denied events as completed validation/review outcomes.
- The original block is superseded by two-step governance.
- Apply mode remains gated; the reviewed proposal batch approved zero hypothesis writes.

## 2026-06-21 Memory Update Denied Closeout
- Closed the old memory update apply denied event as completed validation evidence.
- The denied event was an intentional audit-wiring test against a temporary file.
- Real memory update apply remains governed and requires Greg approval.

## 2026-06-21 Proxy Approval Policy Decision
- colby_proxy.py is classified as governed-active, not broadly approved.
- Normal chat routing, read-only context assembly, model listing, and answer generation remain allowed.
- Service control, Docker/systemd actions, publishing, memory writes, filesystem writes, and external-control actions require governed approval and audit evidence.
- This clears the proxy capability from live housekeeping while preserving safety boundaries.

## 2026-06-21 OpenWebUI Persona Integration Plan
- OpenWebUI Persona Integration now has a controlled implementation plan.
- The plan preserves existing personas: colby-greg, colby-mel, colby-dj, and colby-public.
- Next phase is read-only persona route audit before any OpenWebUI, Docker, service, or proxy changes.
- Risky actions remain governed and approval-gated.

## 2026-06-21 Persona Route Audit
- Phase 1 OpenWebUI Persona Integration read-only route audit passed.
- Validated model-to-user routing, workspace route matrix, public-safe boundary checks, and active persona registry presence.
- Private memory content was not printed.
- Next phase is persona memory isolation contract.

## 2026-06-21 Persona Memory Isolation Contract
- Phase 2 OpenWebUI Persona Integration memory isolation contract passed.
- Validated allowed and denied memory prefixes for Greg, Mel, DJ, and Public.
- Public cannot access private user/workspace memory. Mel and DJ cannot access Greg-private memory unless shared. Greg owner access remains relationship-scoped unless explicitly listed.
- Private memory content was not printed.
- Next phase is proxy route validation.

## 2026-06-21 Current Truth Publish Denied Closeout
- Closed stale Current Truth publish denied events as superseded by later Greg-approved governed publishes.
- Current Truth publish remains approval-gated.
- Housekeeping suppresses old denied publish artifacts so they do not reappear as live work.

## 2026-06-21 Phase 3 Proxy Service Ready
- colby-proxy.service was validated for OpenWebUI Persona Integration Phase 3.
- Service action: already_active.
- /v1/models returned colby, colby-greg, colby-mel, colby-dj, and colby-public.
- Phase 3 proxy route validation may proceed.

## 2026-06-21 Proxy Persona Route Validation
- Phase 3 OpenWebUI Persona Integration proxy route validation passed.
- Validated /v1/models, persona status routes, and public private-workspace denial.
- Validation reports include route result shapes only; full private response content was not printed.
- Next phase is OpenWebUI configuration review.

## Phase 3 Current Truth publish retry completed
- Recorded: 2026-06-21T15:20:57-05:00
- Phase 3 proxy persona route validation passed locally and Current Truth publish retry completed.

## Phase 3 Current Truth closeout publish
- Recorded: 2026-06-21T15:22:11-05:00
- Purpose: publish the retry-success memory/audit delta created after commit `8e09299`.
- Phase 3 proxy persona route validation remains PASS.

## PI500 access parity partial
- Recorded: 2026-06-21T15:32:49-05:00
- ASUSAI can SSH to PI500 over Tailscale at `100.108.205.70`.
- PI500 public key has been authorized on PI4.
- PI500 cannot yet reach PI4 over tested LAN paths while traveling/off-LAN.
- Likely next fix: approve Tailscale subnet routing to the home LAN or install Tailscale directly on PI4.

## PI500 Tailscale subnet route acceptance
- Recorded: 2026-06-21T15:34:27-05:00
- PI500 accepts Tailscale subnet routes while traveling/off-LAN.
- PI500-to-PI4 access status: `blocked`.
- Remaining fix: approve Home Assistant subnet routes or install Tailscale directly on PI4.

## PI4 direct Tailscale access
- Recorded: 2026-06-21T15:37:55-05:00
- PI4 Tailscale IP: `100.114.132.97`.
- ASUSAI has `pi4-ts` / `collector-ts` SSH aliases for direct Tailscale access.
- PI500-to-PI4 Tailscale SSH status: `pass`.
- Direct Tailscale is preferred for travel/off-LAN access because local WiFi subnets may overlap home LAN ranges.

## PI500 route blocker closeout
- Recorded: 2026-06-21T15:39:51-05:00
- PI500 Tailscale subnet-route blocker is closed as superseded.
- Direct PI4 Tailscale access validates PI500-to-PI4 SSH while traveling/off-LAN.
- PI4 Tailscale IP: `100.114.132.97`.

## Colby Codex Bridge
- Recorded: 2026-06-21T15:47:05-05:00
- Codex CLI path: `/home/cothrang/.local/bin/codex`.
- Codex version: `codex-cli 0.141.0`.
- Bridge: `/opt/colby/services/codex/colby_codex_bridge.py`.
- Colby may prepare Codex job proposals.
- Codex execution requires explicit Greg approval.
- Write-capable Codex jobs require `COLBY_GOVERNED_ACTION_APPROVED=Greg` and `--allow-write`.
- Codex is a supervised engineering tool for Colby; it is not a replacement for Colby's private ASUSAI runtime, memory, services, or governance.

## OpenWebUI Persona Integration Phase 4
- Recorded: 2026-06-21T15:54:06-05:00
- Status: `pass_no_upstream_change_required`.
- Report: `/opt/colby/reports/openwebui_persona_config_review.md`.
- Read-only OpenWebUI configuration review completed without Docker restart, service change, proxy change, or private content exposure.

## OpenWebUI Persona Production Readiness
- Recorded: 2026-06-21T15:57:07-05:00
- Status: `production_ready_read_only`.
- Phase 1-4 validations passed.
- Phase 5 upstream implementation is not required by the current review.
- Report: `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.md`.

## OpenWebUI Persona Project Closeout
- Recorded: 2026-06-21T16:03:02-05:00
- Status: Operational.
- Completion: 100%.
- Phase 5 implementation is future-only if new requirements create a governed change need.

## Current Truth Health Generated Service
- Recorded: 2026-06-21T16:07:15-05:00
- Status: `PASS`.
- Service: `/opt/colby/services/cos/current_truth_health.py`.
- Report: `/opt/colby/reports/cos/current_truth_health.md`.
- Current Truth health is now generated by a repeatable local service/report instead of a one-off prototype.

## Travel-Safe Current Truth Publishing
- Updated: 2026-06-21T16:13:03-05:00
- Current Truth publishing is travel-safe: ASUSAI publishes through PI4 over Tailscale using `100.114.132.97`.
- Publisher explicitly uses `/home/cothrang/.ssh/id_ed25519`, so governed sudo launches retain the correct PI4 authentication identity.

## Debug-Only Route Context Trace
- Updated: 2026-06-21T16:23:02-05:00
- `relationship_context_loader.py` supports `--debug-trace` / `--trace-json`.
- Debug mode returns route, authorization, authority tier, source paths, freshness metadata, and counts only.
- Debug mode does not include raw memory content and does not call live tools.

## Home Assistant Remote Work Unblocked
- Updated: 2026-06-21T16:27:37-05:00
- Home Assistant Multi-Site Architecture is no longer fully blocked by physical return to McKenzie.
- Remote read-only architecture, inventory, dashboard/entity review, and planning may proceed now.
- Physical/on-site work and write/control changes remain governed and require Greg approval.

## Right Turn Final Historical-Only Closeout
- Updated: 2026-06-21T16:37:25-05:00
- Right Turn has zero active current-risk references in authoritative current context.
- Current references are corrections/closeouts only; OpenWebUI history archives remain historical evidence.
- Do not volunteer Right Turn as current work unless Greg explicitly asks about historical Right Turn context.

## Remote Access Control Inventory
- Updated: 2026-06-21T16:42:20-05:00
- Read-only inventory captured current single-command control surfaces.
- Ready surfaces: `5`; partial: `0`; blocked/not ready: `3`.
- Preferred model remains Tailscale plus SSH/API with governed approval for writes.

## Current Project Status

Source: `/opt/colby/reports/projects/current_project_status.md`

# Current Project Status

Generated: 2026-06-21T16:42:21

Purpose: Summarize authoritative project registry files for Colby planning and dependency reasoning.

Project Count: 5

## Executive Summary

- Active Projects: 2
- Deferred Projects: 0

## Projects

### Colby Cognitive Operating System

- Source File: /opt/colby/memory/projects/colby_cognitive_operating_system.md
- Status: Active
- Priority: High
- Phase: Foundation
- Completion: 35%
- Owner: Greg

Depends On:
- Conversation Intelligence

Blocks:
- None

Supports:
- Cognitive Workstead

Next Actions:
- Build Project Registry
- Build Dependency Awareness

### Conversation Intelligence

- Source File: /opt/colby/memory/projects/conversation_intelligence.md
- Status: Complete
- Priority: High
- Phase: Complete
- Completion: 100%
- Owner: Greg

Depends On:
- None

Blocks:
- None

Supports:
- Develop Colby into a cognitive operating system
- Open WebUI Persona Integration

Next Actions:
- None

### Home Assistant Multi-Site Architecture

- Source File: /opt/colby/memory/projects/home_assistant_multi_site.md
- Status: Remote Work Unblocked
- Priority: High
- Phase: Remote architecture and inventory
- Completion: 20%
- Owner: Greg

Depends On:
- Tailscale connectivity for remote work
- Greg approval for write/control actions
- McKenzie presence only for physical/on-site changes

Blocks:
- Solar Assistant Integration hardening
- MQTT Architecture hardening
- Voice Layer
- Multi-site monitoring

Supports:
- Infrastructure Automation
- McKenzie operations
- Cognitive Operating System live-status context

Next Actions:
- Build a read-only Home Assistant access and entity inventory snapshot.
- Map safe single-command execution paths for ASUSAI, PI4, PI500, Home Assistant, and GCSnapDragon.
- Keep physical/on-site McKenzie changes gated until Greg approves them explicitly.

### McKenzie Solar Data Bridge

- Source File: /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- Status: Active
- Priority: High
- Phase: Read-only API foundation
- Completion: 60%
- Owner: Greg

Depends On:
- None listed.

Blocks:
- None listed.

Supports:
- None listed.

Next Actions:
- None listed.

### Open WebUI Persona Integration

- Source File: /opt/colby/memory/projects/openwebui_persona_integration.md
- Status: Operational
- Priority: High
- Phase: Production Readiness Complete
- Completion: 100%
- Owner: Greg

Depends On:
- Conversation Intelligence

Blocks:
- None

Supports:
- Colby Cognitive Operating System
- User-specific memory
- Persona-aware routing
- Workspace-aware responses
- Multi-user Colby deployment

Next Actions:
- Use OpenWebUI personas normally
- Track OpenWebUI tool-server DNS cleanup separately if tool endpoints are needed
- Reopen Phase 5 only if future requirements introduce a governed implementation change

## Operating Interpretation

- Project registry files are authoritative for project names, status, phase, completion, dependencies, blockers, and next actions.
- Do not infer projects outside the project registry unless explicitly asked for brainstorming.
- Use this report as the summary layer; use project files as the source of truth.

## Current Milestone Status

Source: `/opt/colby/reports/projects/current_milestone_status.md`

# Current Milestone Status

Generated: 2026-06-21T16:42:21

Purpose: Calculate project progress from milestone registry files.

Milestone Registry Count: 4

## Summary

- Colby Cognitive Operating System: 56% complete (5/9); next: Dependency Awareness
- Conversation Intelligence: 92% complete (11/12); next: Autonomous Project Updates
- Home Assistant Multi-Site Architecture: 18% complete (2/11); next: MQTT Architecture
- Open WebUI Persona Integration: 0% complete (0/0); next: None. All milestones complete.

## Projects

### Colby Cognitive Operating System

- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md
- Completed Milestones: 5
- Remaining Milestones: 4
- Total Milestones: 9
- Calculated Completion: 56%
- Next Milestone: Dependency Awareness

Completed:
- Memory Architecture
- Authority Awareness
- Capability Awareness
- Change Awareness
- Project Awareness

Remaining:
- Dependency Awareness
- Milestone Awareness
- Executive Dashboard
- Autonomous Planning

### Conversation Intelligence

- Source File: /opt/colby/memory/milestones/conversation_intelligence.md
- Completed Milestones: 11
- Remaining Milestones: 1
- Total Milestones: 12
- Calculated Completion: 92%
- Next Milestone: Autonomous Project Updates

Completed:
- Conversation Inventory
- Conversation Export
- Review Generator
- Review Validator
- Promotion Candidate Builder
- Authority Validator
- Project Registry
- Dependency Registry
- Critical Path Engine
- Capability Registry Generator
- Project Impact Analysis

Remaining:
- Autonomous Project Updates

### Home Assistant Multi-Site Architecture

- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md
- Completed Milestones: 2
- Remaining Milestones: 9
- Total Milestones: 11
- Calculated Completion: 18%
- Next Milestone: MQTT Architecture

Completed:
- Initial Architecture
- Remote Access / Architecture Work Unblocked

Remaining:
- MQTT Architecture
- Solar Assistant Integration
- Multi-Site Connectivity
- Voice Layer
- Production Deployment
- Remote Read-Only Entity Inventory
- Remote Execution Control Plan
- MQTT Architecture Review
- Voice Layer Plan

### Open WebUI Persona Integration

- Source File: /opt/colby/memory/milestones/openwebui_persona_integration.md
- Completed Milestones: 0
- Remaining Milestones: 0
- Total Milestones: 0
- Calculated Completion: 0%
- Next Milestone: None. All milestones complete.

Completed:
- None

Remaining:
- None

## Operating Interpretation

- Milestone status is the authoritative source for calculated completion percentage.
- Project files remain authoritative for project name, status, phase, dependencies, blockers, and ownership.
- Use milestone status to answer progress, remaining work, and next milestone questions.
- Do not rely on manually entered project completion percentages when milestone status exists.

## Current Dependency Status

Source: `/opt/colby/reports/projects/current_dependency_status.md`

# Current Dependency Status

Generated: 2026-06-21T16:42:21

Purpose: Map project dependencies, blockers, supported outcomes, and critical-path signals.

Project Count: 5

## Dependency Map

### Colby Cognitive Operating System
- Status: Active
- Phase: Foundation
- Completion: 35%
- Depends On:
  - Conversation Intelligence (known project)
- Blocks:
  - None
- Supports:
  - Cognitive Workstead

### Conversation Intelligence
- Status: Complete
- Phase: Complete
- Completion: 100%
- Depends On:
  - None
- Blocks:
  - None
- Supports:
  - Develop Colby into a cognitive operating system
  - Open WebUI Persona Integration

### Home Assistant Multi-Site Architecture
- Status: Remote Work Unblocked
- Phase: Remote architecture and inventory
- Completion: 20%
- Depends On:
  - Tailscale connectivity for remote work (external or not registered)
  - Greg approval for write/control actions (external or not registered)
  - McKenzie presence only for physical/on-site changes (external or not registered)
- Blocks:
  - Solar Assistant Integration hardening
  - MQTT Architecture hardening
  - Voice Layer
  - Multi-site monitoring
- Supports:
  - Infrastructure Automation
  - McKenzie operations
  - Cognitive Operating System live-status context

### McKenzie Solar Data Bridge
- Status: Active
- Phase: Read-only API foundation
- Completion: 60%
- Depends On:
  - None
- Blocks:
  - None
- Supports:
  - None

### Open WebUI Persona Integration
- Status: Operational
- Phase: Production Readiness Complete
- Completion: 100%
- Depends On:
  - Conversation Intelligence (known project)
- Blocks:
  - None
- Supports:
  - Colby Cognitive Operating System
  - User-specific memory
  - Persona-aware routing
  - Workspace-aware responses
  - Multi-user Colby deployment

## Blocked / Deferred Signals

- No deferred projects found.

## Critical Path Signals

- Home Assistant Multi-Site Architecture blocks: Solar Assistant Integration hardening, MQTT Architecture hardening, Voice Layer, Multi-site monitoring
- Conversation Intelligence remains a critical path dependency for Open WebUI Persona Integration.
- Home Assistant Multi-Site Architecture remains dependent on return to McKenzie.

## Operating Interpretation

- Use project registry files as source of truth.
- Use this dependency report for impact analysis and sequencing.
- Do not infer dependencies outside registered project files unless Greg requests brainstorming.

## Current Critical Path

Source: `/opt/colby/reports/projects/current_critical_path.md`

# Current Critical Path

Generated: 2026-06-21T16:42:21

Purpose: Identify blocked projects, unblock criteria, impact, and recommended critical-path focus.

Blocker Registry Count: 2

## Home Assistant Multi-Site Architecture

- Source File: /opt/colby/memory/blockers/home_assistant_multi_site.md
- Status: Partially Unblocked
- Priority: High
- Risk: Medium
- Impact: Remote planning and validation can proceed now; physical McKenzie changes remain gated.

Blocked By:
- Physical/on-site McKenzie work remains blocked until Greg is at McKenzie or explicitly approves remote changes with validated access.

Unblock Criteria:
- Remote read-only Home Assistant access available through Tailscale/browser/API.
- Architecture planning, entity inventory, dashboard review, MQTT review, and documentation may proceed remotely.
- Physical device changes, destructive HA changes, credential rotation, add-on restarts, and production write actions require explicit governed approval.

## Open WebUI Persona Integration

- Source File: /opt/colby/memory/blockers/openwebui_persona_integration.md
- Status: Complete
- Priority: None
- Risk: Medium
- Impact: Production-ready for governed read-only persona model routing

Blocked By:
- None

Unblock Criteria:
- Completed

## Executive Summary

Blocked Projects: 0

## Recommended Critical-Path Focus

- Complete remaining Conversation Intelligence milestones before Open WebUI Persona Integration.
- Treat Return to McKenzie as the external dependency for Home Assistant Multi-Site Architecture.
- Do not prioritize blocked downstream integrations ahead of their unblock criteria.

## Operating Interpretation

- Blocker registry files are authoritative for blocked projects and unblock criteria.
- Critical path recommendations must not override Current Authority Summary.
- A dependency may block completion without blocking all parallel development.

## Current Capability Status

Source: `/opt/colby/reports/capabilities/current_capability_status.md`

# Current Capability Status

Generated: 2026-06-21T16:42:21

Purpose: Inventory operational and planned capabilities from milestone registries.

Capability Count: 32

## Summary

- Operational Capabilities: 18
- Planned Capabilities: 14

## Operational Capabilities

### Memory Architecture
- Status: Operational
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Authority Awareness
- Status: Operational
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Capability Awareness
- Status: Operational
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Change Awareness
- Status: Operational
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Project Awareness
- Status: Operational
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Conversation Inventory
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Conversation Export
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Review Generator
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Review Validator
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Promotion Candidate Builder
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Authority Validator
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Project Registry
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Dependency Registry
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Critical Path Engine
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Capability Registry Generator
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Project Impact Analysis
- Status: Operational
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### Initial Architecture
- Status: Operational
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Remote Access / Architecture Work Unblocked
- Status: Operational
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

## Planned Capabilities

### Dependency Awareness
- Status: Planned
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Milestone Awareness
- Status: Planned
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Executive Dashboard
- Status: Planned
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Autonomous Planning
- Status: Planned
- Project: Colby Cognitive Operating System
- Source File: /opt/colby/memory/milestones/colby_cognitive_operating_system.md

### Autonomous Project Updates
- Status: Planned
- Project: Conversation Intelligence
- Source File: /opt/colby/memory/milestones/conversation_intelligence.md

### MQTT Architecture
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Solar Assistant Integration
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Multi-Site Connectivity
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Voice Layer
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Production Deployment
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Remote Read-Only Entity Inventory
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Remote Execution Control Plan
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### MQTT Architecture Review
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

### Voice Layer Plan
- Status: Planned
- Project: Home Assistant Multi-Site Architecture
- Source File: /opt/colby/memory/milestones/home_assistant_multi_site.md

## Operating Interpretation

- Completed milestones are treated as operational capabilities.
- Incomplete milestones are treated as planned capabilities.
- Capability status is derived from milestone registry files.
- Use this report for capability questions before inferring from projects or general memory.

## McKenzie Solar Data Bridge

Source: `/opt/colby/memory/projects/mckenzie_solar_data_bridge.md`

# Project: McKenzie Solar Data Bridge

Project:
McKenzie Solar Data Bridge

Status:
Active

Priority:
High

Owner:
Greg

Phase:
Read-only API foundation

Completion:
60%

Objective:
Allow Colby to answer questions about McKenzie solar, battery, load, survivability, anomalies, and operating status using read-only data from the Pi4 solar SQLite database.

Current Working System:
- Pi4 hostname: pi4
- Pi4 IP: 192.168.86.79
- Pi4 user: cothrang
- Solar Assistant IP: 192.168.86.69
- MQTT port: 1883
- Collector service: solar-collector.service
- Collector path: /home/cothrang/solar-collector
- SQLite database: /home/cothrang/solar-collector/solar.db
- Website repo: /home/cothrang/CognitiveWorkstead
- Live JSON: /home/cothrang/CognitiveWorkstead/solarstatus.json
- Dashboard URL: https://www.cognitiveworkstead.com/mckenzie-solar.html

Current Pipeline:
Solar Assistant MQTT -> Pi4 collector -> solar.db -> solarstatus_json.py -> solarstatus.json -> GitHub Pages dashboard

Current Status:
- MQTT collector is working.
- GitHub push is working.
- Dashboard updates are restored.
- update_dashboard.sh runs every 5 minutes by cron.
- Occupancy display uses label/confidence correctly:
  away + 95 = AWAY / Confidence: 95%

Boundaries:
- Do not connect Colby directly to MQTT first.
- Do not allow Colby to write to solar.db.
- Do not allow Colby to modify GitHub/dashboard files.
- Build a read-only API layer first.
- Treat SQLite analytics as source of truth.

Recommended Architecture:
Pi4 solar.db -> read-only FastAPI service on Pi4 port 5057 -> AsusAI/Colby tool call -> Colby answers questions.

Initial API Endpoints:
- GET /solar/now
- GET /solar/today
- GET /solar/history?hours=24
- GET /solar/survivability
- GET /solar/anomalies
- GET /solar/status

Validation From AsusAI:
curl http://192.168.86.79:5057/solar/now

Colby Prompt Rule:
When asked about McKenzie solar, call the solar API first. Treat returned data as source of truth. Do not guess. Clearly label facts, inferences, and recommendations.

Example Questions:
- How much solar did we produce today?
- How long can McKenzie survive with no solar?
- Was today normal for this weather?
- Did load spike while we were away?
- What should we do before tomorrow's clouds?


## 2026-06-05 - McKenzie Solar Dashboard V1 Stable

Status:
Operationally stable.

Completed:
- Dashboard generation pipeline restored.
- Automated GitHub publishing restored.
- Validation gate added before commit/push.
- Stale-data detection verified.
- Production tracking added.
- Expected-vs-actual solar analytics added.
- Sunset SOC forecasting added.
- Survivability forecasting verified.
- Seasonal-best array tracking added.
- Battery power reporting corrected.
- MQTT, occupancy, weather, dashboard generation, validation, and deployment pipelines verified.

Current Capability:
The McKenzie Solar dashboard now supports real-time solar/battery/load status, historical production intelligence, expected-vs-actual production tracking, projected sunset SOC, survivability forecasts, occupancy awareness, weather awareness, and validation-gated publishing.

Known Boundary:
Historical Solar Assistant Grafana exports are downsampled and should not be treated as authoritative peak-record data. Live PI4 observed records are the source for season-best tracking going forward.

Next Priorities:
1. Reolink sky camera integration.
2. EM16P circuit-level load intelligence.
3. Visual sky-condition analysis.
4. Appliance-level attribution.
5. Solar anomaly detection.

## 2026-06-09 MQTT authentication restore

PI4 McKenzie Solar collector was restored after MQTT authentication was enabled.

Confirmed architecture:

- PI4 collector source: authenticated direct SolarAssistant MQTT at `192.168.86.69:1883`.
- PI4 does not currently use HA Mosquitto as the McKenzie dashboard collector source.
- Home Assistant remains a separate operational sensor/control plane.
- MQTT passwords must remain local-only and must not be published, logged, or stored in Current Truth/model memory.

Validation after restore:

- PI4 `/solar/now` refreshed to current data.
- PI4 `/solar/bridge` refreshed to current data.
- Public dashboard JSON was verified current after GitHub Pages cache bypass.
- GitHub Pages may cache `solarstatus.json` for approximately 10 minutes.

Former follow-up:

- `/solar/anomalies` previously returned HTTP 500 due to a missing `inverter_temp_f` column reference in the endpoint query.
- This was resolved later on 2026-06-09 by joining `energy_analysis` with `solar_metrics_1min`.
- Current status: resolved.

## 2026-06-09 /solar/anomalies endpoint fixed

Status:
Resolved.

Issue:
PI4 `/solar/anomalies` returned HTTP 500 because `solar_api.py` queried `inverter_temp_f` from the `energy_analysis` view, but that column exists in `solar_metrics_1min`, not `energy_analysis`.

Fix:
Updated `/home/cothrang/solar-collector/solar_api.py` so `/solar/anomalies` joins:

- `energy_analysis e`
- `solar_metrics_1min s`

on `bucket_utc`, then reads `s.inverter_temp_f`.

Validation:
After restarting `solar-api.service`, the following endpoints returned HTTP 200:

- `/solar/status`
- `/solar/now`
- `/solar/bridge`
- `/solar/anomalies`

Boundary:
This fix touched only the read-only PI4 solar API. It did not modify MQTT collection, dashboard generation, GitHub publishing, Home Assistant, or solar.db schema.

## 2026-06-09 McKenzie solar live evidence packet guardrails

Status:
Active candidate architecture.

Tool:
`/opt/colby/tools/mckenzie_solar_evidence.py`

Purpose:
Coach Colby to answer McKenzie solar questions from live evidence and Current Truth, not canned responses or stale memory.

Design:
The tool fetches read-only PI4 solar API data and returns source, timestamp, freshness, and current values.

The tool does not answer user questions directly.
The tool does not hard-code canned responses.
The tool does not call Home Assistant services.
The tool does not access MQTT directly.
The tool does not store or expose secrets.

Reasoning guardrails:
- Do not answer current McKenzie solar questions from memory alone.
- Use live PI4 API evidence when available.
- Report value, source, Central Time timestamp, and freshness state.
- If live evidence is stale, missing, or conflicting, say the current state is not verified and identify the source problem.
- Prefer verified PI4 API live data over public GitHub Pages JSON for current state because GitHub Pages may cache for approximately 10 minutes.
- Use Home Assistant read-only snapshot as supporting evidence when fresh.
- Do not infer array faults from low solar without supporting evidence.
- High battery SOC may indicate charge taper.
- Weather is supporting evidence only.
- Keep McKenzie fixed-site solar separate from RiVi RV power.

Best snapshot rule:
The evidence packet preserves raw `/solar/now` and `/solar/bridge` data. It also creates `best_current_snapshot`.

If `/solar/now` has missing operational fields but `/solar/bridge` has complete current values, `best_current_snapshot` selects `/solar/bridge` and explains why.

This is not a hard-coded answer. It is source quality selection.

## 2026-06-09 Live Colby routing for current McKenzie solar questions

Status:
Operational and validated.

Summary:
Colby's live OpenAI-compatible proxy on ASUSAI now routes current McKenzie solar state questions through the live evidence packet tool before generating an answer.

Runtime files:
- `/opt/colby/services/proxy/colby_proxy.py`
- `/opt/colby/services/context/relationship_context_loader.py`
- `/opt/colby/tools/mckenzie_solar_evidence.py`

Behavior:
- Current-status questions such as current SOC, current solar, current load, current battery state, charging, or discharging are routed to `/opt/colby/tools/mckenzie_solar_evidence.py`.
- The evidence tool returns `best_current_snapshot`, source, Central Time timestamp, freshness, and raw PI4 `/solar/now` and `/solar/bridge` snapshots.
- The model is instructed to reason from the evidence packet, not use canned answers.
- Broader analytics questions may still use McKenzie Solar Analytics Context for history, production, survivability, array, or trend analysis.

Validation:
- `relationship_context_loader.py` detected `Detected Route: solar` for `What is the current SOC at McKenzie?`.
- Context output included `McKenzie Solar Live Evidence Packet`.
- Context output included `best_current_snapshot`.
- `colby-proxy.service` restarted cleanly.
- Local OpenAI-compatible proxy test returned a live current SOC answer from PI4 evidence.
- Test answer reported McKenzie SOC as 98.0% with Central Time freshness from the live evidence packet.

Governance:
- This is not a hard-coded response.
- No SOC value is embedded in the proxy or prompt as a static answer.
- Code collects evidence and injects guardrails; the model still generates the final answer from live evidence.
- No Home Assistant services are called.
- No MQTT credentials are exposed.
- No write access to PI4 solar database, Home Assistant, SolarAssistant, GitHub, or dashboard files is added.

Supersedes:
- Failed change record `a2b5b576c290`.
- Partial patch attempts at `20260609_154542` and `20260609_154740`.

## 2026-06-10 Combined McKenzie and RiVi energy evidence routing

Status:
Operational and validated.

Summary:
Colby's live OpenAI-compatible proxy on ASUSAI now supports combined current-energy questions across McKenzie fixed-site solar and RiVi RV Victron power while keeping the two systems separate.

Runtime files:
- `/opt/colby/tools/energy_systems_evidence.py`
- `/opt/colby/tools/mckenzie_solar_evidence.py`
- `/home/cothrang/colby-ha/ha_state_pull.py`
- `/home/cothrang/colby-ha/ha_state_snapshot.json`
- `/opt/colby/services/proxy/colby_proxy.py`

Behavior:
- Combined questions mentioning McKenzie and RiVi route through `/opt/colby/tools/energy_systems_evidence.py`.
- McKenzie current values use the PI4 live solar evidence packet as the preferred current source.
- RiVi current values use the Home Assistant read-only snapshot allowlist.
- Answers must keep McKenzie and RiVi separate unless Greg explicitly asks for totals.
- Answers must include source, Central Time timestamp, and freshness state for each system.
- RiVi battery power sign convention is not yet validated, so Colby must not infer RiVi charging or discharging from sign alone.

Validated local proxy test:
Question:
`What is the current SOC for both McKenzie Solar and RiVi?`

Validated answer included:
- McKenzie Solar SOC: 62.0%
- McKenzie source: PI4 solar API live endpoint
- McKenzie freshness: current
- RiVi RV Victron SOC: 86.7%
- RiVi source: Home Assistant read-only snapshot
- RiVi freshness: current

Governance:
- This is read-only evidence routing.
- No Home Assistant service calls are enabled.
- No device control was added.
- No MQTT credentials are exposed.
- McKenzie fixed-site solar and RiVi RV Victron power remain separate operational systems.

Change record:
`0cb2cd5bc6a5`

## Home Assistant Read-Only Access

Source: `/opt/colby/memory/operational/home_assistant_readonly_colby_access.md`

# Home Assistant Read-Only Access for Colby

Status: active as of 2026-06-09 14:11 Central Time.

## Confirmed State

ASUSAI has validated read-only Home Assistant REST API access.

Home Assistant endpoints:
- External: https://ha.gregcothran.com
- Local: http://192.168.86.222:8123

ASUSAI read-only files:
- Pull script: /home/cothrang/colby-ha/ha_state_pull.py
- Snapshot file: /home/cothrang/colby-ha/ha_state_snapshot.json
- Token env file: /home/cothrang/.config/colby-ha/ha.env

The HA token is stored only on ASUSAI in the local env file. It must never be pasted into prompts, proxy context, model memory, Current Truth, GitHub, logs, or chat transcripts.

## Security Boundary

Home Assistant remains the sensor/control plane.

Colby remains the reasoning/reporting layer.

Colby may read the generated HA snapshot.

Colby may summarize operational facts from the snapshot.

Colby must not call Home Assistant services.

Colby must not write Home Assistant state.

Colby must not control switches, buttons, numbers, selects, time entities, climate entities, inverter entities, charger entities, relay entities, or ESS entities without Greg’s explicit approval.

## Access Method

- GET-only Home Assistant REST API.
- Selected allowlisted entities only.
- No POST.
- No DELETE.
- No /api/services.
- No destructive actions.
- No write/control entities exposed to Colby by default.

## Current Allowlisted Scope

RiVi:
- Battery watts.
- Battery state of charge.
- Battery charge cycles.
- PV watts.
- Consumption/load watts.
- MultiPlus AC input watts.
- MultiPlus AC output watts.

McKenzie:
- Battery state of charge.
- Battery power.
- Load power.
- Grid CT power.

## Validation

Validated on 2026-06-09 14:11:22 Central Time.

The read-only puller successfully queried Home Assistant from ASUSAI using GET /api/states/{entity_id}.

The selected allowlist returned ok:true for RiVi and McKenzie entities.

Validated sample:
- sensor.gx_device_pv_power returned successfully from Home Assistant.

## Operational Separation

McKenzie fixed-site solar and Home Assistant operations remain separate from RiVi RV Victron operations.

Home Assistant is the operational sensor/control plane.

Colby is the reasoning/reporting layer.

Future HA control must be approval-gated, auditable, and executed through Home Assistant scripts or automations, not direct uncontrolled model actions.

## Constraints

Source: `/opt/colby/memory/core/constraints.md`

# Constraints

Internet:
McKenzie internet bandwidth is limited.

Compute:
Single RTX 3090.

Memory:
Long-term memory architecture not yet implemented.

Automation:
Home Assistant not currently integrated.

Safety:
No autonomous infrastructure changes without approval.

Knowledge:
Must distinguish between observations, decisions, lessons, and knowledge.

Operations:
Prefer reversible actions.
Prefer backup before modification.
Prefer observation before action.

## 20260530_090116 - Imported Operating Constraints

- Investigate thoroughly before edits.
- Prefer read-only discovery first.
- Back up files before modification.
- Avoid assumptions.
- Use easy copy-paste commands.
- Do not modify Colby proxy unless required.
- Do not modify OpenWebUI unless required.
- Do not modify the memory learning pipeline unless required.

## Limitations

Source: `/opt/colby/memory/core/limitations.md`

# Current Limitations

Cannot:

- Access Home Assistant
- Access Solar Assistant
- Access MQTT
- Execute autonomous infrastructure changes
- Verify visual webpage rendering
- Persist memories automatically
- Correlate historical observations automatically
- Learn from outcomes automatically

Requires Human Approval:

- Container rebuilds
- System upgrades
- DNS changes
- Firewall changes
- Network modifications
- Data deletion
- Volume deletion

Future Expansion:

- Home Assistant OS
- Solar Assistant
- Letta
- Observation Router
- Memory Engine
- Voice Interface

## 2026-06-01 - Open WebUI Stale Context During UAT

Limitation:
Existing Open WebUI chat sessions may retain stale model context after memory, prompt, or context-loader changes.

Impact:
A memory or prompt fix may appear to fail if tested inside an old chat session.

Validation Rule:
After changes to memory files, relationship files, context loader behavior, or proxy prompt behavior, validation should be performed in a new Open WebUI chat.

Known Example:
Mel's registered Architect fact and Greg-Mel relationship context worked in a new chat after profile and relationship memory updates, while older chats could still reflect stale context.

## COS Status

Source: `/opt/colby/reports/cos/COS_STATUS.md`

# COS Status

Generated: 2026-06-21T05:57:22-05:00

## Phase

- foundation_control_plane

## Active Control Plane

- governed_action_schema: present
- evidence_schema: present
- route_trace: present
- project_metadata: present
- approval_surface_review: present
- governed_action_preflight: present
- governed_action_preflight_enforcement: present
- governed_action_audit_log: present
- governed_action_dashboard: active
- housekeeping_agenda: active
- openwebui_persona_integration_plan: active
- persona_route_audit: PASS
- persona_memory_isolation_contract: PASS
- phase3_proxy_service_ready: PASS
- proxy_persona_route_validation: PASS

## Next Actions

- Build Phase 4 OpenWebUI configuration review for OpenWebUI Persona Integration.
- Use governed action dashboard as the first source for approval, denial, blocked-action, and needs-Greg status.
- Convert current_truth_health into a generated service/report.
- Wire route_context_trace into a debug-only context loader mode.

## Phase 3 Current Truth Publish Retry

- Recorded: 2026-06-21T15:20:57-05:00
- Status: PUBLISHED.
- Report: `/opt/colby/reports/cos/current_truth_publish_retry_after_phase3.md`

## Phase 3 Current Truth Closeout Publish

- Recorded: 2026-06-21T15:22:11-05:00
- Status: READY TO PUBLISH.
- Purpose: publish the retry-success memory/audit delta created after commit `8e09299`.

## PI500 Access Parity

- Recorded: 2026-06-21T15:32:49-05:00
- Status: PARTIAL. ASUSAI to PI500 over Tailscale is PASS; PI500 to PI4 is blocked by route reachability.

## PI500 Tailscale Subnet Route Acceptance

- Recorded: 2026-06-21T15:34:27-05:00
- Status: BLOCKED after accept-routes.

## PI4 Direct Tailscale Access

- Recorded: 2026-06-21T15:37:55-05:00
- PI4 Tailscale IP: `100.114.132.97`.
- PI500-to-PI4 Tailscale SSH: `pass`.

## PI500 Route Blocker Closeout

- Recorded: 2026-06-21T15:39:51-05:00
- Status: CLOSED.
- Superseded by direct PI4 Tailscale access.
- PI500-to-PI4 Tailscale SSH: PASS.

## Colby Codex Bridge

- Recorded: 2026-06-21T15:47:05-05:00
- Status: INSTALLED.
- Proposal mode: active.
- Execution mode: approval-gated.

## OpenWebUI Persona Integration Phase 4

- Recorded: 2026-06-21T15:54:06-05:00
- Status: `pass_no_upstream_change_required`.
- Report: `/opt/colby/reports/openwebui_persona_config_review.md`.

## OpenWebUI Persona Production Readiness

- Recorded: 2026-06-21T15:57:07-05:00
- Status: `production_ready_read_only`.
- Phase 5 implementation required: false.
- Report: `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.md`.

## OpenWebUI Persona Project Closeout

- Recorded: 2026-06-21T16:03:02-05:00
- Status: Operational.
- Completion: 100%.

## Current Truth Health Generated Service

- Recorded: 2026-06-21T16:07:15-05:00
- Status: `PASS`.
- Service: `/opt/colby/services/cos/current_truth_health.py`.
- Report: `/opt/colby/reports/cos/current_truth_health.md`.
## Current Truth Publisher PI4 Tailscale Repair
- Updated: 2026-06-21T16:11:03-05:00
- Status: PASS
- Publisher target: PI4 Tailscale `100.114.132.97`
- Authentication: explicit ASUSAI `cothrang` SSH identity for sudo-safe publish runs
## Travel-Safe Current Truth Publishing Closeout
- Updated: 2026-06-21T16:13:03-05:00
- Status: PASS
- Current Truth publisher is Tailscale-first through PI4 `100.114.132.97`.
- This route is intended to work both at McKenzie and while Greg is traveling, provided the participating machines are logged into Tailscale.
## server.key Security Triage
- Updated: 2026-06-21T16:20:44-05:00
- Status: PASS
- Result: `restricted_small_text_no_private_marker`
- Contents printed: `False`
- Permissions: `cothrang:cothrang 0600`
- Report: `/opt/colby/reports/security/SERVER_KEY_TRIAGE.md`
## Debug-Only Route Context Trace
- Updated: 2026-06-21T16:23:02-05:00
- Status: PASS
- Normal context loader output unchanged.
- Debug mode: `/opt/colby/services/context/relationship_context_loader.py --debug-trace <user> [workspace] [question]`
- Safety: metadata only; no raw private memory content; no live tool calls.
## Home Assistant Remote Work Unblocked
- Updated: 2026-06-21T16:27:37-05:00
- Status: PASS
- HA architecture/read-only inventory work can proceed remotely.
- Physical McKenzie work and HA write/control operations remain governed.
- Control plan: `/opt/colby/reports/cos/REMOTE_EXECUTION_CONTROL_PLAN.md`
## Right Turn Final Historical-Only Closeout
- Updated: 2026-06-21T16:37:25-05:00
- Status: PASS
- Active current-risk references: `0`
- Archived DB/vector matches are historical evidence only.
## Right Turn Housekeeping Generator Repair
- Updated: 2026-06-21T16:38:33-05:00
- Status: PASS
- Closed Right Turn historical-only correction item is no longer re-added to housekeeping.
## Remote Access Control Inventory
- Updated: 2026-06-21T16:42:20-05:00
- Status: PASS
- Ready surfaces: `5`
- Partial surfaces: `0`
- Blocked/not ready surfaces: `3`
- Report: `/opt/colby/reports/cos/REMOTE_ACCESS_CONTROL_INVENTORY.md`

## Governed Action Audit Log

Source: `/opt/colby/reports/cos/GOVERNED_ACTION_AUDIT_LOG.md`

# Governed Action Audit Log

Generated: 2026-06-21T16:42:20-05:00
Source: /opt/colby/state/cos/governed_action_audit_log.jsonl

## Summary

- Events: 59
- Decisions: {'approved': 43, 'approval_required': 16}
- Risk classes: {'WRITES_LOCAL': 38, 'WRITES_SYSTEM': 6, 'EXTERNAL_CONTROL': 15}
- Action classes: {'local_write': 35, 'system_write': 6, 'memory_promotion': 3, 'publish': 14, 'external_control': 1}
- Status: {'validated': 40, 'denied': 15, 'ready_to_publish': 1, 'partial_blocked': 1, 'blocked': 1, 'approved_completed': 1}

## Recent Events

### Phase 3 Current Truth closeout publish

- Event ID: `gaa_f8fba6d33a77ccec`
- Occurred: 2026-06-21T15:22:11-05:00
- Decision: `approved`
- Action class: `publish`
- Risk class: `EXTERNAL_CONTROL`
- Status: `ready_to_publish`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/phase3_current_truth_closeout_publish_20260621_152211`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `23eaab0ba76963fe9a4d703e882416cd01e401d7e4fb8b3a7f1dcb4a5ef3c81f`

Touched paths:
- `/opt/colby/reports/cos/phase3_current_truth_closeout_publish.md`
- `/opt/colby/reports/cos/phase3_current_truth_closeout_publish.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/state/cos/cos_status.json`

Validations:
- phase3_local_validation: `PASS`
- prior_publish: `PASS_PUBLISHED`

Notes:
- Recorded before publish so the closeout event is included in the public Current Truth without creating a post-publish delta.

### Grant PI500 PI4 access parity partial

- Event ID: `gaa_055e3a7175202840`
- Occurred: 2026-06-21T15:32:49-05:00
- Decision: `approved`
- Action class: `external_control`
- Risk class: `EXTERNAL_CONTROL`
- Status: `partial_blocked`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/pi500_pi4_access_parity_20260621_153232`
- Memory updated: `True`
- Publish status: `local_current_truth_regenerated`
- Current Truth semantic SHA256: `5ed8e63ae923b6a17e8df67cfaa9b2e59c2d866314f8e1e71198441846c6bfd8`

Touched paths:
- `/opt/colby/reports/cos/pi500_pi4_access_parity.md`
- `/opt/colby/reports/cos/pi500_pi4_access_parity.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`

Validations:
- asusai_to_pi500_tailscale_ssh: `PASS`
- pi500_key_authorized_on_pi4: `PASS`
- pi500_to_pi4_ssh: `BLOCKED_ROUTE`

Notes:
- PI500 needs Tailscale subnet routing or direct PI4 Tailscale access to complete off-LAN PI4 parity.

### Enable PI500 Tailscale subnet route acceptance

- Event ID: `gaa_7fb2cc8cf88ffdcd`
- Occurred: 2026-06-21T15:34:27-05:00
- Decision: `approved`
- Action class: `system_write`
- Risk class: `WRITES_SYSTEM`
- Status: `blocked`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/pi500_tailscale_subnet_route_acceptance_20260621_153411`
- Memory updated: `True`
- Publish status: `local_current_truth_regenerated`
- Current Truth semantic SHA256: `4704568ffdf102fede2a012c98b3ebc2bdc2e34dcfc0e2c4a98cd763847a692a`

Touched paths:
- `/opt/colby/reports/cos/pi500_tailscale_subnet_route_acceptance.md`
- `/opt/colby/reports/cos/pi500_tailscale_subnet_route_acceptance.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`

Validations:
- asusai_to_pi500_tailscale_ssh: `PASS`
- pi500_accept_routes: `ENABLED`
- pi500_to_pi4: `blocked`

Notes:
- Enabled PI500 Tailscale accept-routes to support off-LAN access parity.

### Install PI4 direct Tailscale access

- Event ID: `gaa_012c0cefb1f62a94`
- Occurred: 2026-06-21T15:37:55-05:00
- Decision: `approved`
- Action class: `system_write`
- Risk class: `WRITES_SYSTEM`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/pi4_direct_tailscale_access_20260621_153552`
- Memory updated: `True`
- Publish status: `local_current_truth_regenerated`
- Current Truth semantic SHA256: `25c5cd534e367802ec7985550c1eeedd3e383a1aaf8c2917a4cf34ad4b627eb1`

Touched paths:
- `/opt/colby/reports/cos/pi4_direct_tailscale_access.md`
- `/opt/colby/reports/cos/pi4_direct_tailscale_access.json`
- `/home/cothrang/.ssh/config`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`

Validations:
- asusai_to_pi4_lan_ssh: `PASS`
- asusai_to_pi4_tailscale_ssh: `PASS`
- pi500_to_pi4_tailscale_ssh: `pass`

Notes:
- Direct PI4 Tailscale path avoids travel WiFi/home LAN subnet overlap.

### Close PI500 route blockers after direct PI4 Tailscale success

- Event ID: `gaa_f1aabc6beabcbfbd`
- Occurred: 2026-06-21T15:39:51-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/pi500_route_blocker_closeout_20260621_153951`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `ce7a10d755c10abaf63ea11fd944deab3c358cfcb7f73736bff79c12eecf9e21`

Touched paths:
- `/opt/colby/reports/cos/housekeeping_closeouts.json`
- `/opt/colby/reports/cos/pi500_route_blocker_closeout.md`
- `/opt/colby/reports/cos/pi500_route_blocker_closeout.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`

Validations:
- pi4_direct_tailscale_access: `PASS`
- pi500_to_pi4_tailscale_ssh: `PASS`

Notes:
- Closed stale PI500 subnet-route housekeeping items because direct PI4 Tailscale access completed the parity objective.

### Install Colby Codex Bridge

- Event ID: `gaa_3e253bd8476b11d5`
- Occurred: 2026-06-21T15:47:05-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/colby_codex_bridge_20260621_154705`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `43ad5eda592b903336348969e0cc56c5b536741dc0a3a50339f75148ced0a481`

Touched paths:
- `/opt/colby/services/codex/colby_codex_bridge.py`
- `/opt/colby/reports/codex/COLBY_CODEX_BRIDGE.md`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`

Validations:
- bridge_syntax: `PASS`
- codex_cli_present: `PASS`
- proposal_mode: `PASS`
- unapproved_run_block: `PASS`

Notes:
- Colby can prepare Codex job proposals; execution remains Greg-approved and governed.

### Current Truth publish blocked without approval

- Event ID: `gaa_a52edb841a40a5bc`
- Occurred: 2026-06-21T15:51:35-05:00
- Decision: `approval_required`
- Action class: `publish`
- Risk class: `EXTERNAL_CONTROL`
- Status: `denied`
- Approved by: `None`
- Backup: `None`
- Memory updated: `False`
- Publish status: `blocked_before_publish`
- Current Truth semantic SHA256: `435f391efe3e8d45aff095cb2ca2a72b3981ca39f2c7bbfbb0e0c3c8ca19acb2`

Touched paths:
- `/opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md`
- `/opt/colby/export/knowledge_transfer.json`

Validations:
- action_executed: `NO`
- git_push: `NO`
- preflight: `PASS`
- remote_copy: `NO`
- required_contract: `governed_action_required`

Notes:
- Blocked because COLBY_GOVERNED_ACTION_APPROVED=Greg was not present.
- No publish log, remote copy, commit, or push should occur before approval.

### Complete OpenWebUI Persona Integration Phase 4 configuration review

- Event ID: `gaa_a22e532c02b2cfe4`
- Occurred: 2026-06-21T15:54:06-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/openwebui_phase4_config_review_20260621_155350`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `435f391efe3e8d45aff095cb2ca2a72b3981ca39f2c7bbfbb0e0c3c8ca19acb2`

Touched paths:
- `/opt/colby/services/openwebui/openwebui_phase4_config_review.py`
- `/opt/colby/reports/openwebui_persona_config_review.md`
- `/opt/colby/reports/openwebui_persona_config_review.json`
- `/opt/colby/memory/projects/openwebui_persona_integration.md`
- `/opt/colby/memory/milestones/openwebui_persona_integration.md`

Validations:
- host_proxy_ok: `True`
- phase4_review: `pass_no_upstream_change_required`

Notes:
- Read-only OpenWebUI Phase 4 review completed; Phase 5 remains governed and approval-gated.

### Complete OpenWebUI Persona Integration Production Readiness Review

- Event ID: `gaa_4d1f5f69c84ba2dc`
- Occurred: 2026-06-21T15:57:07-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/openwebui_persona_prr_20260621_155707`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `168f61001eb886947195d6ae39a352d7a0bd5a55f7d10799672fc6621f4b3a15`

Touched paths:
- `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.md`
- `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.json`
- `/opt/colby/memory/projects/openwebui_persona_integration.md`
- `/opt/colby/memory/milestones/openwebui_persona_integration.md`
- `/opt/colby/reports/personas/current_persona_status.md`

Validations:
- phase5_required: `false`
- production_readiness: `production_ready_read_only`

Notes:
- OpenWebUI Persona Integration passed production readiness for governed read-only persona routing.

### Complete OpenWebUI Persona Integration Production Readiness Review

- Event ID: `gaa_ea391ad8d5b3fd49`
- Occurred: 2026-06-21T16:00:30-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/openwebui_persona_prr_20260621_160029`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `8a214f12507ec6a5b0e8c41a63617b07d1404ebae0b39e637293e72df96eed81`

Touched paths:
- `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.md`
- `/opt/colby/reports/personas/openwebui_persona_production_readiness_review.json`
- `/opt/colby/memory/projects/openwebui_persona_integration.md`
- `/opt/colby/memory/milestones/openwebui_persona_integration.md`
- `/opt/colby/reports/personas/current_persona_status.md`

Validations:
- phase5_required: `false`
- production_readiness: `production_ready_read_only`

Notes:
- OpenWebUI Persona Integration passed production readiness for governed read-only persona routing.

### Close OpenWebUI Persona Integration as operational

- Event ID: `gaa_1a08a798b5d1c633`
- Occurred: 2026-06-21T16:03:02-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/openwebui_persona_project_closeout_20260621_160302`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `6f2eb8c753f90b47b307ab7a376574a4f6dda3b937001ba51734180ee5e249a7`

Touched paths:
- `/opt/colby/memory/projects/openwebui_persona_integration.md`
- `/opt/colby/memory/blockers/openwebui_persona_integration.md`
- `/opt/colby/memory/milestones/openwebui_persona_integration.md`
- `/opt/colby/reports/personas/current_persona_status.md`
- `/opt/colby/reports/personas/openwebui_persona_project_closeout.md`
- `/opt/colby/reports/personas/openwebui_persona_project_closeout.json`

Validations:
- critical_path_removed: `PASS`
- openwebui_persona_status: `operational`

Notes:
- Project closed as operational; Phase 5 remains future-only if new requirements require governed implementation.

### Install Current Truth Health generated service

- Event ID: `gaa_9a5d50d6c5137e02`
- Occurred: 2026-06-21T16:07:15-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/current_truth_health_service_20260621_160714`
- Memory updated: `True`
- Publish status: `ready_to_publish`
- Current Truth semantic SHA256: `b73fb3f0d43835ba4cd9e387684821e32c08cba68bd81ffd6c5d2603ddd8919a`

Touched paths:
- `/opt/colby/services/cos/current_truth_health.py`
- `/opt/colby/reports/cos/current_truth_health.md`
- `/opt/colby/reports/cos/current_truth_health.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`

Validations:
- current_truth_health: `PASS`
- json_valid: `PASS`

Notes:
- Promoted Current Truth health from prototype into repeatable generated service/report.

### Repair Current Truth publisher PI4 route

- Event ID: `gaa_e99ea2ac25e3c8ed`
- Occurred: 2026-06-21T16:11:03-05:00
- Decision: `approval_required`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `approved_completed`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/current_truth_publisher_pi4_tailscale_20260621_161051`
- Memory updated: `True`
- Publish status: `pending_retry`
- Current Truth semantic SHA256: `cb9307867e3619a96a9ec821c1dd8229ded71670f072dd9cd6b134a20834dac8`

Touched paths:
- `/opt/colby/services/export/publish_current_truth.sh`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- pi4_tailscale_ssh: `PASS`
- publisher_syntax: `PASS`

Notes:
- The prior publish failed after host-key repair because sudo/root did not use Greg's normal SSH identity and the publisher still targeted PI4 by LAN IP.
- The publisher now uses PI4 Tailscale IP 100.114.132.97 and explicit identity /home/cothrang/.ssh/id_ed25519.

### Close out travel-safe Current Truth publishing route

- Event ID: `gaa_02294c5f982d975e`
- Occurred: 2026-06-21T16:13:03-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/travel_safe_current_truth_publish_closeout_20260621_161302`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `ee1cbc55633e1a141ba42d13311c1b1e523c41ec79caef1dc63295c970d07471`

Touched paths:
- `/opt/colby/reports/cos/housekeeping_closeouts.json`
- `/opt/colby/memory/core/infrastructure_inventory.md`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- pi4_tailscale_ssh: `PASS`
- publisher_tailscale_first: `PASS`

Notes:
- Greg travels frequently, so Colby infrastructure access must use Tailscale-first routing when available.
- Current Truth publishing is closed out as travel-safe through PI4 Tailscale endpoint 100.114.132.97.

### Triage and restrict /home/cothrang/server.key

- Event ID: `gaa_7e494a3d5907cb3b`
- Occurred: 2026-06-21T16:20:44-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/server_key_security_triage_20260621_162044`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `4c2f918829a9c40d1f2276f4024fbc6fdd2a61911dd706e5c5bd3b01596d6165`

Touched paths:
- `/home/cothrang/server.key`
- `/opt/colby/reports/security/server_key_triage.json`
- `/opt/colby/reports/security/SERVER_KEY_TRIAGE.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- content_not_printed: `PASS`
- permissions_restricted: `PASS`
- server_key_status: `restricted_small_text_no_private_marker`

Notes:
- File contents were not printed.
- The file was restricted to owner-only permissions instead of being deleted.

### Install debug-only route context trace

- Event ID: `gaa_094d6c42bdb41140`
- Occurred: 2026-06-21T16:23:02-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/debug_route_context_trace_20260621_162301`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `5779b37c76aaa9ba17e2776850e7498e436ad01775dde63672682e1c908362e3`

Touched paths:
- `/opt/colby/services/context/relationship_context_loader.py`
- `/opt/colby/reports/cos/route_context_trace_report.json`
- `/opt/colby/reports/cos/route_context_trace_report.md`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- debug_trace_metadata_only: `PASS`
- normal_mode_unchanged: `PASS`
- syntax: `PASS`
- unauthorized_case: `PASS`

Notes:
- Debug mode is opt-in only.
- The trace includes paths, route, authorization, freshness, and counts, but not raw memory content.

### Unblock Home Assistant remote work and define remote control plan

- Event ID: `gaa_1df4e504c8cdfbd1`
- Occurred: 2026-06-21T16:27:37-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/home_assistant_remote_unblock_20260621_162737`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `7889a0580624c758aebcec002db57a9a67ff41a16f5a4748c637895b3854ab6c`

Touched paths:
- `/opt/colby/memory/projects/home_assistant_multi_site.md`
- `/opt/colby/memory/blockers/home_assistant_multi_site.md`
- `/opt/colby/memory/milestones/home_assistant_multi_site.md`
- `/opt/colby/memory/dependencies/home_assistant_multi_site.md`
- `/opt/colby/reports/cos/REMOTE_EXECUTION_CONTROL_PLAN.md`
- `/opt/colby/reports/cos/remote_execution_control_plan.json`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- ha_blocker_split: `PASS`
- physical_work_remains_gated: `PASS`
- remote_work_unblocked: `PASS`

Notes:
- Greg clarified Home Assistant is running and reachable remotely.
- Return to McKenzie is no longer a hard blocker for remote planning/read-only work.

### Finalize Right Turn historical-only closeout

- Event ID: `gaa_325ee7ff4fd1d769`
- Occurred: 2026-06-21T16:37:25-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/right_turn_historical_only_final_20260621_163720`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `de16b0e8ddf2d1dd8f6929e1bab91bc9285728c04a79ef0ce3203a7f624ac20e`

Touched paths:
- `/opt/colby/reports/cos/right_turn_historical_only_scan.json`
- `/opt/colby/reports/cos/RIGHT_TURN_HISTORICAL_ONLY_SCAN.md`
- `/opt/colby/reports/cos/housekeeping_closeouts.json`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- active_current_risk_count: `0`
- archive_aware_classification: `PASS`
- housekeeping_closeout_recorded: `PASS`

Notes:
- Right Turn remains historical-only.
- No files were deleted.

### Repair Right Turn housekeeping generator closeout handling

- Event ID: `gaa_b3d1a958f4c0a1b8`
- Occurred: 2026-06-21T16:38:33-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/right_turn_housekeeping_generator_repair_20260621_163833`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `71f0aaf9f3cd6d61ed076b6cb9fe2a2eb3ea342a16d2e2309135a2d72fb5b9ac`

Touched paths:
- `/opt/colby/services/cos/housekeeping_agenda.py`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`

Validations:
- right_turn_housekeeping_closed: `PASS`
- syntax: `PASS`

Notes:
- The prior closeout was recorded correctly, but the stale-context branch did not consult closeouts.

### Install remote access control inventory

- Event ID: `gaa_7b42792a5be60869`
- Occurred: 2026-06-21T16:42:20-05:00
- Decision: `approved`
- Action class: `local_write`
- Risk class: `WRITES_LOCAL`
- Status: `validated`
- Approved by: `Greg`
- Backup: `/opt/colby/backups/remote_access_control_inventory_20260621_164219`
- Memory updated: `True`
- Publish status: `pending`
- Current Truth semantic SHA256: `7db33aedee7a3ba43b3db98dce7303afb238eae723cd49f0e0ae5b61c05a5a89`

Touched paths:
- `/opt/colby/reports/cos/remote_access_control_inventory.json`
- `/opt/colby/reports/cos/REMOTE_ACCESS_CONTROL_INVENTORY.md`
- `/opt/colby/reports/cos/REMOTE_EXECUTION_CONTROL_PLAN.md`
- `/opt/colby/reports/cos/remote_execution_control_plan.json`
- `/opt/colby/state/cos/cos_status.json`
- `/opt/colby/reports/cos/COS_STATUS.md`
- `/opt/colby/memory/core/current_capabilities.md`
- `/opt/colby/memory/core/infrastructure_inventory.md`
- `/opt/colby/memory/operational/code_capability_registry_active.md`

Validations:
- read_only_probe: `PASS`
- summary: `{'blocked_or_not_ready_count': 3, 'partial_count': 0, 'preferred_pattern': 'single-command scripts through Tailscale SSH/API; no Telnet unless forced by legacy device', 'ready_count': 5, 'surface_count': 8}`

Notes:
- Inventory used read-only SSH/TCP/HTTP probes.
- Telnet is not recommended unless a specific legacy exception is approved.

## Governed Action Dashboard

Source: `/opt/colby/reports/cos/GOVERNED_ACTION_DASHBOARD.md`

# Governed Action Dashboard

Generated: 2026-06-21T16:42:20-05:00

## Overview

- Audit events: 59
- Approved actions: 43
- Approval-required decisions: 16
- Denied or blocked actions: 17
- Approval-surface items: 27
- Current items needing Greg: 20

## Current Controls

- preflight_policy_installed: active
- preflight_enforcement_installed: active
- audit_log_installed: active
- fresh_context_correction_installed: active
- approval_surface_review_installed: active

## Approval Surface

- Contracts: {'block_execution': 6, 'future_approval_required': 4, 'governed_action_required': 8, 'read_only_preflight': 9}
- Risk classes: {'EXTERNAL_CONTROL': 17, 'WRITES_SYSTEM': 10}
- Status values: {'active': 17, 'historical': 6, 'planned': 4}

## Recent Denied Or Blocked Actions

- 2026-06-21T16:11:03-05:00 | Repair Current Truth publisher PI4 route | approval_required / approved_completed | local_write / WRITES_LOCAL | paths: /opt/colby/services/export/publish_current_truth.sh, /opt/colby/memory/core/current_capabilities.md, /opt/colby/memory/operational/code_capability_registry_active.md, /opt/colby/memory/core/infrastructure_inventory.md, +2 more
- 2026-06-21T15:51:35-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json
- 2026-06-21T15:34:27-05:00 | Enable PI500 Tailscale subnet route acceptance | approved / blocked | system_write / WRITES_SYSTEM | paths: /opt/colby/reports/cos/pi500_tailscale_subnet_route_acceptance.md, /opt/colby/reports/cos/pi500_tailscale_subnet_route_acceptance.json, /opt/colby/memory/core/current_capabilities.md, /opt/colby/memory/core/infrastructure_inventory.md
- 2026-06-21T14:51:31-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json
- 2026-06-21T13:51:18-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json
- 2026-06-21T12:51:14-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json
- 2026-06-21T11:51:08-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json
- 2026-06-21T10:51:04-05:00 | Current Truth publish blocked without approval | approval_required / denied | publish / EXTERNAL_CONTROL | paths: /opt/colby/export/COLBY_PROJECT_CURRENT_TRUTH.md, /opt/colby/export/knowledge_transfer.json

## Recent Approved Actions

- 2026-06-21T16:42:20-05:00 | Install remote access control inventory | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/reports/cos/remote_access_control_inventory.json, /opt/colby/reports/cos/REMOTE_ACCESS_CONTROL_INVENTORY.md, /opt/colby/reports/cos/REMOTE_EXECUTION_CONTROL_PLAN.md, /opt/colby/reports/cos/remote_execution_control_plan.json, +5 more
- 2026-06-21T16:38:33-05:00 | Repair Right Turn housekeeping generator closeout handling | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/services/cos/housekeeping_agenda.py, /opt/colby/state/cos/cos_status.json, /opt/colby/reports/cos/COS_STATUS.md
- 2026-06-21T16:37:25-05:00 | Finalize Right Turn historical-only closeout | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/reports/cos/right_turn_historical_only_scan.json, /opt/colby/reports/cos/RIGHT_TURN_HISTORICAL_ONLY_SCAN.md, /opt/colby/reports/cos/housekeeping_closeouts.json, /opt/colby/memory/core/current_capabilities.md, +3 more
- 2026-06-21T16:27:37-05:00 | Unblock Home Assistant remote work and define remote control plan | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/memory/projects/home_assistant_multi_site.md, /opt/colby/memory/blockers/home_assistant_multi_site.md, /opt/colby/memory/milestones/home_assistant_multi_site.md, /opt/colby/memory/dependencies/home_assistant_multi_site.md, +4 more
- 2026-06-21T16:23:02-05:00 | Install debug-only route context trace | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/services/context/relationship_context_loader.py, /opt/colby/reports/cos/route_context_trace_report.json, /opt/colby/reports/cos/route_context_trace_report.md, /opt/colby/memory/core/current_capabilities.md, +3 more
- 2026-06-21T16:20:44-05:00 | Triage and restrict /home/cothrang/server.key | approved / validated | local_write / WRITES_LOCAL | paths: /home/cothrang/server.key, /opt/colby/reports/security/server_key_triage.json, /opt/colby/reports/security/SERVER_KEY_TRIAGE.md, /opt/colby/memory/core/infrastructure_inventory.md, +3 more
- 2026-06-21T16:13:03-05:00 | Close out travel-safe Current Truth publishing route | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/reports/cos/housekeeping_closeouts.json, /opt/colby/memory/core/infrastructure_inventory.md, /opt/colby/memory/core/current_capabilities.md, /opt/colby/memory/operational/code_capability_registry_active.md, +2 more
- 2026-06-21T16:07:15-05:00 | Install Current Truth Health generated service | approved / validated | local_write / WRITES_LOCAL | paths: /opt/colby/services/cos/current_truth_health.py, /opt/colby/reports/cos/current_truth_health.md, /opt/colby/reports/cos/current_truth_health.json, /opt/colby/memory/core/current_capabilities.md, +1 more

## Needs Greg

- Repair Current Truth publisher PI4 route | WRITES_LOCAL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Enable PI500 Tailscale subnet route acceptance | WRITES_SYSTEM | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- Current Truth publish blocked without approval | EXTERNAL_CONTROL | recent_denied_action | Recent governed action was blocked before execution and needs explicit approval to proceed.
- colby_proxy.py | EXTERNAL_CONTROL | approval_surface_review | Capability is in the approval-required surface and must not execute without Greg approval.
- memory_promoter.py | EXTERNAL_CONTROL | approval_surface_review | Capability is in the approval-required surface and must not execute without Greg approval.

## Next Actions

- Use the dashboard as the first source for blocked, denied, approved, or approval-needed governed actions.
- Keep Current Truth local until Greg explicitly approves publication.
- Wire dashboard-backed answers into any UI/admin view after the source report is stable.

## Sources

- audit_log: /opt/colby/state/cos/governed_action_audit_log.jsonl
- cos_status: /opt/colby/state/cos/cos_status.json
- approval_review: /opt/colby/reports/cos/approval_required_capability_review.json

## Housekeeping Agenda

Source: `/opt/colby/reports/cos/HOUSEKEEPING_AGENDA.md`

# Housekeeping Agenda

Generated: 2026-06-21T16:42:20-05:00

## Conversation Policy

- Offer: I have housekeeping items queued. Want to handle them now?
- If Greg says yes: Walk agenda_items in descending priority. For each item, give context, why it matters, recommendation, and the available decision options. Stop when Greg pauses or redirects.
- If Greg says no: Acknowledge and defer without losing the queue.

Offer when:
- At natural pauses after answering the user's primary question.
- When Greg asks what is next, what is pending, what is blocked, or what needs approval.
- After a task changes Colby's reasoning, capabilities, governance, memory, Current Truth, or project state.

Do not offer when:
- Do not interrupt urgent troubleshooting.
- Do not repeatedly ask in the same conversation after Greg declines.
- Do not treat the agenda as higher authority than Greg's current message.

## Summary

- Agenda items: 1
- Approval-required items: 0
- Top priority: Advance Cognitive Operating System build
- Dashboard needs-Greg count: 20
- Dashboard denied/blocked count: 17

## Agenda Items

### 1. Advance Cognitive Operating System build

- Priority: 50
- Category: strategic_priority
- Approval required: False
- Risk class: none
- Context: Current priority 3 is building Colby into a cognitive operating system.
- Recommendation: Use housekeeping to keep governance, memory, and context clean before adding larger automation.
- Options: continue_control_plane, build_ui, expand_memory_governance
- Source: /opt/colby/memory/core/current_priorities.md

## Sources

- governed_action_dashboard: /opt/colby/state/cos/governed_action_dashboard.json
- cos_status: /opt/colby/state/cos/cos_status.json
- critical_path: /opt/colby/reports/projects/current_critical_path.md
- current_priorities: /opt/colby/memory/core/current_priorities.md
- greg_corrections: /opt/colby/memory/users/greg/corrections.md
- memory_promotion_review: /opt/colby/reports/cos/memory_promotion_proposal_review.json
- housekeeping_closeouts: /opt/colby/reports/cos/housekeeping_closeouts.json

## Approval Required Capability Review

Source: `/opt/colby/reports/cos/approval_required_capability_review.md`

# Approval-Required Capability Review

Generated: 2026-06-21T06:01:20-05:00
Source registry: `/opt/colby/state/cos/cos_capability_registry_v2.json`

## Summary

- Approval surface entries: 27
- Risk counts: {'EXTERNAL_CONTROL': 17, 'WRITES_SYSTEM': 10}
- Status counts: {'active': 17, 'historical': 6, 'planned': 4}
- Required contract counts: {'governed_action_required': 8, 'read_only_preflight': 9, 'block_execution': 6, 'future_approval_required': 4}

## Operating Decision

- Active read-only checks remain usable only as evidence collection.
- Memory promotion, Current Truth publishing, prompt edits, proxy-mediated external actions, and any system-modifying path require explicit Greg approval plus backup and validation.
- Historical proxy files are preserved as evidence/backups only and must not be routed or executed.
- Planned external capabilities remain disabled until separately scoped and approved.

## Entries

### colby_proxy.py

- ID: `code_services_proxy_colby_proxy_py`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Keep active as reasoning interface/proxy; route external actions through approval checks and logged evidence packets.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy.py`
- Output/write indicators: requests\.post (3), inverter (1), systemctl (1), docker  (1), restart (1), \.write_text\( (1), open\(.*['\"]w (1), yaml\.dump (1)
- External services: requests\. (3), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy.py && echo present`

### fleet_discovery_snapshot.sh

- ID: `code_services_discovery_fleet_discovery_snapshot_sh`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit discovery snapshot reads only. Do not change remote hosts or network configuration.
- Entrypoints: `/opt/colby/services/discovery/fleet_discovery_snapshot.sh`
- Output/write indicators: ssh  (3), systemctl (4)
- External services: ssh  (3), mqtt (2)
- Secret boundaries: TOKEN (1), token (1), SECRET (1), secret (1)
- Safe validation: `test -e /opt/colby/services/discovery/fleet_discovery_snapshot.sh && echo present`

### ha_snapshot_summary.py

- ID: `code_tools_ha_snapshot_summary_py`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/2: Home Assistant Evidence Summarization
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit Home Assistant summary reads only. Do not control devices, write HA state, or modify HA configuration.
- Entrypoints: `/opt/colby/tools/ha_snapshot_summary.py`
- Output/write indicators: ha service (1)
- Safe validation: `test -e /opt/colby/tools/ha_snapshot_summary.py && echo present`

### memory_promoter.py

- ID: `code_services_memory_router_memory_promoter_py`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 3: Memory and Promotion Governance
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Require governed action contract, backup, validation, and explicit Greg approval before promoting operational memory.
- Entrypoints: `/opt/colby/services/memory_router/memory_promoter.py`
- Output/write indicators: homeassistant (1), \.write_text\( (1), mkdir (1)
- Safe validation: `test -e /opt/colby/services/memory_router/memory_promoter.py && echo present`

### publish_current_truth.sh

- ID: `code_services_export_publish_current_truth_sh`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 2: State Normalization / Export
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Require explicit publish approval, semantic-hash validation, and no blind execution from ChatGPT/Codex.
- Entrypoints: `/opt/colby/services/export/publish_current_truth.sh`
- Output/write indicators: git push (1), scp  (2), ssh  (7), mkdir (1), tee  (1)
- External services: ssh  (7), scp  (2)
- Secret boundaries: PASSWORD (1), password (1)
- Safe validation: `test -e /opt/colby/services/export/publish_current_truth.sh && echo present`

### relationship_context_loader.py

- ID: `code_services_context_relationship_context_loader_py`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 4: Retrieval and Context Assembly
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Keep active for context assembly. External or sensitive-source reads must remain bounded by source policy.
- Entrypoints: `/opt/colby/services/context/relationship_context_loader.py`
- Output/write indicators: inverter (1)
- Safe validation: `test -e /opt/colby/services/context/relationship_context_loader.py && echo present`

### solar_analyst.py

- ID: `code_tools_solar_analyst_py`
- Status: `active`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/2: Evidence Collection / State Normalization
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Keep active for analysis. Live bridge/API data is source of truth; external calls are read-only unless separately approved.
- Entrypoints: `/opt/colby/tools/solar_analyst.py`
- Output/write indicators: inverter (3)
- External services: http:// (1), mqtt (1)
- Safe validation: `test -e /opt/colby/tools/solar_analyst.py && echo present`

### colby_proxy_bad_v07_20260530_075220.py

- ID: `code_services_proxy_colby_proxy_bad_v07_20260530_075220_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_bad_v07_20260530_075220.py`
- Output/write indicators: requests\.post (1), \.write_text\( (1), open\(.*['\"]w (1), json\.dump (1), yaml\.dump (1), mkdir (2)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (2)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_bad_v07_20260530_075220.py && echo present`

### colby_proxy_pre_profile_learning_20260530_083553.py

- ID: `code_services_proxy_colby_proxy_pre_profile_learning_20260530_083553_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_pre_profile_learning_20260530_083553.py`
- Output/write indicators: requests\.post (1), \.write_text\( (1), open\(.*['\"]w (1), yaml\.dump (1), mkdir (2)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_pre_profile_learning_20260530_083553.py && echo present`

### colby_proxy_pre_request_logging_20260529_154147.py

- ID: `code_services_proxy_colby_proxy_pre_request_logging_20260529_154147_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_pre_request_logging_20260529_154147.py`
- Output/write indicators: requests\.post (1), open\(.*['\"]w (1), yaml\.dump (1), mkdir (1)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_pre_request_logging_20260529_154147.py && echo present`

### colby_proxy_pre_request_logging_20260529_154302.py

- ID: `code_services_proxy_colby_proxy_pre_request_logging_20260529_154302_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_pre_request_logging_20260529_154302.py`
- Output/write indicators: requests\.post (1), open\(.*['\"]w (1), yaml\.dump (1), mkdir (1)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_pre_request_logging_20260529_154302.py && echo present`

### colby_proxy_v0.4_backup_20260529_152911.py

- ID: `code_services_proxy_colby_proxy_v0_4_backup_20260529_152911_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_v0.4_backup_20260529_152911.py`
- Output/write indicators: requests\.post (1), open\(.*['\"]w (1), yaml\.dump (1), mkdir (1)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_v0.4_backup_20260529_152911.py && echo present`

### colby_proxy_v0.5_backup_20260529_153905.py

- ID: `code_services_proxy_colby_proxy_v0_5_backup_20260529_153905_py`
- Status: `historical`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 5: Reasoning Interface / Proxy
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `block_execution`
- Disposition: Historical-only. Preserve as evidence/backups; do not route, execute, or treat as active capability.
- Entrypoints: `/opt/colby/services/proxy/colby_proxy_v0.5_backup_20260529_153905.py`
- Output/write indicators: requests\.post (1), open\(.*['\"]w (1), yaml\.dump (1), mkdir (1)
- External services: requests\. (1), http:// (1)
- Secret boundaries: TOKEN (3), token (3), Authorization (1)
- Safe validation: `test -e /opt/colby/services/proxy/colby_proxy_v0.5_backup_20260529_153905.py && echo present`

### Multi-Site Connectivity

- ID: `milestone_multi_site_connectivity`
- Status: `planned`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/6: External Integration / Control-Sensitive Capability
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `future_approval_required`
- Disposition: Keep planned/disabled. Do not implement, route, or execute until separately scoped and approved.
- Entrypoints: `/opt/colby/reports/capabilities/current_capability_status.md`, `/opt/colby/memory/milestones/home_assistant_multi_site.md`
- Safe validation: `grep -n '### Multi-Site Connectivity' /opt/colby/reports/capabilities/current_capability_status.md`

### Production Deployment

- ID: `milestone_production_deployment`
- Status: `planned`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/6: External Integration / Control-Sensitive Capability
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `future_approval_required`
- Disposition: Keep planned/disabled. Do not implement, route, or execute until separately scoped and approved.
- Entrypoints: `/opt/colby/reports/capabilities/current_capability_status.md`, `/opt/colby/memory/milestones/home_assistant_multi_site.md`
- Safe validation: `grep -n '### Production Deployment' /opt/colby/reports/capabilities/current_capability_status.md`

### Solar Assistant Integration

- ID: `milestone_solar_assistant_integration`
- Status: `planned`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/6: External Integration / Control-Sensitive Capability
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `future_approval_required`
- Disposition: Keep planned/disabled. Do not implement, route, or execute until separately scoped and approved.
- Entrypoints: `/opt/colby/reports/capabilities/current_capability_status.md`, `/opt/colby/memory/milestones/home_assistant_multi_site.md`
- Safe validation: `grep -n '### Solar Assistant Integration' /opt/colby/reports/capabilities/current_capability_status.md`

### Voice Layer

- ID: `milestone_voice_layer`
- Status: `planned`
- Risk: `EXTERNAL_CONTROL`
- Layer: Layer 1/6: External Integration / Control-Sensitive Capability
- Approval reason: external-control classified, approval_required=true
- Recommended enabled: `no`
- Required contract: `future_approval_required`
- Disposition: Keep planned/disabled. Do not implement, route, or execute until separately scoped and approved.
- Entrypoints: `/opt/colby/reports/capabilities/current_capability_status.md`, `/opt/colby/memory/milestones/home_assistant_multi_site.md`
- Safe validation: `grep -n '### Voice Layer' /opt/colby/reports/capabilities/current_capability_status.md`

### check_docker.sh

- ID: `code_services_reality_tools_check_docker_sh`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit read-only service/container inspection only. Do not restart, stop, prune, pull, or modify containers.
- Entrypoints: `/opt/colby/services/reality/tools/check_docker.sh`
- Output/write indicators: systemctl (1), docker  (2)
- Safe validation: `test -e /opt/colby/services/reality/tools/check_docker.sh && echo present`

### check_ollama.sh

- ID: `code_services_reality_tools_check_ollama_sh`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit read-only Ollama availability/model inspection only. Do not start, restart, pull, or remove models.
- Entrypoints: `/opt/colby/services/reality/tools/check_ollama.sh`
- Output/write indicators: systemctl (1)
- Safe validation: `test -e /opt/colby/services/reality/tools/check_ollama.sh && echo present`

### check_openwebui.sh

- ID: `code_services_reality_tools_check_openwebui_sh`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit read-only OpenWebUI service inspection only. Do not restart services or change containers.
- Entrypoints: `/opt/colby/services/reality/tools/check_openwebui.sh`
- Output/write indicators: docker  (1)
- External services: curl  (1), http:// (1)
- Safe validation: `test -e /opt/colby/services/reality/tools/check_openwebui.sh && echo present`

### code_capability_scanner.py

- ID: `code_services_architecture_code_capability_scanner_py`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 2/3: Architecture Registry
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit local scanner/report generation only. Treat keyword-based write/system detections as conservative until reviewed.
- Entrypoints: `/opt/colby/services/architecture/code_capability_scanner.py`
- Output/write indicators: /api/services (1), git push (1), scp  (2), ssh  (2), homeassistant (1), ha service (1), relay (1), inverter (1)
- External services: curl  (2), ssh  (2), scp  (2), http:// (1), https:// (1), mqtt (1)
- Secret boundaries: TOKEN (3), token (3), SECRET (11), secret (11), PASSWORD (3), password (3), \.env (2), Authorization (1), Bearer (1)
- Safe validation: `test -e /opt/colby/services/architecture/code_capability_scanner.py && echo present`

### colby_openwebui_system_prompt.md

- ID: `code_prompts_openwebui_colby_openwebui_system_prompt_md`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 5: Reasoning Instructions
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: OpenWebUI prompt edits require backup, explicit approval, and post-change Current Truth regeneration.
- Entrypoints: `/opt/colby/prompts/openwebui/colby_openwebui_system_prompt.md`
- External services: mqtt (1)
- Safe validation: `test -e /opt/colby/prompts/openwebui/colby_openwebui_system_prompt.md && echo present`

### colby_system_prompt.md

- ID: `code_prompts_colby_system_prompt_md`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 5: Reasoning Instructions
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Prompt edits require backup, explicit approval, and post-change Current Truth regeneration.
- Entrypoints: `/opt/colby/prompts/colby_system_prompt.md`
- Safe validation: `test -e /opt/colby/prompts/colby_system_prompt.md && echo present`

### current_truth_export.py

- ID: `code_services_export_current_truth_export_py`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 2: State Normalization / Export
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit local Current Truth generation only. Publishing remains separate and approval-gated.
- Entrypoints: `/opt/colby/services/export/current_truth_export.py`
- Output/write indicators: systemctl (1), \.write_text\( (3), json\.dump (1), mkdir (1)
- External services: https:// (2)
- Secret boundaries: PASSWORD (1), password (1), \.env (1)
- Safe validation: `test -e /opt/colby/services/export/current_truth_export.py && echo present`

### reality_scan.sh

- ID: `code_services_reality_reality_scan_sh`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit evidence collection only. Any repair/remediation branch requires separate approval.
- Entrypoints: `/opt/colby/services/reality/reality_scan.sh`
- Output/write indicators: systemctl (1), docker  (1)
- Safe validation: `test -e /opt/colby/services/reality/reality_scan.sh && echo present`

### system_inventory.sh

- ID: `code_services_inventory_system_inventory_sh`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 1/2: Evidence Collection and Reality Checks
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `read_only_preflight`
- Disposition: Permit inventory collection only. Do not change packages, services, users, permissions, or containers.
- Entrypoints: `/opt/colby/services/inventory/system_inventory.sh`
- Output/write indicators: docker  (2)
- Safe validation: `test -e /opt/colby/services/inventory/system_inventory.sh && echo present`

### update_memories.py

- ID: `code_services_memory_update_update_memories_py`
- Status: `active`
- Risk: `WRITES_SYSTEM`
- Layer: Layer 3: Memory and Promotion Governance
- Approval reason: system-write classified, approval_required=true
- Recommended enabled: `yes`
- Required contract: `governed_action_required`
- Disposition: Require governed action contract, backup, validation, and explicit Greg approval before durable memory writes.
- Entrypoints: `/opt/colby/services/memory_update/update_memories.py`
- Output/write indicators: systemctl (2), \.write_text\( (1), open\(.*['\"]a (1), mkdir (2)
- External services: mqtt (3)
- Safe validation: `test -e /opt/colby/services/memory_update/update_memories.py && echo present`

## Next Governed Build

Implement a governed action preflight that can classify a requested action as read-only, local-write, system-write, external-control, publish, or memory-promotion before execution. The first enforcement targets should be memory writes, Current Truth publish, proxy external actions, prompt edits, and system-control scripts.

## OpenWebUI Persona Integration Plan

Source: `/opt/colby/reports/cos/OPENWEBUI_PERSONA_INTEGRATION_PLAN.md`

# OpenWebUI Persona Integration Plan

Generated: 2026-06-21T07:05:14-05:00

## Status

- Project: Open WebUI Persona Integration
- Status: planned_controlled_implementation
- Next action: Build Phase 1 read-only persona route audit.

## Personas

### colby-greg

- User: greg
- Authority: Owner
- Memory scope: Full private + shared + approved workspace
- Default workspace: cognitive_workstead
- Allowed workspaces: cognitive_workstead, dj_lego_store
- Notes: Owner authority does not bypass governed action preflight for risky actions.

### colby-mel

- User: mel
- Authority: Partner
- Memory scope: Assigned private + shared relationship + approved workspace
- Default workspace: cognitive_workstead
- Allowed workspaces: cognitive_workstead, terracon_accessibility
- Notes: No access to Greg-private memory unless promoted to shared relationship/context sources.

### colby-dj

- User: dj
- Authority: User
- Memory scope: Assigned user memory + approved workspace
- Default workspace: dj_lego_store
- Allowed workspaces: dj_lego_store
- Notes: Child/user scope; no system-control or private adult workspace access.

### colby-public

- User: webuser
- Authority: Restricted
- Memory scope: Public-safe only
- Default workspace: public_website
- Allowed workspaces: public_website
- Notes: No private user memory, no operational secrets, no system actions.

## Routing Contract

### source_of_model_identity

- O
- p
- e
- n
- W
- e
- b
- U
- I
-  
- s
- e
- l
- e
- c
- t
- e
- d
-  
- m
- o
- d
- e
- l
-  
- i
- d

### model_to_user_map

- colby: greg
- colby-greg: greg
- colby-mel: mel
- colby-dj: dj
- colby-public: webuser

### workspace_resolution

- Use explicit workspace switch when present.
- Otherwise use session current workspace.
- Otherwise use persona default workspace.
- Reject workspace access not authorized by relationships.yaml/persona policy.

### context_resolution

- Always include current operational context first.
- Load active user profile/preferences/corrections only for the resolved user.
- Load shared relationship context only for authorized private users.
- Load public-safe context only for colby-public/webuser.

### action_governance

- Normal chat/read-only routing is allowed.
- System writes, service control, publish, memory promotion, memory update apply, and external-control actions require governed approval.
- Denied governed actions are audit-logged and may later be closed as validation evidence or approved separately.

## Implementation Phases

### Phase 1: Read-only persona route audit

- Writes: False
- Goal: Generate repeatable matrix showing model id, resolved user, workspace, context files, and allowed/blocked status without printing private content.

Deliverables:
- `/opt/colby/services/personas/persona_route_audit.py`
- `/opt/colby/reports/personas/persona_route_audit.md`
- `/opt/colby/reports/personas/persona_route_audit.json`

Validation:
- Greg routes to greg context.
- Mel routes to mel context.
- DJ routes to dj context.
- Public routes only to public-safe context.
- Workspace mismatches are rejected.

### Phase 2: Persona memory isolation contract

- Writes: False
- Goal: Define and validate which memory paths each persona can read before any OpenWebUI behavior changes.

Deliverables:
- `/opt/colby/reports/personas/persona_memory_isolation_contract.md`
- `/opt/colby/reports/personas/persona_memory_isolation_contract.json`

Validation:
- Public cannot access private user memory.
- Mel and DJ cannot access Greg-private memory unless shared.
- Greg owner override is explicit and audited.

### Phase 3: Proxy route validation

- Writes: False
- Goal: Exercise the existing proxy models with safe prompts and verify persona-specific context behavior.

Deliverables:
- `/opt/colby/reports/personas/proxy_persona_route_validation.md`
- `/opt/colby/reports/personas/proxy_persona_route_validation.json`

Validation:
- No private content appears in public route.
- OpenWebUI model list remains colby, colby-greg, colby-mel, colby-dj, colby-public.
- Governed-action requests are denied without approval.

### Phase 4: OpenWebUI configuration review

- Writes: False
- Goal: Read-only review of OpenWebUI model/API config, current 401 behavior, and host/container proxy reachability before any service changes.

Deliverables:
- `/opt/colby/reports/openwebui_persona_config_review.md`
- `/opt/colby/reports/openwebui_persona_config_review.json`

Validation:
- Determine whether browser 401 is session/auth vs upstream model config.
- Determine whether container can reach Colby proxy.
- Produce exact governed change plan if config repair is needed.

### Phase 5: Controlled implementation

- Writes: True
- Goal: Only after phases 1-4 pass, apply any needed OpenWebUI/proxy changes with backups, approval, restart plan, rollback, and validation.

Deliverables:

Validation:
- Approval required: true

## Non-Goals

- No OpenWebUI restart in this plan.
- No Docker changes in this plan.
- No proxy behavior change in this plan.
- No private memory content printed in reports.
- No broad approval of governed actions.

## OpenWebUI Persona Routing Contract

Source: `/opt/colby/reports/cos/OPENWEBUI_PERSONA_ROUTING_CONTRACT.md`

# OpenWebUI Persona Routing Contract

Generated: 2026-06-21T07:05:14-05:00

## Model IDs

- colby-greg
- colby-mel
- colby-dj
- colby-public
- colby

## Read-Only Allowed

- model listing
- context route detection
- authorized memory/context retrieval
- answer generation
- housekeeping offer/readout

## Approval Required

- service control
- OpenWebUI config writes
- proxy code writes
- memory writes/apply/promote
- Current Truth publish
- external API control actions

## Current Persona Status

Source: `/opt/colby/reports/personas/current_persona_status.md`

# Current Persona Status

Generated:
2026-06-21T16:03:02-05:00

Registered Personas:
- Greg / colby-greg
- Mel / colby-mel
- DJ / colby-dj
- Public / colby-public

Persona Count:
4

Integration Status:
Operational for governed read-only persona model routing.

Completed Phases:
- Phase 1 read-only persona route audit passed.
- Phase 2 persona memory isolation contract passed.
- Phase 3 proxy route validation passed.
- Phase 4 OpenWebUI configuration review passed.
- Production Readiness Review passed.
- Project Closeout completed.

Current Phase:
Operational. Phase 5 controlled implementation is future-only if new requirements introduce an OpenWebUI/proxy change.

Governance:
Normal read-only chat routing is allowed. System control, memory writes, publishing, external-control actions, and OpenWebUI/proxy changes remain governed and approval-gated.

## Persona Route Audit

Source: `/opt/colby/reports/personas/persona_route_audit.md`

# Persona Route Audit

Generated: 2026-06-21T07:09:55-05:00
Status: PASS

Scope: read-only route audit. Private memory content was not printed.

## Summary

- model_checks: 5
- route_checks: 16
- public_checks: 2
- registry_checks: 4
- failure_count: 0
- private_content_printed: False

## Model Checks

- colby: expected greg, actual greg -> PASS
- colby-dj: expected dj, actual dj -> PASS
- colby-greg: expected greg, actual greg -> PASS
- colby-mel: expected mel, actual mel -> PASS
- colby-public: expected webuser, actual webuser -> PASS

## Workspace Route Matrix

- colby-greg / greg / cognitive_workstead: expected_allowed=True relationship_allows=True -> PASS
- colby-greg / greg / dj_lego_store: expected_allowed=True relationship_allows=True -> PASS
- colby-greg / greg / public_website: expected_allowed=False relationship_allows=False -> PASS
- colby-greg / greg / terracon_accessibility: expected_allowed=False relationship_allows=False -> PASS
- colby-mel / mel / cognitive_workstead: expected_allowed=True relationship_allows=True -> PASS
- colby-mel / mel / dj_lego_store: expected_allowed=False relationship_allows=False -> PASS
- colby-mel / mel / public_website: expected_allowed=False relationship_allows=False -> PASS
- colby-mel / mel / terracon_accessibility: expected_allowed=True relationship_allows=True -> PASS
- colby-dj / dj / cognitive_workstead: expected_allowed=False relationship_allows=False -> PASS
- colby-dj / dj / dj_lego_store: expected_allowed=True relationship_allows=True -> PASS
- colby-dj / dj / public_website: expected_allowed=False relationship_allows=False -> PASS
- colby-dj / dj / terracon_accessibility: expected_allowed=False relationship_allows=False -> PASS
- colby-public / webuser / cognitive_workstead: expected_allowed=False relationship_allows=False -> PASS
- colby-public / webuser / dj_lego_store: expected_allowed=False relationship_allows=False -> PASS
- colby-public / webuser / public_website: expected_allowed=True relationship_allows=True -> PASS
- colby-public / webuser / terracon_accessibility: expected_allowed=False relationship_allows=False -> PASS

## Public Boundary Checks

- webuser_workspace_scope: PASS
- webuser_memory_scope_public_safe: PASS

## Registry Checks

- greg / colby-greg: present=True status=Active -> PASS
- mel / colby-mel: present=True status=Active -> PASS
- dj / colby-dj: present=True status=Active -> PASS
- webuser / colby-public: present=True status=Active -> PASS

## Failures

- none

## Next Action

- Build Phase 2 persona memory isolation contract.

## Persona Memory Isolation Contract

Source: `/opt/colby/reports/personas/persona_memory_isolation_contract.md`

# Persona Memory Isolation Contract

Generated: 2026-06-21T07:13:02-05:00
Status: PASS

Scope: read-only memory isolation contract. Private memory content was not printed.

## Summary

- persona_count: 4
- validation_count: 6
- failure_count: 0
- private_content_printed: False

## Validations

- route_audit_passed: PASS - Phase 1 route audit must pass before memory isolation contract is valid.
- public_no_private_user_memory: PASS - Public route has only shared_public, users/webuser, and public_website memory prefixes.
- mel_cannot_read_greg_private_memory: PASS - Mel may use shared relationship context, not Greg-private memory.
- dj_cannot_read_greg_private_memory: PASS - DJ may use assigned user/workspace context, not Greg-private memory.
- greg_owner_override_explicit: PASS - Owner authority does not automatically bypass workspace scope in this contract.
- private_content_not_printed: PASS - Only prefix metadata and file counts are reported.

## Persona Contracts

### colby-greg / greg

- Authority: Owner
- Workspace scope: cognitive_workstead, dj_lego_store
- Owner override: none; Greg access is relationship-scoped unless explicitly listed
- Private content printed: False

Allowed prefixes:
- memory/collective | exists=True | files=0
- memory/core | exists=True | files=29
- memory/governance | exists=True | files=6
- memory/personas | exists=True | files=2
- memory/shared | exists=True | files=0
- memory/users/greg | exists=True | files=7
- memory/workspaces/cognitive_workstead | exists=True | files=6
- memory/workspaces/dj_lego_store | exists=True | files=6

Denied prefixes:
- memory/users/dj | exists=True | files=3
- memory/users/mel | exists=True | files=5
- memory/workspaces/terracon_accessibility | exists=True | files=6

### colby-mel / mel

- Authority: Partner
- Workspace scope: cognitive_workstead, terracon_accessibility
- Owner override: none; Greg access is relationship-scoped unless explicitly listed
- Private content printed: False

Allowed prefixes:
- memory/collective | exists=True | files=0
- memory/core | exists=True | files=29
- memory/governance | exists=True | files=6
- memory/personas | exists=True | files=2
- memory/shared | exists=True | files=0
- memory/users/mel | exists=True | files=5
- memory/workspaces/cognitive_workstead | exists=True | files=6
- memory/workspaces/terracon_accessibility | exists=True | files=6

Denied prefixes:
- memory/users/dj | exists=True | files=3
- memory/users/greg | exists=True | files=7
- memory/workspaces/dj_lego_store | exists=True | files=6

### colby-dj / dj

- Authority: User
- Workspace scope: dj_lego_store
- Owner override: none; Greg access is relationship-scoped unless explicitly listed
- Private content printed: False

Allowed prefixes:
- memory/collective | exists=True | files=0
- memory/core | exists=True | files=29
- memory/governance | exists=True | files=6
- memory/personas | exists=True | files=2
- memory/shared | exists=True | files=0
- memory/users/dj | exists=True | files=3
- memory/workspaces/dj_lego_store | exists=True | files=6

Denied prefixes:
- memory/users/greg | exists=True | files=7
- memory/users/mel | exists=True | files=5
- memory/workspaces/cognitive_workstead | exists=True | files=6
- memory/workspaces/terracon_accessibility | exists=True | files=6

### colby-public / webuser

- Authority: Restricted
- Workspace scope: public_website
- Owner override: none; Greg access is relationship-scoped unless explicitly listed
- Private content printed: False

Allowed prefixes:
- memory/shared_public | exists=False | files=0
- memory/users/webuser | exists=True | files=3
- memory/workspaces/public_website | exists=True | files=6

Denied prefixes:
- memory/operational | exists=True | files=6
- memory/projects | exists=True | files=11
- memory/relationships | exists=True | files=5
- memory/users/dj | exists=True | files=3
- memory/users/greg | exists=True | files=7
- memory/users/mel | exists=True | files=5
- memory/workspaces/cognitive_workstead | exists=True | files=6
- memory/workspaces/dj_lego_store | exists=True | files=6
- memory/workspaces/terracon_accessibility | exists=True | files=6

## Failures

- none

## Next Action

- Build Phase 3 proxy route validation.

## Proxy Persona Route Validation

Source: `/opt/colby/reports/personas/proxy_persona_route_validation.md`

# Proxy Persona Route Validation

Generated: 2026-06-21T15:16:04-05:00
Status: PASS

Scope: safe proxy route validation. Full private response content is not printed.

## Summary

- check_count: 4
- failure_count: 0
- model_count: 5
- private_content_printed: False

## Checks

### models_endpoint

- Result: PASS
- models: `['colby', 'colby-greg', 'colby-mel', 'colby-dj', 'colby-public']`
- missing: `[]`

### persona_status_routes

- Result: PASS
- `{'model': 'colby', 'expected_user': 'greg', 'pass': True, 'content_shape': {'has_user_section': True, 'has_workspace_section': True, 'has_learning_section': True, 'byte_count': 230}}`
- `{'model': 'colby-greg', 'expected_user': 'greg', 'pass': True, 'content_shape': {'has_user_section': True, 'has_workspace_section': True, 'has_learning_section': True, 'byte_count': 230}}`
- `{'model': 'colby-mel', 'expected_user': 'mel', 'pass': True, 'content_shape': {'has_user_section': True, 'has_workspace_section': True, 'has_learning_section': True, 'byte_count': 254}}`
- `{'model': 'colby-dj', 'expected_user': 'dj', 'pass': True, 'content_shape': {'has_user_section': True, 'has_workspace_section': True, 'has_learning_section': True, 'byte_count': 193}}`
- `{'model': 'colby-public', 'expected_user': 'webuser', 'pass': True, 'content_shape': {'has_user_section': True, 'has_workspace_section': True, 'has_learning_section': True, 'byte_count': 204}}`

### public_private_workspace_denial

- Result: PASS
- expected: `public route cannot switch to cognitive_workstead`
- response_shape: `{'has_access_denial': False, 'has_not_authorized': True, 'byte_count': 76}`

### validation_report_private_content

- Result: PASS
- Detail: Reports include route result shapes and byte counts only, not full proxy response content.

## Failures

- none

## Next Action

- Build Phase 4 OpenWebUI configuration review.

## Fleet Discovery Snapshot

Source: `/opt/colby/reports/discovery/current_infrastructure_discovery.md`

# COL-B Fleet Discovery Snapshot

Generated: 2026-06-05T14:00:33-05:00
Source Node: ASUSAI

Purpose:
Read-only categorized discovery snapshot for AsusAI, Pi4, and known workstation context. Used by Current Truth so future COL-B/ChatGPT sessions understand the active operating environment.

Guardrails:
- Read-only discovery only.
- No secrets, keys, tokens, or environment dumps.
- Do not treat unavailable nodes as failed systems.
- Use live bridge/API data as authority for McKenzie Solar operations.

## ASUSAI Local Identity

ASUSAI
Fri Jun  5 02:00:33 PM CDT 2026
cothrang
 14:00:33 up 3 days, 22:18,  5 users,  load average: 0.18, 0.14, 0.10

## ASUSAI Network

lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp5s0           DOWN           
wlx306893384ce4  UP             192.168.86.185/24 fde2:6a98:944e:813c:152:ecae:da87:d5c/64 fde2:6a98:944e:813c:4c49:f736:67a9:a76c/64 fde2:6a98:944e:813c:84:b81c:786f:5c2/64 fde2:6a98:944e:813c:17e8:d455:ad15:ff01/64 fde2:6a98:944e:813c:a893:b7e6:6f6:7d9a/64 fe80::8da7:a387:8929:d093/64 
br-2d1f7a001e04  UP             100.64.1.1/24 fe80::d062:cdff:fe3d:17/64 
tailscale0       UNKNOWN        100.65.243.112/32 fd7a:115c:a1e0::4501:f39a/128 fe80::ee41:4ac7:5031:56e6/64 
docker0          UP             172.18.0.1/16 fe80::4463:31ff:fefc:7c67/64 
veth49b0064@if2  UP             fe80::f47b:67ff:fe31:25b1/64 
veth9f4dd4a@if2  UP             fe80::9862:66ff:fef6:789a/64 
vethf2fddf3@if2  UP             fe80::2450:f9ff:fe81:1871/64 
vethead9125@if2  UP             fe80::b484:80ff:fef7:738/64 
veth7f82997@if2  UP             fe80::2cd2:7ff:fe6b:d462/64 
veth45c377d@if2  UP             fe80::24f2:55ff:fe04:8d5/64 

default via 192.168.86.1 dev wlx306893384ce4 proto dhcp src 192.168.86.185 metric 600 
100.64.1.0/24 dev br-2d1f7a001e04 proto kernel scope link src 100.64.1.1 
172.18.0.0/16 dev docker0 proto kernel scope link src 172.18.0.1 
192.168.86.0/24 dev wlx306893384ce4 proto kernel scope link src 192.168.86.185 metric 600 

## ASUSAI Disk

Filesystem      Size  Used Avail Use% Mounted on
tmpfs           3.2G  7.1M  3.2G   1% /run
/dev/nvme0n1p2  916G  386G  484G  45% /
tmpfs            16G     0   16G   0% /dev/shm
tmpfs           5.0M   12K  5.0M   1% /run/lock
efivarfs        192K  149K   39K  80% /sys/firmware/efi/efivars
/dev/nvme0n1p1  511M  6.2M  505M   2% /boot/efi
tmpfs           3.2G  120K  3.2G   1% /run/user/1000

## ASUSAI Colby Services

● colby-proxy.service - Colby OpenAI-Compatible Proxy
     Loaded: loaded (/etc/systemd/system/colby-proxy.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-06-05 13:52:07 CDT; 8min ago
   Main PID: 385737 (python)
      Tasks: 1 (limit: 38103)
     Memory: 34.9M (peak: 47.3M)
        CPU: 2.651s
     CGroup: /system.slice/colby-proxy.service
             └─385737 /opt/colby/venv/bin/python -m uvicorn colby_proxy:app --host 0.0.0.0 --port 5056 --app-dir /opt/colby/services/proxy

Jun 05 13:55:28 ASUSAI python[385737]: INFO:     172.18.0.4:45586 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:55:29 ASUSAI python[385737]: INFO:     172.18.0.4:45586 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:14 ASUSAI python[385737]: INFO:     172.18.0.4:49262 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:14 ASUSAI python[385737]: INFO:     172.18.0.4:49262 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:40 ASUSAI python[385737]: INFO:     172.18.0.4:56888 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:40 ASUSAI python[385737]: INFO:     172.18.0.4:56888 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:50 ASUSAI python[385737]: INFO:     172.18.0.4:60252 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:50 ASUSAI python[385737]: INFO:     172.18.0.4:60252 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:51 ASUSAI python[385737]: INFO:     172.18.0.4:60252 - "POST /v1/chat/completions HTTP/1.1" 200 OK
Jun 05 13:59:52 ASUSAI python[385737]: INFO:     172.18.0.4:60252 - "POST /v1/chat/completions HTTP/1.1" 200 OK

● colby-current-truth.timer - Run COL-B Current Truth Export and Publish hourly
     Loaded: loaded (/etc/systemd/system/colby-current-truth.timer; enabled; preset: enabled)
     Active: active (waiting) since Thu 2026-06-04 13:30:26 CDT; 24h ago
    Trigger: Fri 2026-06-05 14:07:56 CDT; 7min left
   Triggers: ● colby-current-truth.service

Jun 04 13:30:26 ASUSAI systemd[1]: Started colby-current-truth.timer - Run COL-B Current Truth Export and Publish hourly.

## ASUSAI Colby Processes

ollama      2180       1  0 Jun01 ?        00:01:01 /usr/local/bin/ollama serve
root       93283   93191  0 Jun02 ?        00:11:34 /usr/local/bin/python3.11 /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port 8000
root       93299   93207  0 Jun02 ?        00:15:47 /usr/local/bin/python3 -m uvicorn open_webui.main:app --host 0.0.0.0 --port 8080 --forwarded-allow-ips * --workers 1
root       93397   93255  0 Jun02 ?        00:11:34 /usr/local/bin/python3.11 /usr/local/bin/uvicorn app:app --host 0.0.0.0 --port 5055
root       93612   93370  0 Jun02 ?        00:11:36 /usr/local/bin/python3.11 /usr/local/bin/uvicorn app:app --host 0.0.0.0 --port 7077
root       93710   93375  0 Jun02 ?        00:11:33 /usr/local/bin/python3.11 /usr/local/bin/uvicorn backend.main:app --host 0.0.0.0 --port 8000
cothrang  383616       1  0 13:25 ?        00:00:05 /opt/colby/venv/bin/python -m uvicorn colby_proxy:app --host 127.0.0.1 --port 9999
ollama    385154    2180  3 13:42 ?        00:00:37 /usr/local/bin/ollama runner --model /usr/share/ollama/.ollama/models/blobs/sha256-2bada8a7450677000f678be90653b85d364de7db25eb5ea54136ada5f3933730 --port 45167
cothrang  385737       1  0 13:52 ?        00:00:01 /opt/colby/venv/bin/python -m uvicorn colby_proxy:app --host 0.0.0.0 --port 5056 --app-dir /opt/colby/services/proxy
cothrang  386341  386224  0 14:00 pts/2    00:00:00 bash /opt/colby/services/discovery/fleet_discovery_snapshot.sh

## ASUSAI Colby Key Paths

/opt/colby
/opt/colby/archive
/opt/colby/backups
/opt/colby/backups/after_action
/opt/colby/backups/after_action/20260531_091521
/opt/colby/backups/approved_learning
/opt/colby/backups/change_registry
/opt/colby/backups/change_registry/20260531_093150
/opt/colby/backups/change_registry/20260531_102116
/opt/colby/backups/change_registry/20260531_102605
/opt/colby/backups/change_registry/20260531_104719
/opt/colby/backups/change_registry/20260531_110051
/opt/colby/backups/change_registry/20260531_113254
/opt/colby/backups/change_registry/20260531_113507
/opt/colby/backups/change_registry/20260531_114029
/opt/colby/backups/change_registry/20260531_120136
/opt/colby/backups/change_registry/20260531_122053
/opt/colby/backups/change_registry/20260531_122846
/opt/colby/backups/change_registry/20260531_123849
/opt/colby/backups/change_registry/20260531_130456
/opt/colby/backups/change_registry/20260531_131808
/opt/colby/backups/change_registry/20260531_132953
/opt/colby/backups/change_registry/20260531_133947
/opt/colby/backups/change_registry/20260531_135101
/opt/colby/backups/change_registry/20260531_141138
/opt/colby/backups/change_registry/20260531_145942
/opt/colby/backups/change_registry/20260531_151952
/opt/colby/backups/change_registry/20260531_153641
/opt/colby/backups/change_registry/20260531_154107
/opt/colby/backups/change_registry/20260531_154649
/opt/colby/backups/change_registry/20260531_154852
/opt/colby/backups/change_registry/20260531_155056
/opt/colby/backups/change_registry/20260531_155251
/opt/colby/backups/change_registry/20260531_155406
/opt/colby/backups/change_registry/20260531_155438
/opt/colby/backups/change_registry/20260531_155543
/opt/colby/backups/change_registry/20260531_155625
/opt/colby/backups/change_registry/20260531_160151
/opt/colby/backups/change_registry/20260531_180041
/opt/colby/backups/change_registry/20260531_180212
/opt/colby/backups/change_registry/20260531_180447
/opt/colby/backups/change_registry/20260531_180559
/opt/colby/backups/change_registry/20260531_180825
/opt/colby/backups/change_registry/20260531_180920
/opt/colby/backups/change_registry/20260531_181658
/opt/colby/backups/change_registry/20260531_182001
/opt/colby/backups/change_registry/20260531_182107
/opt/colby/backups/change_registry/20260531_182355
/opt/colby/backups/change_registry/20260531_182535
/opt/colby/backups/change_registry/20260531_182720
/opt/colby/backups/change_registry/20260531_182809
/opt/colby/backups/change_registry/20260531_182917
/opt/colby/backups/change_registry/20260531_183040
/opt/colby/backups/change_registry/20260531_183135
/opt/colby/backups/change_registry/20260531_183330
/opt/colby/backups/change_registry/20260531_183515
/opt/colby/backups/change_registry/20260531_183608
/opt/colby/backups/change_registry/20260531_183727
/opt/colby/backups/change_registry/20260531_184327
/opt/colby/backups/change_registry/20260531_184444
/opt/colby/backups/change_registry/20260531_184603
/opt/colby/backups/change_registry/20260531_184719
/opt/colby/backups/change_registry/20260531_185006
/opt/colby/backups/change_registry/20260531_185220
/opt/colby/backups/change_registry/20260531_185343
/opt/colby/backups/change_registry/20260531_185500
/opt/colby/backups/change_registry/20260531_185651
/opt/colby/backups/change_registry/20260531_190601
/opt/colby/backups/change_registry/20260531_190832
/opt/colby/backups/change_registry/20260531_191020
/opt/colby/backups/change_registry/20260531_191724
/opt/colby/backups/change_registry/20260531_192154
/opt/colby/backups/change_registry/20260531_192409
/opt/colby/backups/change_registry/20260531_192615
/opt/colby/backups/change_registry/20260531_192721
/opt/colby/backups/chatgpt_imports
/opt/colby/backups/chatgpt_imports/20260530_090116
/opt/colby/backups/current_truth_architecture_block
/opt/colby/backups/current_truth_exporter
/opt/colby/backups/current_truth_publisher
/opt/colby/backups/current_truth_semantic_fix
/opt/colby/backups/current_truth_systemd
/opt/colby/backups/decision_roadmap
/opt/colby/backups/decision_roadmap/20260531_064217
/opt/colby/backups/learning_applied
/opt/colby/backups/manual
/opt/colby/backups/memory_updates
/opt/colby/backups/ollama
/opt/colby/backups/profile_candidates_scope_normalization_20260531_175902
/opt/colby/backups/project_updates
/opt/colby/backups/project_updates/20260531_102116
/opt/colby/backups/promotion_applier
/opt/colby/backups/promotion_applier/20260531_071511
/opt/colby/backups/services_authz
/opt/colby/backups/services_profile_learning
/opt/colby/backups/state_alignment
/opt/colby/backups/state_alignment/20260531_064905
/opt/colby/backups/update_memories_v1_20260605-120622
/opt/colby/config
/opt/colby/conversations
/opt/colby/conversations/exported
/opt/colby/conversations/rejected
/opt/colby/conversations/reviewed
/opt/colby/conversations/review_required
/opt/colby/conversations/validated_review
/opt/colby/evidence
/opt/colby/evidence/reality
/opt/colby/export
/opt/colby/imports
/opt/colby/imports/chatgpt_project
/opt/colby/imports/chatgpt_project/applied
/opt/colby/imports/chatgpt_project/logs
/opt/colby/imports/chatgpt_project/rejected
/opt/colby/imports/chatgpt_project/review_required
/opt/colby/imports/chatgpt_project/staged
/opt/colby/journal
/opt/colby/journal/daily
/opt/colby/journal/monthly
/opt/colby/journal/weekly
/opt/colby/knowledge
/opt/colby/knowledge/cognitive_workstead
/opt/colby/knowledge/greg_technical
/opt/colby/knowledge/mel_terracon_accessibility
/opt/colby/knowledge/procedures
/opt/colby/knowledge/rv
/opt/colby/knowledge/solar_energy
/opt/colby/knowledge/vehicles_equipment
/opt/colby/knowledge/web_projects
/opt/colby/learning
/opt/colby/learning/applied
/opt/colby/learning/approved
/opt/colby/learning/conversation_observations
/opt/colby/learning/conversation_observations/pending
/opt/colby/learning/conversation_observations/rejected
/opt/colby/learning/conversation_observations/reviewed
/opt/colby/learning/inbox
/opt/colby/learning/pending
/opt/colby/learning/profile_candidates
/opt/colby/learning/profile_candidates/applied
/opt/colby/learning/profile_candidates/pending
/opt/colby/learning/profile_candidates/quarantine_prompt_artifacts
/opt/colby/learning/profile_candidates/redirected_workspace_fact_20260531_192615
/opt/colby/learning/profile_candidates/rejected
/opt/colby/learning/profile_candidates/restricted
/opt/colby/learning/profile_candidates/review_required
/opt/colby/learning/rejected
/opt/colby/learning/review_required
/opt/colby/logs
/opt/colby/logs/current_truth
/opt/colby/logs/proxy
/opt/colby/memory
/opt/colby/memory/archive
/opt/colby/memory/blockers
/opt/colby/memory/collective
/opt/colby/memory/core
/opt/colby/memory/decisions
/opt/colby/memory/events
/opt/colby/memory/governance
/opt/colby/memory/hypotheses
/opt/colby/memory/hypotheses/rejected
/opt/colby/memory/lessons
/opt/colby/memory/milestones
/opt/colby/memory/observations
/opt/colby/memory/operational
/opt/colby/memory/personas
/opt/colby/memory/personas/mappings
/opt/colby/memory/projects
/opt/colby/memory/relationships
/opt/colby/memory/relationships/applied_or_duplicate
/opt/colby/memory/shared
/opt/colby/memory_updates
/opt/colby/memory_updates/applied
/opt/colby/memory_updates/approved
/opt/colby/memory_updates/pending
/opt/colby/memory_updates/rejected
/opt/colby/memory/users
/opt/colby/memory/users/dj
/opt/colby/memory/users/greg
/opt/colby/memory/users/mel
/opt/colby/memory/users/webuser
/opt/colby/memory/workspaces
/opt/colby/memory/workspaces/cognitive_workstead
/opt/colby/memory/workspaces/dj_lego_store
/opt/colby/memory/workspaces/public_website
/opt/colby/memory/workspaces/terracon_accessibility
/opt/colby/models
/opt/colby/policies
/opt/colby/promotions
/opt/colby/promotions/applied
/opt/colby/promotions/approved
/opt/colby/promotions/candidates
/opt/colby/promotions/logs
/opt/colby/promotions/rejected
/opt/colby/prompts
/opt/colby/prompts/openwebui
/opt/colby/reports
/opt/colby/reports/after_action
/opt/colby/reports/capabilities
/opt/colby/reports/changes
/opt/colby/reports/conversation_inventory

## ASUSAI Current Truth Export Files

total 100K
-rw-rw-r-- 1 cothrang cothrang 41K Jun  5 13:17 COLBY_PROJECT_CURRENT_TRUTH.md
-rw-rw-r-- 1 cothrang cothrang  65 Jun  5 13:17 current_truth.semantic.sha
-rw-rw-r-- 1 cothrang cothrang 45K Jun  5 13:17 knowledge_transfer.json
-rw-rw-r-- 1 cothrang cothrang  65 Jun  5 12:07 last_published.semantic.sha

## ASUSAI Recent Discovery/Executive/Investigation Reports

2026-05-31 14:34 /opt/colby/reports/memory_scope_discovery_20260531_153426.txt
2026-05-31 14:51 /opt/colby/reports/persona_authority_discovery_20260531_155139.txt
2026-05-31 15:00 /opt/colby/reports/learning_promotion_v2_discovery_20260531_160012.txt
2026-05-31 17:10 /opt/colby/reports/workspace_memory_discovery_20260531_181041.txt
2026-06-05 13:17 /opt/colby/reports/executive/current_day_summary.md
2026-06-05 13:17 /opt/colby/reports/investigations/investigation_20260605_131717_mckenzie_solar_daylight_0w_dashboard_event_forensic_investigation.md
2026-06-05 14:00 /opt/colby/reports/discovery/current_infrastructure_discovery.md.tmp

## PI4 Remote Snapshot 192.168.86.79

### Identity
pi4
Fri  5 Jun 14:00:33 CDT 2026
cothrang

### Network
lo               UNKNOWN        127.0.0.1/8 ::1/128 
eth0             UP             192.168.0.153/24 2600:1005:b18d:fa38:51d8:cecd:87ec:3298/64 fe80::d02c:9b24:fd05:5395/64 
wlan0            UP             192.168.86.79/24 fde2:6a98:944e:813c:70:1df7:9d4a:e609/64 fe80::a51f:8eb9:ba34:b2c/64 

### Uptime
 14:00:33 up 3 days, 22:25,  3 users,  load average: 0.92, 0.36, 0.26

### Disk
Filesystem      Size  Used Avail Use% Mounted on
udev            3.6G     0  3.6G   0% /dev
tmpfs           1.6G  151M  1.4G  10% /run
/dev/mmcblk0p2  235G   13G  210G   6% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M   16K  5.0M   1% /run/lock
/dev/mmcblk0p1  510M   67M  444M  13% /boot/firmware
tmpfs           783M     0  783M   0% /run/user/1000

### Key Services
  solar-api.service           loaded active running McKenzie Solar Read-Only API
  solar-collector.service     loaded active running Solar Assistant MQTT Collector

### Key Timers
Sat 2026-06-06 00:00:00 CDT 9h left        Fri 2026-06-05 11:34:53 CDT 2h 25min ago dpkg-db-backup.timer         dpkg-db-backup.service

### Key Processes
cothrang     699       1  1 Jun01 ?        01:02:02 /home/cothrang/solar-collector/venv/bin/python /home/cothrang/solar-collector/collect_solar.py
cothrang   13261       1  0 Jun03 ?        00:07:39 /home/cothrang/solar-collector/venv-api/bin/python3 /home/cothrang/solar-collector/venv-api/bin/uvicorn solar_api:app --host 0.0.0.0 --port 5057
cothrang   37165   37160  0 14:00 ?        00:00:00 /bin/sh -c /home/cothrang/solar-collector/update_dashboard.sh >> /home/cothrang/solar-collector/dashboard_update.log 2>&1
cothrang   37166   37165  0 14:00 ?        00:00:00 /bin/bash /home/cothrang/solar-collector/update_dashboard.sh
cothrang   37173   37166 99 14:00 ?        00:00:29 python normalize_solar.py

## PI4 Remote Snapshot hostname pi4 fallback

Host key verification failed.
REMOTE_UNAVAILABLE: cothrang@pi4

## GCSnapDragon Known Context

- Hostname: GCSnapDragon
- Known LAN IP: 192.168.86.110
- Role: Windows workstation / PowerShell control node used for SSH collection and upload workflows.
- Note: Detailed GCSnapDragon discovery requires local Windows-side collection or OpenSSH server access.

## Executive Daily Review

Source: `/opt/colby/reports/executive/current_day_summary.md`

# Executive Daily Review

Generated: 2026-06-21T16:42:22

Purpose:
Capture recent accomplishments, discoveries, risks, and next actions so Colby and external Current Truth consumers can reason from recent work instead of relying only on hard-coded reports.

## Recent Executive Signals

- Current Truth Health Report
- Status: `WARN`
- Local export pass: `True`
- Latest publish pass: `True`
- Markdown reachable: `True` status=`200`
- Knowledge transfer reachable: `True` status=`200`
- Timer active: `active`
- Findings
- Local Current Truth export files are present.
- Latest publish log reports pass: True.
- Treat status PASS as Current Truth delivery healthy.
- If semantic hashes diverge, rerun governed Current Truth publish.
- If Greg says yes: Walk agenda_items in descending priority. For each item, give context, why it matters, recommendation, and the available decision options. Stop when Greg pauses or redirects.
- When Greg asks what is next, what is pending, what is blocked, or what needs approval.
- After a task changes Colby's reasoning, capabilities, governance, memory, Current Truth, or project state.
- Approval-required items: 0
- Top priority: Advance Cognitive Operating System build
- Dashboard needs-Greg count: 20
- Dashboard denied/blocked count: 17
- Priority: 50
- Category: strategic_priority
- Approval required: False
- Risk class: none
- Context: Current priority 3 is building Colby into a cognitive operating system.
- Source: /opt/colby/memory/core/current_priorities.md
- governed_action_dashboard: /opt/colby/state/cos/governed_action_dashboard.json
- cos_status: /opt/colby/state/cos/cos_status.json
- critical_path: /opt/colby/reports/projects/current_critical_path.md
- current_priorities: /opt/colby/memory/core/current_priorities.md
- greg_corrections: /opt/colby/memory/users/greg/corrections.md

## Interpretation

- This report is a synthesized continuity layer, not a source of live system telemetry.
- Treat source project files, after-action records, and live bridge/API data as higher authority when conflicts exist.
- Use this report to answer what changed recently, what was learned, and what should happen next.

## Source Files Reviewed

- /opt/colby/reports/cos/current_truth_health.md
- /opt/colby/reports/cos/HOUSEKEEPING_AGENDA.md
- /opt/colby/reports/cos/GOVERNED_ACTION_DASHBOARD.md
- /opt/colby/reports/cos/GOVERNED_ACTION_AUDIT_LOG.md
- /opt/colby/reports/cos/COS_STATUS.md
- /opt/colby/reports/cos/REMOTE_EXECUTION_CONTROL_PLAN.md
- /opt/colby/reports/cos/REMOTE_ACCESS_CONTROL_INVENTORY.md
- /opt/colby/reports/cos/RIGHT_TURN_HISTORICAL_ONLY_SCAN.md
- /opt/colby/reports/cos/route_context_trace_report.md
- /opt/colby/reports/cos/pi500_route_blocker_closeout.md
- /opt/colby/reports/cos/pi4_direct_tailscale_access.md
- /opt/colby/reports/cos/pi500_tailscale_subnet_route_acceptance.md
- /opt/colby/reports/projects/current_project_impact.md
- /opt/colby/reports/projects/current_critical_path.md
- /opt/colby/reports/projects/current_dependency_status.md
- /opt/colby/reports/projects/current_project_status.md
- /opt/colby/reports/projects/current_milestone_status.md
- /opt/colby/reports/capabilities/current_capability_status.md
- /opt/colby/reports/executive/current_day_summary.md
- /opt/colby/reports/after_action/after_action_20260605_120734_mckenzie_solar_v1_stable.md
- /opt/colby/reports/after_action/after_action_20260605_120636_mckenzie_solar_v1_stable.md
- /opt/colby/reports/after_action/after_action_20260605_120622_mckenzie_solar_v1_stable.md
- /opt/colby/reports/after_action/after_action_20260531_091521.md
- /opt/colby/reports/investigations/manual_memory_migration.md
- /opt/colby/reports/investigations/investigation_20260605_131717_mckenzie_solar_daylight_0w_dashboard_event_forensic_investigation.md
- /opt/colby/memory/workspaces/cognitive_workstead/decisions.md
- /opt/colby/memory/workspaces/cognitive_workstead/milestones.md
- /opt/colby/memory/workspaces/cognitive_workstead/assumptions.md
- /opt/colby/memory/workspaces/cognitive_workstead/goals.md
- /opt/colby/memory/workspaces/cognitive_workstead/README.md
- /opt/colby/memory/projects/home_assistant_multi_site.md
- /opt/colby/memory/projects/openwebui_persona_integration.md
- /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- /opt/colby/memory/projects/conversation_intelligence.md
- /opt/colby/memory/projects/colby_cognitive_operating_system.md
- /opt/colby/memory/core/current_capabilities.md
- /opt/colby/memory/operational/code_capability_registry_active.md
- /opt/colby/memory/core/current_priorities.md
- /opt/colby/memory/core/next_actions.md
- /opt/colby/state/current_state.md

## Recent Investigations

Source: `/opt/colby/reports/investigations`

----- /opt/colby/reports/investigations/investigation_20260605_131717_mckenzie_solar_daylight_0w_dashboard_event_forensic_investigation.md -----
# Investigation Record

Timestamp: 2026-06-05T13:17:17
Actor: greg
Workspace: cognitive_workstead
Project: McKenzie Solar Data Bridge

Title: McKenzie Solar Daylight 0W Dashboard Event Forensic Investigation

Objective:
Investigate the temporary daylight 0W solar dashboard event and verify dashboard field lineage using live Pi4 evidence.

Evidence:
Verified field lineage from MQTT to mqtt_raw to solar_metrics_1min to energy_analysis to solarstatus_json.py to solarstatus.json to dashboard. Confirmed solarstatus_json.py uses production /home/cothrang/solar-collector/solar.db. Measured normalize_solar.py runtime around 31 seconds. Verified no execution locking. Captured direct evidence of two normalize_solar.py processes running simultaneously at the 12:45 boundary.

Finding:
Concurrent normalize_solar.py execution is real. One instance runs from cron and another runs inside update_dashboard.sh at the same 15-minute dashboard boundary. No lock or serialization prevents overlap.

Conclusion:
Concurrent normalization is the leading root-cause candidate for the transient daylight solar_w=0 and mode=null dashboard snapshot. MQTT, raw data, normalized data, analysis view, and wrong-database hypotheses were cleared.

Confidence:
High, approximately 95 percent.

Next Action:
Perform hardening review, design locking/serialization, and add validator guardrail for daylight + charging battery + solar_w=0.

Status:
recorded

----- /opt/colby/reports/investigations/manual_memory_migration.md -----
## Manual Memory Migration Entry

- Timestamp: 2026-06-16 16:25:56 CDT
- Source: remember command

```text
Memory migration chunk 2 — move legacy AI server / Open WebUI setup history to COLBY Current Truth, not ChatGPT memory.

Preserve these historical details in COLBY Current Truth or project records:
- Open WebUI setup and reset history.
- Ollama exposure/configuration history.
- ai.gregcothran.com setup and routing notes.
- Speedify endpoint planning.
- Cloudflare and NGINX dashboard planning.
- O365 SSO preference notes.
- Historical model preload/model selection notes.
- RTX 4090 planning history.
- ASUSAI reload planning history.
- Self-healing pipeline design history.
- React + FastAPI dashboard planning.
- External-drive full-system snapshot planning.

Classification:
- Preserve in COLBY Current Truth.
- Remove from ChatGPT memory after verification.
- Treat only current confirmed ASUSAI facts as live operational truth.
- Current confirmed ASUSAI fact: ASUSAI uses RTX 3090 and now has working COLBY CLI/OpenAI API access.
```

## Manual Memory Migration Entry

- Timestamp: 2026-06-16 16:27:35 CDT
- Source: remember command

```text
Memory migration chunk 3 — move historical Raspberry Pi / cluster infrastructure details to COLBY Current Truth, not ChatGPT memory.

Preserve these historical details in COLBY Current Truth or project records:
- Raspberry Pi cluster inventories, node names, node IPs, and historical roles.
- Jetson Orin Nano and Jetson Nano setup history.
- k3s, Rancher, Kubernetes, Slurm, and Raspberry Pi standardization history.
- Drobo/NAS log storage paths and historical backup planning.
- Historical OneDrive log storage ideas.
- Historical VPN planning for vpn.gregcothran.com.
- Old cluster-wide log collection plans.
- Legacy node snapshot procedures.
- Retired or superseded network devices and cluster hardware.

Classification:
- Preserve in COLBY Current Truth.
- Remove from ChatGPT memory after verification.
- Treat this as historical lab infrastructure unless current evidence confirms it is part of active McKenzie operations.
```

## Manual Memory Migration Entry

- Timestamp: 2026-06-16 16:28:15 CDT
- Source: remember command

```text
Memory migration chunk 4 — move completed Home Assistant troubleshooting artifacts to COLBY Current Truth, not ChatGPT memory.

Preserve these historical details in COLBY Current Truth or project records:
- Home Assistant MQTT setup troubleshooting history.
- Solar Assistant to Home Assistant MQTT bridge setup history.
- Mosquitto bridge configuration history.
- HA UI terminology corrections, including Apps instead of Add-ons.
- Home Assistant MQTT reconfigure screen behavior and reset issue.
- Home Assistant local voice setup history.
- Whisper, Piper, and openWakeWord local voice architecture notes.
- HA Assist exposed-entity cleanup history.
- Battery SOC notification setup history.
- Sonos integration setup history.
- Home Assistant Voice Preview Edition setup notes.

Classification:
- Preserve in COLBY Current Truth.
- Remove from ChatGPT memory after verification.
- Keep only the current confirmed Home Assistant architecture in ChatGPT memory.
- Current confirmed architecture: SolarAssistant MQTT bridges into HA Mosquitto; HA MQTT integration remains pointed at core-mosquitto; local voice uses Whisper, Piper, openWakeWord, and HA conversation agent.
```

## Manual Memory Migration Entry

- Timestamp: 2026-06-16 16:39:59 CDT
- Source: remember command

```text
ChatGPT Memory Full Archive Export — 2026-06-16

Purpose:
Preserve useful ChatGPT memory content inside COLBY Current Truth before clearing ChatGPT memory.

Disposition:
- Preserve this archive in COLBY.
- After verification, Greg may delete all ChatGPT saved memories.
- Rebuild ChatGPT memory afterward using only a curated core set.
- Treat archived operational details as historical unless Current Truth or live evidence confirms they are current.

Major categories archived:
- Greg identity, preferences, writing style, command style, and decision preferences.
- Cognitive Workstead mission, Greg/Mel roles, outreach history, grant positioning, and public messaging rules.
- COL-B / Colby / ASUSAI / COS architecture, governance rules, audit requirements, rollback requirements, and Current Truth workflow.
- ASUSAI AI server history, Open WebUI, Ollama, Grafana, Node Exporter, Speedify, Cloudflare, NGINX, dashboard, backup, and self-healing pipeline plans.
- Current confirmed ASUSAI fact: ASUSAI uses RTX 3090 and has working COLBY CLI/OpenAI API access.
- PI4 / McKenzie Solar collector and GitHub Pages publishing role.
- McKenzie Solar architecture, SolarAssistant, EG4 18kPV, MPPT mapping, Central Time rules, and live-data authority rules.
- Home Assistant architecture, SolarAssistant MQTT bridge, Mosquitto, local voice stack, HA terminology corrections, and known UI workflow notes.
- Refoss EM16 Pro mapping, validation history, CT channel notes, and panel mapping notes.
- RiVi/RV solar, Victron, battery bank, dashboard, and Total AC derivation notes.
- Historical Raspberry Pi, Jetson, k3s, Rancher, Slurm, Drobo, NAS, VPN, logging, and standardization details.
- Recipes and family recipe collection references.
- USAFR profile, rank, duty title, Maxwell/Gunter assignment, and military writing defaults.
- Professional writing, resumes, IAM ebook, cover letters, and outreach preferences.
- Future project concepts including Autonomous MSP Operations, AI log anomaly detection, electrical system design, and vapor fuel concept.

Governance:
- ChatGPT memory should only retain durable strategic facts expected to matter for 6+ months.
- Operational details belong in COLBY Current Truth, reports, project records, or logs.
- Do not re-add obsolete troubleshooting artifacts to ChatGPT memory.
- Do not blend historical lab infrastructure with live McKenzie operations.
- For McKenzie Solar, use live bridge/API data as source of truth.

Source:
This archive was based on Greg’s exported/pasted ChatGPT memory list uploaded as Pasted text.txt during the 2026-06-16 cleanup session.
```

## Latest Sync Report

Source: `/opt/colby/reports/sync/latest_sync.md`

# Auto-Sync Report

Generated: 2026-06-21T16:42:22

Purpose: Regenerate and validate derived reports after approved registry changes.

## Generator Results

### milestone_status
- Path: /opt/colby/services/projects/milestone_status_generator.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/projects/current_milestone_status.md
```

### capability_status
- Path: /opt/colby/services/projects/capability_registry_generator.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/capabilities/current_capability_status.md
CAPABILITY_COUNT=32
OPERATIONAL_COUNT=18
PLANNED_COUNT=14
```

### project_status
- Path: /opt/colby/services/projects/project_status_generator.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/projects/current_project_status.md
```

### dependency_status
- Path: /opt/colby/services/projects/dependency_registry.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/projects/current_dependency_status.md
```

### critical_path
- Path: /opt/colby/services/projects/critical_path_engine.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/projects/current_critical_path.md
```

### project_impact
- Path: /opt/colby/services/projects/project_impact_analysis.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/projects/current_project_impact.md
```

### executive_daily_review
- Path: /opt/colby/services/reporting/executive_daily_review.py
- Status: ok
- Return Code: 0
- Stdout:
```
WROTE: /opt/colby/reports/executive/current_day_summary.md
```

## Output Validation

- OK: /opt/colby/reports/projects/current_milestone_status.md (2863 bytes)
- OK: /opt/colby/reports/capabilities/current_capability_status.md (5914 bytes)
- OK: /opt/colby/reports/projects/current_project_status.md (3152 bytes)
- OK: /opt/colby/reports/projects/current_dependency_status.md (2434 bytes)
- OK: /opt/colby/reports/projects/current_critical_path.md (1893 bytes)
- OK: /opt/colby/reports/projects/current_project_impact.md (2819 bytes)
- OK: /opt/colby/reports/executive/current_day_summary.md (4652 bytes)
- OK: /opt/colby/reports/personas/current_persona_status.md (860 bytes)

## Sync Summary

- Generator Failures: 0
- Missing or Empty Outputs: 0
- Status: PASS
