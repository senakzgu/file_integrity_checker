from pathlib import Path
import json
from datetime import datetime

def write_hashes(hashes: dict, output_file: Path) -> None:
    try:
        with output_file.open("w") as f:
            json.dump(hashes, f, indent=2)
    except Exception:
        pass  # Cron uyumu: terminal çıktısı yok

def write_report(differences: dict, report_file: Path) -> None:
    try:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        lines = [f"Integrity Report - {now}\n"]
        for change_type in ["added", "removed", "modified"]:
            items = differences.get(change_type, [])
            lines.append(f"\n{change_type.upper()} FILES ({len(items)}):")
            lines.extend(items if items else ["None"])

        with report_file.open("w") as f:
            f.write("\n".join(lines))
    except Exception:
        pass
