# 📊 Kalkulator Metode Biseksi


## 👥 Anggota Kelompok 5
1. Andre Alfaridzi-2408107010011
2. Muhammad Riyadh-2408107010015
3. Hani Huriyah Ahmad-2408107010020
4. Meurahmah Nushsharie-2408107010035
5. U’rfan-2408107010038


Sebuah program Python sederhana untuk mencari akar persamaan menggunakan metode biseksi (bisection method).

## 🔄 Alur Program

### 1️⃣ User Input
- Pengguna memasukkan persamaan matematika
- Menentukan nilai batas bawah (a) dan batas atas (b)
- Menentukan toleransi error (e)
- Menentukan jumlah maksimum iterasi (N)

### 2️⃣ Validasi Input
- Program melakukan pemeriksaan validitas data input
- Memastikan format persamaan benar dan dapat diproses
- Memeriksa apakah interval [a,b] valid untuk metode biseksi

### 3️⃣ Proses Perhitungan
- Menghitung titik tengah interval
- Melakukan update interval berdasarkan teorema biseksi
- Proses iterasi berlanjut hingga mencapai konvergensi

### 4️⃣ Tampilan Hasil
Menampilkan tabel iterasi yang berisi:
- Nilai a dan b (interval)
- Nilai x (titik tengah)
- Nilai f(a), f(b), dan f(x)
- Error pada setiap langkah

### 5️⃣ Pesan Akhir
- Menampilkan akar hampiran jika metode konvergen
- Menampilkan pesan peringatan jika metode tidak konvergen

## ⭐ Keunggulan Program

### 1. Tampilan Interaktif
- Pengguna bisa langsung memasukkan persamaan, nilai a, b, toleransi, dan jumlah iterasi melalui kolom input
- Interface yang user-friendly dan mudah dipahami

### 2. Perhitungan Otomatis dan Akurat
- Program secara otomatis menghitung nilai akar hampiran
- Menampilkan hasil setiap iterasi secara cepat dan tepat
- Tingkat akurasi yang tinggi dalam perhitungan

### 3. Validasi dan Penanganan Error Otomatis
- Program menampilkan pesan otomatis saat terjadi kesalahan input
- Validasi format persamaan secara otomatis
- Peringatan jika hasil belum konvergen sesuai toleransi

### 4. Tabel Hasil Iterasi Lengkap
- Setiap langkah perhitungan ditampilkan dalam tabel
- Memudahkan pengguna memahami proses metode biseksi
- Tampilan hasil yang terstruktur dan informatif

## 🛠️ Teknologi yang Digunakan
- Python 3.13.7
- Library matematika Python
- Lbirary sympy
- Library PyQt5


## 📝 Cara Penggunaan
1. Pastikan Python sudah terinstall di komputer anda
2. Clone repository ini
3. Jalankan file `main.py`
4. Ikuti instruksi yang muncul di layar

## 🎯 Fitur
- Input persamaan yang fleksibel
- Visualisasi proses iterasi
- Deteksi konvergensi otomatis
- Perhitungan error yang akurat

## ⚠️ Batasan
- Metode biseksi hanya bekerja jika ada perubahan tanda pada interval [a,b]
- Konvergensi bergantung pada pemilihan interval awal yang tepat

 

 
 
 


 
