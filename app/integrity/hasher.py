# app/integrity/hasher.py

import hashlib
from pathlib import Path
from app.utils.file_utils import get_files_recursive

def compute_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    try:
        with file_path.open("rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return ""  # Dosya okunamazsa boş döner

def generate_hashes(target_dir: Path) -> dict:
    hashes = {}
    files = get_files_recursive(target_dir)
    for file_path in files:
        hash_val = compute_sha256(file_path)
        if hash_val:
            hashes[str(file_path.resolve())] = hash_val
    return hashes
