# COLBY PROJECT CURRENT TRUTH

Generated Local Time: 2026-06-09T14:46:54-05:00

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
- Source file count: 21

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
- Size Bytes: 6460
- Modified Time: 2026-06-09T14:35:21-05:00
- SHA256: 9e81eb1011845cca53102a63d5b6d64318a58da6ac20a98ca4ff6aa1732c12c6

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
- Size Bytes: 1845
- Modified Time: 2026-06-09T14:45:51-05:00
- SHA256: 72bb14daeb4829e4ef488b9a2f45476c1171732db93dd3858eb7da2118f42a5b

### Infrastructure Inventory
- Path: /opt/colby/memory/core/infrastructure_inventory.md
- Required: False
- Exists: True
- Size Bytes: 1834
- Modified Time: 2026-06-09T10:42:57-05:00
- SHA256: f39f6fb7c72dc94964da5c3d464be9f82ce56caaec615dba3bfd93224ff4593e

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
- Size Bytes: 423
- Modified Time: 2026-06-09T14:25:14-05:00
- SHA256: b408cc0bfe5041f488093bf9fdd67de58ce7a0eed2d8b121a82738db9684cc61

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
- Size Bytes: 3204
- Modified Time: 2026-06-05T12:07:34-05:00
- SHA256: 5e209839e6dd9ce85aaaf6513041133532b7ea8823e87a1dd2cb94a4353a6bb6

### Current Project Status
- Path: /opt/colby/reports/projects/current_project_status.md
- Required: True
- Exists: True
- Size Bytes: 2475
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: 949e9747753fcfe6298c16c1e09427e0c864b6bb3ffb01101e84a7c7ac8a036a

### Current Milestone Status
- Path: /opt/colby/reports/projects/current_milestone_status.md
- Required: True
- Exists: True
- Size Bytes: 2701
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: b379ee255e66c243d4365ae93d825960db4c9f19fb0e5abb5f952a044daefa45

### Current Dependency Status
- Path: /opt/colby/reports/projects/current_dependency_status.md
- Required: True
- Exists: True
- Size Bytes: 2120
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: f596a011407c0f6f3599b5ba9330900b8d6b7414eb29082385c1bcc665089b10

### Current Critical Path
- Path: /opt/colby/reports/projects/current_critical_path.md
- Required: True
- Exists: True
- Size Bytes: 1677
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: d44ede9580306c94ac2439920866f08c5f81720ebdae989f0989e63686229cce

### Current Capability Status
- Path: /opt/colby/reports/capabilities/current_capability_status.md
- Required: True
- Exists: True
- Size Bytes: 5030
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: be94362f20f84eacd635b9d802ed66e7af87a0a1069092fcd944678d32b1a935

### McKenzie Solar Data Bridge
- Path: /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- Required: True
- Exists: True
- Size Bytes: 3450
- Modified Time: 2026-06-05T12:07:34-05:00
- SHA256: 17da6368ba4cc5f0980bcb42c03465c4c462e0b7af173179398b783792f280d4

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
- Size Bytes: 5369
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: fe5cab1617d98ba5a8cc3dedec59583c15e18906ca68c26bc05961551e55f661

### Recent Investigations
- Path: /opt/colby/reports/investigations
- Required: False
- Exists: True
- Size Bytes: 4096
- Modified Time: 2026-06-05T13:17:17-05:00
- SHA256: e2e36caeee9a4353d7c1fa9be494f070419a40b6bd3b2421f4e39c2bc6513ceb

### Latest Sync Report
- Path: /opt/colby/reports/sync/latest_sync.md
- Required: False
- Exists: True
- Size Bytes: 2294
- Modified Time: 2026-06-09T14:46:54-05:00
- SHA256: 91a29ede3de74d817592378d44027ccca84867a4353af50d59f752cd6c670e90

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
Right Turn (on hold)

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

## Current Project Status

Source: `/opt/colby/reports/projects/current_project_status.md`

# Current Project Status

Generated: 2026-06-09T14:46:54

Purpose: Summarize authoritative project registry files for Colby planning and dependency reasoning.

Project Count: 5

## Executive Summary

- Active Projects: 2
- Deferred Projects: 1

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
- Status: Deferred
- Priority: Medium
- Phase: Planning
- Completion: 10%
- Owner: Greg

Depends On:
- Return to McKenzie

Blocks:
- Solar Assistant Integration
- MQTT Architecture

Supports:
- Infrastructure Automation

Next Actions:
- Resume after relocation

### Unnamed Project

- Source File: /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- Status: Planned
- Priority: High
- Phase: Read-only API foundation
- Completion: Unknown
- Owner: Unknown

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
- Status: Active
- Priority: High
- Phase: Planning
- Completion: 0%
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
- Build Persona Memory Isolation
- Build Persona Authority Boundaries

## Operating Interpretation

- Project registry files are authoritative for project names, status, phase, completion, dependencies, blockers, and next actions.
- Do not infer projects outside the project registry unless explicitly asked for brainstorming.
- Use this report as the summary layer; use project files as the source of truth.

## Current Milestone Status

Source: `/opt/colby/reports/projects/current_milestone_status.md`

