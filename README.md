
# Monitoring Kualitas Udara PM2.5

## Studi Kasus

Proyek ini merupakan program sederhana untuk memantau kualitas udara berdasarkan data konsentrasi PM2.5 yang menyerupai hasil pembacaan sensor Internet of Things (IoT). Program dikembangkan menggunakan Python untuk mengolah data, menghitung nilai rata-rata PM2.5, mendeteksi nilai yang melewati ambang simulasi, serta menampilkan perubahan konsentrasi PM2.5 dalam bentuk grafik.

Proyek ini bertujuan untuk memahami penerapan analisis data dalam pemantauan lingkungan. Pengembangannya juga terinspirasi oleh konsep Artificial Intelligence of Things (AIoT) dan pemanfaatan High Performance Computing (HPC) untuk pengolahan data lingkungan dalam skala yang lebih besar.

**Catatan:** Data yang digunakan dalam proyek ini merupakan data simulasi, bukan hasil pengukuran sensor udara secara langsung.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman utama.
- **Pandas** — membaca dan mengolah dataset.
- **Matplotlib** — membuat grafik perubahan konsentrasi PM2.5.
- **Visual Studio Code** — lingkungan pengembangan program.
- **GitHub** — menyimpan kode dan dokumentasi proyek.

## Dataset

Dataset disimpan dalam file `data.csv` dan berisi data simulasi konsentrasi PM2.5 pada delapan waktu pengamatan.

### Struktur Dataset

| Atribut | Keterangan |
|---|---|
| `waktu` | Waktu pengamatan kualitas udara. |
| `pm25` | Nilai konsentrasi PM2.5 pada waktu pengamatan. |

### Contoh Dataset

```csv
waktu,pm25
08:00,12
09:00,18
10:00,25
11:00,32
12:00,42
13:00,55
14:00,38
15:00,28
```

Nilai PM2.5 pada dataset digunakan untuk melihat perubahan konsentrasi partikel halus dari pagi hingga sore hari.

## Fitur Program

### 1. Menampilkan Data

Program membaca file `data.csv` dan menampilkan seluruh data waktu pengamatan beserta nilai PM2.5.

### 2. Menghitung Rata-rata PM2.5

Program menghitung nilai rata-rata konsentrasi PM2.5 berdasarkan seluruh data yang tersedia.

### 3. Peringatan Ambang Simulasi

Program memeriksa apakah nilai PM2.5 tertinggi melewati ambang simulasi sebesar 35. Jika nilai maksimum lebih besar dari ambang tersebut, program menampilkan peringatan.

Ambang 35 dalam proyek ini hanya digunakan untuk simulasi logika peringatan dan tidak dimaksudkan sebagai standar resmi kualitas udara.

### 4. Visualisasi Grafik

Program menampilkan grafik garis yang memperlihatkan perubahan nilai PM2.5 berdasarkan waktu pengamatan.

Grafik juga dilengkapi garis putus-putus sebagai penanda ambang simulasi agar perubahan nilai lebih mudah diamati.

## Alur Kerja Program

1. Membaca dataset dari file `data.csv`.
2. Menampilkan data pengamatan kualitas udara.
3. Menghitung rata-rata nilai PM2.5.
4. Mencari nilai PM2.5 tertinggi.
5. Membandingkan nilai maksimum dengan ambang simulasi.
6. Menampilkan peringatan jika nilai maksimum melewati ambang.
7. Membuat grafik perubahan PM2.5 menggunakan Matplotlib.

## Struktur Folder

```text
monitoring-kualitas-udara/
├── data.csv       # Dataset simulasi PM2.5
├── main.py        # Program monitoring kualitas udara
└── README.md      # Dokumentasi proyek
```

## Contoh Output

```text
=== MONITORING KUALITAS UDARA ===
 waktu  pm25
 08:00    12
 09:00    18
 10:00    25
 11:00    32
 12:00    42
 13:00    55
 14:00    38
 15:00    28

Rata-rata PM2.5: 31.25
Peringatan: PM2.5 melewati ambang simulasi!
```

Setelah output ditampilkan, program juga menampilkan grafik perubahan konsentrasi PM2.5 dengan garis ambang simulasi pada nilai 35.

## Analisis Hasil

Berdasarkan dataset simulasi, nilai rata-rata PM2.5 adalah 31,25, sedangkan nilai tertingginya mencapai 55 pada pukul 13.00.

Karena nilai maksimum tersebut lebih besar daripada ambang simulasi sebesar 35, program menampilkan peringatan. Nilai PM2.5 kemudian menurun pada pukul 14.00 dan 15.00.

Hasil ini menunjukkan bahwa program dapat digunakan untuk menganalisis perubahan data lingkungan, menghitung statistik sederhana, dan memberikan peringatan berdasarkan kondisi yang telah ditentukan.

## Kelebihan Proyek

- Memiliki kode yang sederhana dan mudah dipahami.
- Dapat mengolah data kualitas udara dari file CSV.
- Menghasilkan ringkasan statistik secara otomatis.
- Menampilkan grafik untuk membantu analisis data.
- Memiliki mekanisme peringatan berdasarkan ambang simulasi.

## Kesimpulan

Proyek ini menerapkan Python untuk memantau dan menganalisis data simulasi kualitas udara PM2.5. Program mampu membaca dataset, menghitung rata-rata, memeriksa nilai terhadap ambang simulasi, serta menampilkan grafik perubahan konsentrasi berdasarkan waktu.

Proyek ini menjadi contoh penerapan analisis data untuk pemantauan lingkungan dan dapat dikembangkan lebih lanjut melalui integrasi sensor IoT, prediksi berbasis Machine Learning, serta pemrosesan data berskala besar menggunakan HPC.