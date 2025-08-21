from pathlib import Path

def get_files_recursive(directory: Path) -> list[Path]:
    """
    Belirtilen dizin altında tüm dosyaları (alt dizinler dahil) tarar.
    Sadece gerçek dosyaları (symlink ve klasör hariç) döner.
    """
    if not directory.exists() or not directory.is_dir():
        return []

    return [f for f in directory.rglob("*") if f.is_file()]