# Current Milestone Status

Generated: 2026-06-09T14:46:54

Purpose: Calculate project progress from milestone registry files.

Milestone Registry Count: 4

## Summary

- Colby Cognitive Operating System: 56% complete (5/9); next: Dependency Awareness
- Conversation Intelligence: 92% complete (11/12); next: Autonomous Project Updates
- Home Assistant Multi-Site Architecture: 17% complete (1/6); next: MQTT Architecture
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
- Completed Milestones: 1
- Remaining Milestones: 5
- Total Milestones: 6
- Calculated Completion: 17%
- Next Milestone: MQTT Architecture

Completed:
- Initial Architecture

Remaining:
- MQTT Architecture
- Solar Assistant Integration
- Multi-Site Connectivity
- Voice Layer
- Production Deployment

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

Generated: 2026-06-09T14:46:54

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
- Status: Deferred
- Phase: Planning
- Completion: 10%
- Depends On:
  - Return to McKenzie (external or not registered)
- Blocks:
  - Solar Assistant Integration
  - MQTT Architecture
- Supports:
  - Infrastructure Automation

### mckenzie_solar_data_bridge
- Status: Planned
- Phase: Read-only API foundation
- Completion: Unknown
- Depends On:
  - None
- Blocks:
  - None
- Supports:
  - None

### Open WebUI Persona Integration
- Status: Active
- Phase: Planning
- Completion: 0%
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

- Home Assistant Multi-Site Architecture is deferred.
  - Dependency: Return to McKenzie
  - Blocks: Solar Assistant Integration, MQTT Architecture

## Critical Path Signals

- Home Assistant Multi-Site Architecture blocks: Solar Assistant Integration, MQTT Architecture
- Conversation Intelligence remains a critical path dependency for Open WebUI Persona Integration.
- Home Assistant Multi-Site Architecture remains dependent on return to McKenzie.

## Operating Interpretation

- Use project registry files as source of truth.
- Use this dependency report for impact analysis and sequencing.
- Do not infer dependencies outside registered project files unless Greg requests brainstorming.

## Current Critical Path

Source: `/opt/colby/reports/projects/current_critical_path.md`

# Current Critical Path

Generated: 2026-06-09T14:46:54

Purpose: Identify blocked projects, unblock criteria, impact, and recommended critical-path focus.

Blocker Registry Count: 2

## Home Assistant Multi-Site Architecture

- Source File: /opt/colby/memory/blockers/home_assistant_multi_site.md
- Status: Blocked
- Priority: Medium
- Risk: Low
- Impact: Solar Assistant, MQTT, and Voice remain deferred

Blocked By:
- Return to McKenzie

Unblock Criteria:
- Return to McKenzie completed
- Infrastructure available
- Home Assistant rebuild approved

## Open WebUI Persona Integration

- Source File: /opt/colby/memory/blockers/openwebui_persona_integration.md
- Status: Unblocked
- Priority: High
- Risk: Medium
- Impact: Ready for planning and controlled implementation

Blocked By:
- None

Unblock Criteria:
- Review Generator operational
- Review Validator operational
- Promotion Candidate Builder operational
- Authority Validator operational
- Conversation Intelligence project approved complete

## Executive Summary

Blocked Projects: 1
- Home Assistant Multi-Site Architecture

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

Generated: 2026-06-09T14:46:54

Purpose: Inventory operational and planned capabilities from milestone registries.

Capability Count: 27

## Summary

- Operational Capabilities: 17
- Planned Capabilities: 10

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

## Operating Interpretation

- Completed milestones are treated as operational capabilities.
- Incomplete milestones are treated as planned capabilities.
- Capability status is derived from milestone registry files.
- Use this report for capability questions before inferring from projects or general memory.

## McKenzie Solar Data Bridge

Source: `/opt/colby/memory/projects/mckenzie_solar_data_bridge.md`

# Project: McKenzie Solar Data Bridge

Status:
Planned

Priority:
High

Phase:
Read-only API foundation

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

Generated: 2026-06-09T14:46:54

Purpose:
Capture recent accomplishments, discoveries, risks, and next actions so Colby and external Current Truth consumers can reason from recent work instead of relying only on hard-coded reports.

## Recent Executive Signals

