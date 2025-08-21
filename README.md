# 🛡️ File Integrity Checker

Bu proje, `/opt/scripts/` dizininde bulunan kritik dosyaların **bütünlüğünü korumak ve izlemek** amacıyla geliştirilmiş bir Python tabanlı dosya bütünlük kontrol sistemidir. Her gece çalışarak, dosyalarda meydana gelen **değişiklikleri, silinenleri ve eklenenleri** otomatik olarak algılar ve raporlar.

---

## 🚀 Özellikler

- 📂 Belirli bir dizindeki tüm dosyaları (alt dizinler dahil) tarar.
- 🔐 Her dosya için `SHA256` hash hesaplaması yapar.
- 📌 İlk çalışmada `baseline_hashes.txt` dosyasını oluşturur.
- 🧾 Sonraki çalışmalarda mevcut durum ile önceki durum karşılaştırılır.
- ✅ Farklar `integrity_report.txt` içine yazılır (`ADDED`, `REMOVED`, `MODIFIED`).
- 🕓 Tamamen sessiz çalışır (cron uyumlu).
- ❌ Terminal çıktısı yoktur; sadece dosya üretir.

---

## 📁 Klasör Yapısı

```
file_integrity_checker/
├── run.py                     # Uygulamanın giriş noktası (cron burayı çağırır)
├── config.py                  # Sabit ayarların tanımlandığı dosya
├── app/
│   ├── __init__.py
│   ├── main.py                # İş akışını yürüten mantık
│   ├── integrity/
│   │   ├── __init__.py
│   │   ├── hasher.py          # SHA256 hash üretimi
│   │   ├── comparer.py        # Hash karşılaştırma işlemi
│   │   └── writer.py          # Dosya çıktıları üretimi
│   └── utils/
│       ├── __init__.py
│       └── file_utils.py      # Dosya tarama yardımcıları
├── data/
│   ├── baseline_hashes.txt    # İlk hash kayıtlarının tutulduğu JSON dosyası
│   └── integrity_report.txt   # Son çalıştırmanın raporu
└── requirements.txt           # Harici bağımlılık yok, bilgi amaçlı
```

---

## ⚙️ Kurulum

### 1. Python 3 kurulu olduğundan emin olun

```bash
which python3
```

### 2. Bu projeyi klonlayın veya dizine geçin

```bash
cd ~/Desktop/file_integrity_checker
```

### 3. Gerekirse `data/` klasörünü oluşturun

```bash
mkdir -p data
```

---

## ▶️ Kullanım

### Elle çalıştırmak için:

```bash
python3 run.py
```

### Çıktılar:

- `data/baseline_hashes.txt`: İlk çalıştırmada oluşturulur.
- `data/integrity_report.txt`: Her karşılaştırma sonrası güncellenir.

---

## ⏱️ Cron Entegrasyonu

Her gece saat 02:00'de otomatik çalıştırmak için crontab’a şu satırı ekleyin:

### Kullanıcı bazlı (önerilen):

```bash
crontab -e
```

```cron
0 2 * * * /usr/bin/python3 /home/kullanici_adiniz/Desktop/file_integrity_checker/run.py
```

> Yol ve kullanıcı adını kendi sisteminize göre değiştirin.

---

## ✅ Test Senaryoları

| Senaryo No | Açıklama                        | Beklenen Sonuç              |
|------------|----------------------------------|------------------------------|
| TC-01      | İlk çalıştırma                  | baseline dosyası oluşur     |
| TC-02      | Dosya eklendi                   | `ADDED` olarak listelenir   |
| TC-03      | Dosya silindi                   | `REMOVED` olarak listelenir |
| TC-04      | Dosya değiştirildi              | `MODIFIED` olarak listelenir|
| TC-05      | Boş dizin                       | Hiçbir çıktı üretilmez      |
| TC-06      | Hash alınamayan dosya (izin)    | Atlanır, sistem çökmemeli   |
| TC-07      | Aynı dosya farklı path ile      | Silinmiş + eklenmiş sayılır |

---

## 🧪 Geliştirici Notları

- `str(file_path.resolve())` kullanılarak tüm path’ler normalize edilir.
- JSON formatı sayesinde `baseline_hashes.txt` dosyası okunabilir ve genişletilebilirdir.
- Kod yapısı modülerdir, test edilebilir.
- `data/` dışındaki hiçbir dizin yazma ihtiyacı duymaz.

---

## 📄 Lisans

MIT License — Dilediğiniz gibi kullanabilir, dağıtabilir ve geliştirebilirsiniz.
