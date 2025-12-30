# CLAUDE.md - Strata Control Center

This file guides Claude Code when working on the `strata-game-library/control-center`.

## Project Role
This is the **Orchestrator** for the entire Strata organization. It manages:
- Repository synchronization (`repo-config.json`, `scripts/sync-repos.py`)
- Organization-wide CI/CD standards (`repository-files/always-sync`)
- AI agentic rules and workflows
- Documentation flow for the whole org

The control-center follows the **Parent-Child** pattern established in `jbcom/control-center`.

## Development Commands

```bash
# Sync files to all repos (dry run)
DRY_RUN=true ./scripts/sync-repos.py

# Add a new repo to the organization
# 1. Update repo-config.json
# 2. Run sync
```

## Structure
- `repository-files/`: The "source" files that get synced to other repos.
  - `always-sync/`: Files that are overwritten every time (Workflows, Rules).
  - `initial-only/`: Starter templates for new repos.
- `scripts/`: Python/Bash scripts for automation.
- `.github/workflows/`: Workflows for the control-center itself (Sync, Connector).

## Rules for this Repo
1. **Never commit raw tokens**. Use `GH_TOKEN` or `CI_GITHUB_TOKEN` environment variables.
2. **Phase Sync Philosophy**:
   - Phase 1 (Always Sync): For configs that MUST stay uniform (CI, Lint, Rules).
   - Phase 2 (Initial Only): For files that provide a base but might be edited (README, package.json).
3. **Reference the Parent**: We are a child of `jbcom/control-center`. Follow its patterns for metadata management.
