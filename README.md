# message-queue-2
# RabbitMQ Publisher & Consumer

## 📌 Deskripsi
Proyek ini adalah sistem **Publisher-Subscriber** berbasis **Flask** dan **RabbitMQ**, dengan penyimpanan data menggunakan **SQLite**.

## 📌 **Fitur**
- **Publisher** mengirim pesan ke RabbitMQ dan menyimpannya di database.
- **Subscriber** menerima pesan dari RabbitMQ dan menyimpannya ke database.

---

## 📂 **Struktur Proyek**
```bash
.
├── config.py           # Konfigurasi database & RabbitMQ
├── publisher.py        # Aplikasi Flask untuk mengirim pesan
├── subscriber.py       # Worker yang mendengarkan pesan dari RabbitMQ
├── templates/
│   ├── index.html      # Halaman HTML untuk publisher
├── requirements.txt    # Dependency list
├── README.md           # Dokumentasi
```

---

## 🚀 **Cara Menjalankan Proyek**
### **Instalasi Dependensi**
Pastikan **Python** dan **RabbitMQ** terinstall.

```bash
# Buat virtual environment (opsional)
python -m venv .venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Instal dependensi
pip install -r requirements.txt
```

### **Jalankan Publisher**
```bash
python publisher.py
```
> Publisher akan berjalan di `http://localhost:5000`

### **Jalankan Subscriber**
```bash
python subscriber.py
```
> Akses UI di `http://localhost:5000` untuk mengirim pesan.
> Subscriber akan menunggu pesan masuk dari RabbitMQ.

---

### 📌 **Contoh Request ke Publisher**
```bash
curl -X POST http://localhost:5000/publish -H "Content-Type: application/json" -d '{"message": "Halo"}'
```
> Respon: `{"status": "Message sent and stored"}`

---
