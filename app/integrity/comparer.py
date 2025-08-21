from pathlib import Path
import json

def load_baseline(baseline_path: Path) -> dict:
    try:
        with baseline_path.open("r") as f:
            return json.load(f)
    except Exception:
        return {}

def compare_hashes(baseline_path: Path, current_hashes: dict) -> dict:
    baseline_hashes = load_baseline(baseline_path)

    added = []
    removed = []
    modified = []

    baseline_files = set(baseline_hashes.keys())
    current_files = set(current_hashes.keys())

    for file in current_files - baseline_files:
        added.append(file)

    for file in baseline_files - current_files:
        removed.append(file)

    for file in current_files & baseline_files:
        if baseline_hashes[file] != current_hashes[file]:
            modified.append(file)

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }
