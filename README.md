
# Pertemuan 12 - File I/O dan Error Handling

Nama: Ayu Syarifatu Zahra  
NIM: 2225250043  
Kelas: 3B

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python.

Program ini bertujuan untuk mengolah data nilai mahasiswa dari file teks, menghitung statistik nilai, menentukan jumlah mahasiswa yang lulus, serta menyimpan hasil rekap ke file output.

## Format File Input

File input disimpan dengan nama `data/nilai.txt`.

Setiap baris berisi NIM dan nilai mahasiswa yang dipisahkan menggunakan tanda koma.

Format:

```text
NIM,nilai
```

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Keterangan:
- `NIM`: Nomor Induk Mahasiswa.
- `nilai`: Nilai mahasiswa dalam bentuk angka.
- Setiap baris mewakili satu mahasiswa.
- Data dengan nilai tidak valid akan dilewati dan dilaporkan.
- Baris kosong akan dilewati.

## Cara Menjalankan

Buka terminal VS Code, kemudian jalankan:

```bash
python3 tugas/rekap_nilai_file.py
```

Jika menggunakan Windows:

```bash
python tugas/rekap_nilai_file.py
```

Pastikan file `data/nilai.txt` sudah tersedia sebelum menjalankan program.

## Algoritma

1. Menentukan path file input `data/nilai.txt`.
2. Menentukan path file output `data/hasil_rekap.txt`.
3. Membuka file input menggunakan mode baca dan encoding UTF-8.
4. Membaca isi file baris demi baris.
5. Menghapus spasi berlebih dan melewati baris kosong.
6. Memisahkan NIM dan nilai menggunakan tanda koma.
7. Mengonversi nilai menjadi tipe data `float`.
8. Jika nilai tidak valid, program mencatat atau melewati baris tersebut.
9. Menyimpan data valid dalam struktur data list.
10. Menghitung jumlah data valid.
11. Menghitung total nilai.
12. Menghitung rata-rata nilai.
13. Menentukan nilai minimum dan maksimum.
14. Menghitung jumlah mahasiswa dengan nilai minimal 60 sebagai lulus.
15. Menulis hasil rekap ke file `data/hasil_rekap.txt`.
16. Menampilkan ringkasan proses pada terminal.

## Error Handling

Program menggunakan penanganan kesalahan agar tetap berjalan dengan baik.

### 1. FileNotFoundError

Terjadi ketika file `data/nilai.txt` tidak ditemukan.

Penanganan:
- Menggunakan blok `try-except`.
- Menampilkan pesan bahwa file tidak ditemukan.
- Program tidak berhenti akibat traceback yang tidak ditangani.

### 2. ValueError

Terjadi ketika data nilai tidak dapat dikonversi menjadi angka.

Contoh:

```text
A004,abc
```

Penanganan:
- Menggunakan `try-except ValueError`.
- Melewati data yang tidak valid.
- Melanjutkan proses pada baris berikutnya.

## Test Case

| No | Kasus | Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Normal | Semua baris valid | Semua record diproses dan rekap benar | Belum diuji | Belum diuji |
| 2 | File hilang | nilai.txt tidak tersedia | Pesan file tidak ditemukan, program tidak crash | Belum diuji | Belum diuji |
| 3 | Nilai invalid | A004,abc | Baris invalid dilewati/dilaporkan, record lain tetap diproses | Belum diuji | Belum diuji |
| 4 | Baris kosong | Ada baris kosong | Baris kosong dilewati | Belum diuji | Belum diuji |
| 5 | Batas lulus | Nilai 60 | Dihitung sebagai lulus | Belum diuji | Belum diuji |

## Hasil Rekap
Hasil perhitungan:

| Statistik | Hasil |
|---|---|
| Jumlah data valid | 5 |
| Jumlah data invalid | 1 |
| Total nilai | 417 |
| Rata-rata nilai | 83.40 |
| Nilai minimum | 74 |
| Nilai maksimum | 92 |
| Jumlah mahasiswa lulus | 5 |
| Jumlah mahasiswa tidak lulus | 0 |

Contoh isi file `hasil_rekap.txt`:

```text
=== HASIL REKAP NILAI MAHASISWA ===

Jumlah data valid       : 5
Jumlah data invalid     : 1
Total nilai             : 417
Rata-rata nilai         : 83.40
Nilai minimum           : 74
Nilai maksimum          : 92
Jumlah mahasiswa lulus  : 5
Jumlah tidak lulus      : 0

Batas kelulusan         : 60
```

## Refleksi

Salah satu kesalahan yang dapat ditemukan dalam pengolahan file adalah ketika program mencoba mengubah data teks menjadi angka, tetapi terdapat nilai yang tidak sesuai dengan format numerik.

Contohnya adalah data `A004,abc`. Nilai `abc` tidak dapat dikonversi menjadi tipe data `float` sehingga dapat menyebabkan `ValueError`.

Cara memperbaikinya adalah menggunakan `try-except ValueError` agar program dapat melewati data yang tidak valid dan melanjutkan proses pengolahan data lainnya.

Selain itu, jika file input tidak ditemukan, program dapat mengalami `FileNotFoundError`. Masalah ini dapat ditangani menggunakan `try-except FileNotFoundError` sehingga program menampilkan pesan kesalahan yang jelas.

Melalui tugas ini, saya memahami pentingnya validasi data dan error handling agar program dapat mengolah file secara lebih aman dan terstruktur.

## Kesimpulan

Pada pertemuan 12, saya mempelajari penggunaan File I/O dan Error Handling dalam Python.

Program digunakan untuk membaca data mahasiswa dari file teks, memvalidasi nilai, menghitung statistik, menentukan kelulusan, dan menyimpan hasil rekap ke file output.

Penggunaan `try-except` membantu program menangani kesalahan seperti `FileNotFoundError` dan `ValueError` sehingga proses pengolahan data menjadi lebih baik.