- Built and validated a governed pipeline for OpenWebUI conversation inventory, export, review, validation, promotion candidate generation, task-only application, source attribution, and authority validation.
- /opt/colby/services/conversation_indexer/conversation_inventory.py; /opt/colby/services/conversation_indexer/conversation_exporter.py; /opt/colby/services/conversation_review/review_generator.py; /opt/colby/services/conversation_review/review_validator.py; /opt/colby/services/promotion/promotion_candidate_builder.py; /opt/colby/services/promotion/apply_task_candidate.py; /opt/colby/services/decision_engine/authority_validator.py; /opt/colby/reports/decision_engine/current_authority_summary.md
- Colby-greg correctly identified the conversation review generator as the highest priority and OpenWebUI persona integration as deferred.
- Risks / Open Issues:
- Capability awareness can still lag unless after-action records are created after each build; Colby should not execute self-modifying commands yet.
- Next Step:
- Build capability inventory generation and load current_capabilities.md into context.
- After Action Report - 2026-06-05 - McKenzie Solar Dashboard V1 Stable
- Project: McKenzie Solar Data Bridge
- McKenzie Solar Dashboard V1 Stable achieved.
- Restored dashboard generation pipeline.
- Added expected vs actual solar analytics.
- Fixed battery power reporting.
- Verified MQTT, occupancy, weather, dashboard generation, validation, and deployment pipelines.
- Next Priorities:
- 5. Solar anomaly detection.
- McKenzie Solar Dashboard V1 is operationally stable.
- PI4 remains the operational dashboard and GitHub publishing host for McKenzie Solar web assets.
- Solar Assistant MQTT and PI4 SQLite-derived analytics remain the verified operational source for McKenzie Solar data.
- Dashboard changes must pass regression validation before GitHub commit/push.
- Historical Solar Assistant exports are useful for daily/seasonal modeling but not authoritative for high-resolution peak records.
- McKenzie Solar Dashboard V1 Stable achieved. Validation-gated publishing, historical production intelligence, sunset SOC forecasting, survivability analytics, and array seasonal-best tracking are operational.
- Investigation Record
- Title: McKenzie Solar Daylight 0W Dashboard Event Forensic Investigation
- Investigate the temporary daylight 0W solar dashboard event and verify dashboard field lineage using live Pi4 evidence.
- Verified field lineage from MQTT to mqtt_raw to solar_metrics_1min to energy_analysis to solarstatus_json.py to solarstatus.json to dashboard. Confirmed solarstatus_json.py uses production /home/cothrang/solar-collector/solar.db. Measured normalize_solar.py runtime around 31 seconds. Verified no execution locking. Captured direct evidence of two normalize_solar.py processes running simultaneously at the 12:45 boundary.
- Finding:
- Concurrent normalize_solar.py execution is real. One instance runs from cron and another runs inside update_dashboard.sh at the same 15-minute dashboard boundary. No lock or serialization prevents overlap.
- Concurrent normalization is the leading root-cause candidate for the transient daylight solar_w=0 and mode=null dashboard snapshot. MQTT, raw data, normalized data, analysis view, and wrong-database hypotheses were cleared.
- Next Action:

## Interpretation

- This report is a synthesized continuity layer, not a source of live system telemetry.
- Treat source project files, after-action records, and live bridge/API data as higher authority when conflicts exist.
- Use this report to answer what changed recently, what was learned, and what should happen next.

## Source Files Reviewed

- /opt/colby/reports/after_action/after_action_20260531_091521.md
- /opt/colby/reports/after_action/after_action_20260605_120622_mckenzie_solar_v1_stable.md
- /opt/colby/reports/after_action/after_action_20260605_120636_mckenzie_solar_v1_stable.md
- /opt/colby/reports/after_action/after_action_20260605_120734_mckenzie_solar_v1_stable.md
- /opt/colby/reports/investigations/investigation_20260605_131717_mckenzie_solar_daylight_0w_dashboard_event_forensic_investigation.md
- /opt/colby/memory/workspaces/cognitive_workstead/README.md
- /opt/colby/memory/workspaces/cognitive_workstead/decisions.md
- /opt/colby/memory/workspaces/cognitive_workstead/goals.md
- /opt/colby/memory/workspaces/cognitive_workstead/assumptions.md
- /opt/colby/memory/workspaces/cognitive_workstead/milestones.md
- /opt/colby/memory/projects/colby_cognitive_operating_system.md
- /opt/colby/memory/projects/home_assistant_multi_site.md
- /opt/colby/memory/projects/conversation_intelligence.md
- /opt/colby/memory/projects/openwebui_persona_integration.md
- /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- /opt/colby/memory/core/current_capabilities.md
- /opt/colby/memory/core/next_actions.md
- /opt/colby/state/current_state.md
- /opt/colby/reports/projects/current_project_status.md
- /opt/colby/reports/projects/current_milestone_status.md
- /opt/colby/reports/projects/current_project_impact.md

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

## Latest Sync Report

Source: `/opt/colby/reports/sync/latest_sync.md`

# Auto-Sync Report

Generated: 2026-06-09T14:46:54

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
CAPABILITY_COUNT=27
OPERATIONAL_COUNT=17
PLANNED_COUNT=10
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

- OK: /opt/colby/reports/projects/current_milestone_status.md (2701 bytes)
- OK: /opt/colby/reports/capabilities/current_capability_status.md (5030 bytes)
- OK: /opt/colby/reports/projects/current_project_status.md (2475 bytes)
- OK: /opt/colby/reports/projects/current_dependency_status.md (2120 bytes)
- OK: /opt/colby/reports/projects/current_critical_path.md (1677 bytes)
- OK: /opt/colby/reports/projects/current_project_impact.md (2393 bytes)
- OK: /opt/colby/reports/executive/current_day_summary.md (5369 bytes)
- OK: /opt/colby/reports/personas/current_persona_status.md (112 bytes)

## Sync Summary

- Generator Failures: 0
- Missing or Empty Outputs: 0
- Status: PASS
