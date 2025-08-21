from pathlib import Path

# Kontrol edilecek dizin
TARGET_DIR = Path("/opt/scripts")

# Çıktı klasörü ve dosyaları
DATA_DIR = Path(__file__).parent / "data"
BASELINE_HASH_FILE = DATA_DIR / "baseline_hashes.txt"
INTEGRITY_REPORT_FILE = DATA_DIR / "integrity_report.txt"
