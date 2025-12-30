# strata-game-library Control Center

Organization-level control center for **strata-game-library**. This repository manages shared configurations, CI/CD workflows, and AI-powered automation across all repositories in the organization.

## Purpose

- **Centralized CI/CD**: Standardized workflows for TypeScript, Node.js, Python, and Docker projects.
- **File Synchronization**: Ensures consistent `.github` configurations across all repositories.
- **AI Automation**: Integrated AI reviewers and automated CI fixers.

## Project Structure

```text
control-center/
├── .github/
│   └── workflows/
│       ├── sync.yml                   # Main synchronization workflow
│       ├── ecosystem-orchestrator.yml  # AI task orchestration
│       └── ecosystem-fixer.yml         # Automated CI failure fixer
├── repository-files/
│   ├── always-sync/                   # Files that are always kept in sync
│   │   └── .github/
│   │       ├── workflows/
│   │       │   ├── ci.yml             # Shared CI for TS/Node/Python/Docker
│   │       │   └── ecosystem-connector.yml
│   │       └── dependabot.yml         # Dependency updates
│   └── initial-only/                  # Files synced only once (for new repos)
│       ├── .github/
│       │   └── pull_request_template.md
│       ├── CODE_OF_CONDUCT.md
│       └── SECURITY.md
└── README.md
```

## How It Works

### Synchronization
The `sync.yml` workflow runs on every push to the `main` branch. It iterates through all non-archived repositories in the `strata-game-library` organization:
1. **Always Sync**: Files in `repository-files/always-sync/` are forcefully synced (overwritten) to all repositories.
2. **Initial Only**: Files in `repository-files/initial-only/` are only created if they do not already exist in the target repository.

### CI/CD Pipeline
The shared `ci.yml` provides:
- **Node.js/TypeScript**: Linting, type-checking, building, and testing (supports `npm` and `pnpm`).
- **Python**: Support for `uv`, `ruff`, and `pytest`.
- **Docker**: Automatic build checks if a `Dockerfile` is present.
- **Bundle Size**: Automatic bundle size reporting for distribution folders.

### AI-Powered Features
Each repository is equipped with an `ecosystem-connector.yml` that enables:
- **AI Reviews**: Automated PR analysis using Claude.
- **Interactive Commands**: Support for `@claude`, `/jules`, and `/cursor` in comments.
- **Auto-Fix**: Attempts to automatically resolve CI failures.

## Adding New Shared Files

1. Add the file to `repository-files/always-sync/` if it should be kept up to date everywhere.
2. Add the file to `repository-files/initial-only/` if it's a template for new projects.
3. Push to `main` to trigger the sync.
