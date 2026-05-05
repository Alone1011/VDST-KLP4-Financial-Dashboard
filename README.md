# 🌟 Financial & Equity Dashboard (IHSG Edition)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B?style=flat-square&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=flat-square&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive_Charts-3F4F75?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 🚀 Deskripsi Proyek

**Financial & Equity Dashboard** adalah sebuah aplikasi web interaktif yang dibangun menggunakan Streamlit. Aplikasi ini dirancang untuk mempermudah siapa saja—baik analis pemula maupun masyarakat awam—dalam memvisualisasikan dan membaca pergerakan harga historis saham di Indeks Harga Saham Gabungan (IHSG).

Daripada melihat rentetan angka yang membingungkan di dalam _spreadsheet_, aplikasi ini mengubah data mentah menjadi grafik interaktif yang mudah dipahami. Selain itu, aplikasi ini berjalan secara mandiri dengan mengambil data dari repositori Kaggle secara otomatis dan menyimpannya di memori lokal (_cache_), sehingga sangat cepat dan tidak bergantung pada _API_ berbayar.

## 🛠️ Tech Stack

Proyek ini menggunakan teknologi dan _library_ berikut:

- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Framework untuk membangun antarmuka web interaktif secara instan.
- **Pandas**: Pustaka utama untuk manipulasi dan analisis data _time-series_.
- **Plotly**: Digunakan untuk merender grafik yang responsif dan interaktif (seperti _candlestick_).
- **Kagglehub**: Pustaka untuk mengunduh dataset IHSG secara otomatis langsung dari Kaggle.

## ✨ Fitur Utama

Aplikasi ini dibagi menjadi 3 halaman utama yang mudah dinavigasi:

- 📊 **Data Overview**
  Menampilkan ringkasan dataset yang berhasil dimuat, seperti total baris, jumlah kolom, dan cuplikan data (_dataframe_) mentah. Halaman ini berguna untuk memastikan data telah terunduh dengan benar sebelum dianalisis.
- 📈 **Interactive Visualization**
  Halaman inti tempat pengguna dapat memfilter rentang waktu dan melihat pergerakan harga saham melalui grafik interaktif (seperti _candlestick_ atau grafik garis). Pengguna dapat melihat tren dengan mudah tanpa perlu memahami banyak istilah teknis.
- 🧮 **Target Calculator**
  Sebuah kalkulator sederhana yang memungkinkan pengguna melakukan simulasi. Dengan memasukkan harga beli dan persentase target keuntungan atau batasan kerugian (_stop-loss_), pengguna bisa langsung melihat estimasi angka yang perlu mereka pantau.

## 📂 Struktur Direktori

```text
streamlit-dashboard/
├── app.py                     # Main file / Landing page aplikasi
├── requirements.txt           # Daftar library yang dibutuhkan
├── data/                      # Folder (opsional) untuk cache atau data lokal
├── utils/
│   └── loader.py              # Logic pipeline untuk mengunduh dan membaca data dari Kagglehub
└── pages/
    ├── 1_Overview.py          # Halaman ringkasan data dan metrik
    ├── 2_Visualisasi.py       # Halaman grafik interaktif Plotly
    └── 3_Kalkulator.py        # Halaman form interaktif kalkulator simulasi
```

## ⚙️ Instalasi & Cara Menjalankan

Berikut adalah langkah-langkah untuk menjalankan aplikasi ini di komputer lokal Anda:

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/username/vdst-financial-dashboard.git
   cd vdst-financial-dashboard
   ```

2. **Buat dan aktifkan _Virtual Environment_:**

   ```bash
   # Untuk Windows:
   python -m venv venv
   source venv/Scripts/activate  # atau .\venv\Scripts\activate di PowerShell

   # Untuk macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instal dependensi yang dibutuhkan:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit:**
   ```bash
   streamlit run app.py
   ```
   *Aplikasi akan otomatis terbuka di *browser* pada alamat `http://localhost:8501`.*

## 🤝 Panduan Kolaborasi (Git Workflow)

Untuk menjaga kerapian dan kualitas kode, seluruh anggota tim diwajibkan mengikuti aturan berikut:

- **Dilarang keras melakukan _commit_ dan _push_ langsung ke _branch_ `main`.**
- Setiap mengerjakan fitur atau halaman baru, buatlah _branch_ khusus. Contoh: `git checkout -b feature/interactive-chart`.
- Setelah fitur selesai, lakukan _push_ ke _branch_ tersebut dan buat **Pull Request (PR)** ke `main`.
- Kode baru dapat digabungkan (_merge_) ke `main` setelah diulas (direview) dan disetujui oleh anggota tim yang lain.

## 👥 Tim Pengembang

- **1. Core Architect (Rifki Yuliandra - 2311532011)**
  (Bertanggung jawab atas UI Utama & Data Pipeline otomatis dari Kaggle)
- **2. Logic & Visualization Engineer (Sherly Sukmadira Putri - 2311532015)**
  (Bertanggung jawab membangun grafik interaktif dan logika filtering data)
- **3. Interactive Form Developer (Muhammad Hafiz - 2311532007)**
  (Bertanggung jawab membuat formulir input dan logika matematika di kalkulator simulasi)
