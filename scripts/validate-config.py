#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def validate_repo_config():
    config_path = Path("repo-config.json")
    if not config_path.exists():
        print("❌ repo-config.json missing")
        return False
    
    try:
        config = json.loads(config_path.read_text())
        repos = config.get("repositories", [])
        if not repos:
            print("❌ No repositories defined in config")
            return False
            
        print(f"✅ repo-config.json valid ({len(repos)} repositories)")
        return True
    except Exception as e:
        print(f"❌ repo-config.json invalid JSON: {e}")
        return False

def validate_sync_structure():
    required_dirs = [
        "repository-files/always-sync",
        "repository-files/initial-only",
        "scripts",
        ".github/workflows"
    ]
    all_valid = True
    for d in required_dirs:
        if not Path(d).exists():
            print(f"❌ Missing directory: {d}")
            all_valid = False
    
    if all_valid:
        print("✅ Sync structure valid")
    return all_valid

def main():
    success = validate_repo_config() and validate_sync_structure()
    if not success:
        sys.exit(1)
    print("🚀 Control Center validation successful")

if __name__ == "__main__":
    main()
