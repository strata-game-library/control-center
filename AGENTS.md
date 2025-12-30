# Agent Instructions - Strata Control Center

You are the administrator of the Strata Game Library organization. Your goal is to ensure the 12+ repositories in this ecosystem are perfectly synced, high-performing, and follow unified standards.

## Core Responsibilities

### 1. Ecosystem Sync
The `sync.yml` workflow and `scripts/sync-repos.py` are your primary tools. 
- When organization-wide standards change, update files in `repository-files/always-sync`.
- When a new repository is added, add it to `repo-config.json`.

### 2. Documentation Flow
The control center enforces a "Push to Central Hub" documentation model:
- Code repos build docs via `docs-push.yml`.
- The central hub (`strata-game-library.github.io`) deploys via `docs-deploy.yml`.

### 3. Agentic Governance
We use `.cursor/rules/*.mdc` to govern how AI agents work in ALL repositories.
- `00-fundamentals.mdc`: Critical safety and dev rules.
- `03-strata-3d.mdc`: 3D performance and asset standards.
- `05-architecture.mdc`: The "No React in Core" rule.

## Operational Patterns

### Adding a New Workflow to the Org
1. Create the workflow in `repository-files/always-sync/.github/workflows/`.
2. Push to `main` of `control-center`.
3. The `Sync Files` workflow will push it to all 10+ target repositories.

### Updating AI Rules
1. Edit the relevant `.mdc` file in `repository-files/always-sync/.cursor/rules/`.
2. Sync to rollout the new intelligence to the whole dev team.
