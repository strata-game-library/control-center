#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, capture=True):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=capture, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        if capture:
            print(f"Error running command: {cmd}\nOutput: {e.output}\nError: {e.stderr}")
        return None

def get_file_sha(repo, path):
    return run_command(f"gh api repos/{repo}/contents/{path} --jq '.sha' 2>/dev/null")

def sync_file(repo, source_path, dest_path, overwrite=True):
    if not overwrite:
        # Check if exists
        exists = run_command(f"gh api repos/{repo}/contents/{dest_path} --jq '.name' 2>/dev/null")
        if exists:
            print(f"  ⏭️ {dest_path} (exists)")
            return True

    sha = get_file_sha(repo, dest_path)
    content = Path(source_path).read_text()
    
    # Using vendor-connectors via CLI call
    msg = "chore(sync): update from control-center" if overwrite else "chore(init): bootstrap from control-center"
    
    cmd = [
        "vendor-connectors", "call", "github", "update_repository_file",
        "--github_owner", repo.split('/')[0],
        "--github_repo", repo.split('/')[1],
        "--file_path", dest_path,
        "--file_data", content,
        "--msg", msg
    ]
    if sha:
        cmd.extend(["--file_sha", sha])

    # Run via subprocess to avoid complex shell quoting of large file content
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"  {'✅' if overwrite else '✨'} {dest_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ {dest_path}: {e.stderr.decode()}")
        return False

def main():
    config_path = Path("repo-config.json")
    if not config_path.exists():
        print("repo-config.json not found")
        sys.exit(1)

    config = json.loads(config_path.read_text())
    org = config["organization"]
    dry_run = os.environ.get("DRY_RUN") == "true"

    for repo_entry in config["repositories"]:
        if not repo_entry.get("sync", False):
            continue

        repo_name = repo_entry["name"]
        full_repo = f"{org}/{repo_name}"
        print(f"📦 {full_repo}")

        if dry_run:
            print("  [DRY RUN] Would sync files...")
            continue

        # Phase 1: Always Sync
        always_sync_root = Path("repository-files/always-sync")
        for p in always_sync_root.rglob("*"):
            if p.is_file():
                rel_path = str(p.relative_to(always_sync_root))
                sync_file(full_repo, p, rel_path, overwrite=True)

        # Phase 2: Initial Only
        initial_only_root = Path("repository-files/initial-only")
        if initial_only_root.exists():
            for p in initial_only_root.rglob("*"):
                if p.is_file():
                    rel_path = str(p.relative_to(initial_only_root))
                    sync_file(full_repo, p, rel_path, overwrite=False)

if __name__ == "__main__":
    main()
