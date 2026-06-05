# COLBY PROJECT CURRENT TRUTH

Generated Local Time: 2026-06-05T12:07:43-05:00

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
- Source file count: 13

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
- Size Bytes: 359
- Modified Time: 2026-05-29T07:40:33-05:00
- SHA256: 8b8c99790fbaace154b8fd19da151c2fc88bfb4b3913ab5f1cb0ed20ea9b662e

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
- Modified Time: 2026-06-05T12:07:42-05:00
- SHA256: 256a115c99575deaa639f4e90bda651c4207c8242f965b2905d78d2786c7d374

### Current Milestone Status
- Path: /opt/colby/reports/projects/current_milestone_status.md
- Required: True
- Exists: True
- Size Bytes: 2701
- Modified Time: 2026-06-05T12:07:42-05:00
- SHA256: 89dd181d1b24ef115fc447bdfdbbae10e4472efc45dceba8f544797ec5d6311e

### Current Dependency Status
- Path: /opt/colby/reports/projects/current_dependency_status.md
- Required: True
- Exists: True
- Size Bytes: 2120
- Modified Time: 2026-06-05T12:07:42-05:00
- SHA256: c03464c4eb6452cc7e23668cddbc2cab6e6ed138e5d0bb98891dc259ca3c5573

### Current Critical Path
- Path: /opt/colby/reports/projects/current_critical_path.md
- Required: True
- Exists: True
- Size Bytes: 1677
- Modified Time: 2026-06-05T12:07:43-05:00
- SHA256: 8da603d3e1c45f32c4de3a7b431d0f86b2ff147d13348c2455d62f061f017d2d

### Current Capability Status
- Path: /opt/colby/reports/capabilities/current_capability_status.md
- Required: True
- Exists: True
- Size Bytes: 5030
- Modified Time: 2026-06-05T12:07:42-05:00
- SHA256: b61069e55f63962966eb974968ff7fbea657758fa24ec416e25fe8b0dbbbed7a

### McKenzie Solar Data Bridge
- Path: /opt/colby/memory/projects/mckenzie_solar_data_bridge.md
- Required: True
- Exists: True
- Size Bytes: 3450
- Modified Time: 2026-06-05T12:07:34-05:00
- SHA256: 17da6368ba4cc5f0980bcb42c03465c4c462e0b7af173179398b783792f280d4

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

### Latest Sync Report
- Path: /opt/colby/reports/sync/latest_sync.md
- Required: False
- Exists: True
- Size Bytes: 2024
- Modified Time: 2026-06-05T12:07:43-05:00
- SHA256: a9a243e42565189b3ad33f55e118af2d3980974e8b2e1635c8f0ff2325fe3940

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
Home Assistant rebuild until return to McKenzie.

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

Generated: 2026-06-05T12:07:42

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

Generated: 2026-06-05T12:07:42

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

Generated: 2026-06-05T12:07:42

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

Generated: 2026-06-05T12:07:43

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

Generated: 2026-06-05T12:07:42

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

## Latest Sync Report

Source: `/opt/colby/reports/sync/latest_sync.md`

# Auto-Sync Report

Generated: 2026-06-05T12:07:43

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

## Output Validation

- OK: /opt/colby/reports/projects/current_milestone_status.md (2701 bytes)
- OK: /opt/colby/reports/capabilities/current_capability_status.md (5030 bytes)
- OK: /opt/colby/reports/projects/current_project_status.md (2475 bytes)
- OK: /opt/colby/reports/projects/current_dependency_status.md (2120 bytes)
- OK: /opt/colby/reports/projects/current_critical_path.md (1677 bytes)
- OK: /opt/colby/reports/projects/current_project_impact.md (2393 bytes)
- OK: /opt/colby/reports/personas/current_persona_status.md (112 bytes)

## Sync Summary

- Generator Failures: 0
- Missing or Empty Outputs: 0
- Status: PASS
