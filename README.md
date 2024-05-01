# PA-A23-KELOMPOK 5

## Anggota Kelompok
### 1. Adinda Salsabilla Naura (2309116023)
### 2. Nova Nur Fauziah (2309116043)
### 3. Khalil Pradipta Lee (2309116046)

## Deskripsi Program
Aplikasi yang dibuat sebagai tempat untuk mempermudah masyarakat mengetahui dan juga melakukan tindakan untuk lingkungan di darat terkhusus di Kalimantan Timur. aplikasi ini meliputi informasi dan juga tempat pelaporan mengenai keadaan ekosistem darat di Kalimantan Timur.

## Import Library
### import pwinput : 
Modul ini digunakan untuk mengambil input dari pengguna tanpa menampilkan input tersebut di layar. Biasanya digunakan untuk menerima kata sandi atau informasi sensitif lainnya tanpa menampilkan karakter apa pun saat pengguna mengetikkannya.
### import os : 
Modul ini menyediakan fungsi-fungsi untuk berinteraksi dengan sistem operasi yang terkait dengan Python. Kita dapat menggunakan modul ini untuk melakukan berbagai tugas, seperti mengelola direktori, mengakses variabel lingkungan, dan menjalankan perintah sistem.
### from prettytable import prettytable :  
Library ini digunakan untuk membuat tabel yang rapi dan terstruktur di konsol. Kita dapat menggunakan modul ini untuk membuat tabel dalam kode Python dan menampilkannya dengan format yang bagus di konsol.
### import mysql.connector : 
Modul ini adalah konektor MySQL resmi untuk Python. Ini memungkinkan Python berinteraksi dengan database MySQL, seperti membuat kueri, mengubah data, atau melakukan operasi lainnya pada database.
### import random : 
Modul ini memberikan fungsionalitas untuk menghasilkan bilangan acak.
### import time : 
Modul ini menyediakan fungsi-fungsi untuk bekerja dengan waktu dalam Python. Kita dapat menggunakan modul ini untuk mengukur waktu eksekusi program, membuat jeda dalam eksekusi, atau melakukan operasi lain yang terkait dengan waktu.

## Fitur
Beberapa fitur yang terdapat dalam program meliputi :
### User :
1. Read : User dapat membaca isi dari database tertentu seperti ekosistem darat, spesies hewan, spesies tumbuhan
2. Create Laporan : User dapat membuat sebuah laporan

### Admin :
1. Create : Admin dapat membuat isi dari database yang meliputi seluruhnya kecuali membuat laporan
2. Read : Admin dapat melihat semua isi database
3. Update : Admin dapat melakukan pembaruan pada isi database
4. Delete : Admin dapat melakukan penghapusan isi database tertentu
5. Sort : Admin dapat melakukan sorting pada database untuk merapikan isinya dengan mengurutkan id mereka
6. Search : Admin dapat melakukan pencarian dengan search keyword dari nama suatu databasenya yang terdaftar

## Cara Penggunaan
1. Saat program dimulai, program akan menampilkan menu utama yang terdiri atas 3 menu, yaitu 1) login, 2) daftar, 3) keluar.
2. Pilih daftar untuk mendaftarkan akun user
3. Masukkan nama, password (wajib 10 angka/huruf), nomor telepon (wajib 12 angka)
4. Anda akan dikembalikan ke menu login, kemudian pilih login
5. Masukkan nama dan password yang telah dibuat tadi
6. Setelah login berhasil, akan ditampilkan menu Read Ekosistem Darat, Read Spesies Hewan, Read Spesies Tumbuhan, Create Laporan dan Delete
7. Keluar/Logout jika sudah selesai


   
## Dokumentasi Menu
```
==================================================
‖                    MENU LOGIN                  ‖
==================================================
| 1. Login user                                  |
| 2. Login admin                                 |
| 3. Buat Akun                                   |
| 0. Keluar                                      |
==================================================
Pilih menu:
```

```
==================================================
‖                    MENU USER                   ‖
==================================================
| 1. Baca Ekosistem Darat                        |
| 2. Baca Spesies Hewan                          |
| 3. Baca Spesies Tumbuhan                       |
| 4. Membuat Laporan                             |
| 5. Kembali ke Menu Awal                        |
==================================================
Pilih menu:
```

```
==================================================
‖                     MENU ADMIN                 ‖
==================================================
| 1. Ekosistem Darat                             |
| 2. Spesies Hewan                               |
| 3. Spesies Tumbuhan                            |
| 4. Laporan                                     |
| 5. User                                        |
| 6. Admin                                       |
| 7. Kembali ke Menu Sebelumnya                  |
==================================================
Pilih menu:
```
