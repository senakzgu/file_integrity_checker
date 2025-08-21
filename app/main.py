from config import TARGET_DIR, BASELINE_HASH_FILE, INTEGRITY_REPORT_FILE
from pathlib import Path

def run_integrity_check():
    try:
        # Çıktı klasörü yoksa oluştur
        INTEGRITY_REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

        # İlk çalışmada baseline dosyası yoksa oluşturulacak
        if not BASELINE_HASH_FILE.exists():
            from app.integrity.hasher import generate_hashes
            from app.integrity.writer import write_hashes

            hashes = generate_hashes(TARGET_DIR)
            write_hashes(hashes, BASELINE_HASH_FILE)
        
        else:
            from app.integrity.hasher import generate_hashes
            from app.integrity.comparer import compare_hashes
            from app.integrity.writer import write_report

            new_hashes = generate_hashes(TARGET_DIR)
            differences = compare_hashes(BASELINE_HASH_FILE, new_hashes)
            write_report(differences, INTEGRITY_REPORT_FILE)

    except Exception:
        # Cron uyumlu: hiçbir çıktıyı terminale verme
        pass
