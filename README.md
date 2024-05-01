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
### Tampilan Menu

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

### Tampilan Menu Read User & Create Laporan

```
==================================================
‖                   LOGIN USER                   ‖
==================================================

Masukkan nama user: Christy
Masukkan password: **********
```

```
+--------------+--------------------------------+----------+------------------------------------------+------------------+
| id_ekosistem |         nama_ekosistem         | id_admin |             lokasi_geografis             | status_ekosistem |
+--------------+--------------------------------+----------+------------------------------------------+------------------+
|      1       |     Ekosistem Hutan Primer     |    1     | Taman Nasional Kutai dan Kayan Mentarang |  sangat rentan   |
|              |                                |          |   dan Gunung Soeharto dan Gunung Lumut   |                  |
|      2       | Ekosistem Hutan Dataran Rendah |    2     |      Berau dan Taman Nasional Kutai      | cukup signifikan |
|      3       |       Ekosistem Mangrove       |    1     |          Kawasan Delta Mahakam           |   cukup rentan   |
|      4       |     Ekosistem Padang Lamun     |    4     |     wilayah pesisir Kalimantan Timur     |      rentan      |
|      5       |     Ekosistem Lahan Basah      |    1     |         Kecamatan Muara Ancalong         |      rentan      |
|      6       |       Ekosistem Kerangas       |    2     |         Cagar Alam Kersik Luway          | cukup signifikan |
|      7       |        Ekosistem Gambut        |    3     |   Kutai Kartanegara dan sebagian kecil   |      rentan      |
|              |                                |          |               Kutai Timur                |                  |
|      8       |        Ekosistem Sabana        |    4     |          Kabupaten Kutai Timur           |   cukup normal   |
|      9       |    Ekosistem Hutan Sekunder    |    1     |        Hampir semua bagian Kaltim        |   cukup rentan   |
|      10      |    Ekosistem Hutan Riparian    |    1     |  Sungai Mahakam dan sungai-sungai kecil  |  sedikit rentan  |
|              |                                |          |           di Kalimantan Timur            |                  |
|      20      |          adjawijdawjd          |    1     |                mcewmwemfd                |   awmdlawmlad    |
|      22      |             awdwa              |    1     |                 wwawdad                  |      adwad       |
+--------------+--------------------------------+----------+------------------------------------------+------------------+

Tekan Enter untuk kembali ke menu user...
```

```
+----------+------------------------+--------------+-------------------+---------------------+
| id_hewan |       nama_hewan       | id_ekosistem |  status_populasi  | status_perlindungan |
+----------+------------------------+--------------+-------------------+---------------------+
|    1     |    Alap-alap capung    |      2       |      Terancam     |   Tidak Dilindungi  |
|    2     |      Baza Jerdon       |      9       |   Resiko Rendah   |      Dilindungi     |
|    3     |      Elang tikus       |      8       |   Resiko Rendah   |      Dilindungi     |
|    4     |      Elang Bondol      |      10      |   Resiko Rendah   |      Dilindungi     |
|    5     |     elang brontok      |      9       |   Resiko Rendah   |      Dilindungi     |
|    6     |      elang hitam       |      9       |   Resiko Rendah   |      Dilindungi     |
|    7     |   elang-alap jambul    |      9       |   Resiko Rendah   |      Dilindungi     |
|    8     |    elang-ikan kecil    |      9       | Mendekati Ancaman |      Dilindungi     |
|    9     |    elang-ular bido     |      2       |   Resiko Rendah   |      Dilindungi     |
|    10    |    pecuk-ular asia     |      2       | Mendekati Ancaman |      Dilindungi     |
|    11    |    bambangan coklat    |      2       |   Resiko Rendah   |      Dilindungi     |
|    12    |      cangak laut       |      3       |   Resiko Rendah   |      Dilindungi     |
|    13    |      kuntul besar      |      2       |   Resiko Rendah   |      Dilindungi     |
|    14    |      julang emas       |      2       |   Resiko Rendah   |      Dilindungi     |
|    15    |    kangkareng hitam    |      2       | Mendekati Ancaman |      Dilindungi     |
|    16    | kangkareng perut-putih |      2       |   Resiko Rendah   |      Dilindungi     |
|    17    |     rangkong badak     |      2       | Mendekati Ancaman |      Dilindungi     |
|    18    |      takur tutut       |      2       | Mendekati Ancaman |      Dilindungi     |
|    19    |    cica daun besar     |      2       |      Terancam     |      Dilindungi     |
|    20    |    bangau tongtong     |      2       |       Rentan      |      Dilindungi     |
|    21    |    tangkar kambing     |      3       |   Resiko Rendah   |      Dilindungi     |
|    22    | burung madu sepah raja |      2       |   Resiko Rendah   |      Dilindungi     |
|    23    |   betet ekor panjang   |      2       |       Rentan      |      Dilindungi     |
|    24    |    serindit melayu     |      2       |   Resiko Rendah   |      Dilindungi     |
|    25    |     kipasan belang     |      9       |   Resiko Rendah   |      Dilindungi     |
|    26    |       tiong emas       |      2       |   Resiko Rendah   |      Dilindungi     |
|    27    |       orangutan        |      1       |       Kritis      |      Dilindungi     |
|    28    |        bekantan        |      10      |   Terancam Punah  |      Dilindungi     |
|    29    |      beruang madu      |      1       |       Rentan      |      Dilindungi     |
|    30    |     kijang muntjak     |      1       |   Resiko Rendah   |      Dilindungi     |
|    31    |      kucing kuwuk      |      2       |   Resiko Rendah   |      Dilindungi     |
|    32    |      macan dahan       |      1       |       Rentan      |      Dilindungi     |
|    33    |      owa kalawat       |      1       |      Terancam     |      Dilindungi     |
|    34    |     pelanduk napu      |      2       |   Resiko Rendah   |      Dilindungi     |
|    35    |      rusa sambar       |      9       |       Rentan      |      Dilindungi     |
|    36    |     cipoh jantung      |      2       | Mendekati Ancaman |   Tidak Dilindungi  |
|    37    |    kadalan beruang     |      1       | Mendekati Ancaman |   Tidak Dilindungi  |
|    38    |     pentis kumbang     |      2       | Mendekati Ancaman |   Tidak Dilindungi  |
|    39    |   sempur hujan darat   |      1       | Mendekati Ancaman |   Tidak Dilindungi  |
|    40    |    takut topi emas     |      1       | Mendekati Ancaman |   Tidak Dilindungi  |
|    52    |         HAHHA          |      2       |       awdad       |        wadadk       |
+----------+------------------------+--------------+-------------------+---------------------+

Tekan Enter untuk kembali ke menu user...
```

```
+-------------+-----------------------+--------------+-------------------+---------------------+
| id_tumbuhan |     nama_tumbuhan     | id_ekosistem |  status_populasi  | status_perlindungan |
+-------------+-----------------------+--------------+-------------------+---------------------+
|      1      |        Keruing        |      2       |      Terancam     |   Tidak dilindungi  |
|      2      |         Pasang        |      2       |       Rentan      |   Tidak dilindungi  |
|      3      |         Putat         |      3       |       Rentan      |      Dilindungi     |
|      4      |     Meranti merah     |      4       |      Terancam     |      Dilindungi     |
|      5      |       Pacar cina      |      5       |   Resiko Rendah   |   Tidak dilindungi  |
|      6      |         Medang        |      6       |   Resiko Rendah   |   Tidak dilindungi  |
|      7      |         Pulai         |      7       |      Terancam     |      Dilindungi     |
|      8      |         Terap         |      8       |      Terancam     |      Dilindungi     |
|      9      |       Merentanak      |      9       |      Terancam     |   Tidak dilindungi  |
|      10     |        Kenangan       |      10      |   Resiko Rendah   |   Tidak dilindungi  |
|      11     |       Kayu manis      |      1       |      Terancam     |      Dilindungi     |
|      12     |       Bangkirai       |      2       |       Rentan      |      Dilindungi     |
|      13     |        Bengkal        |      3       |      Terancam     |   Tidak dilindungi  |
|      14     |         Bungur        |      4       |      Terancam     |   Tidak dilindungi  |
|      15     | Celangkap laki gunung |      5       |       Rentan      |      Dilindungi     |
|      16     |      Darah-darah      |      6       |       Kritis      |      Dilindungi     |
|      17     |        Empopor        |      7       |       Rentan      |   Tidak dilindungi  |
|      18     |        Ganitri        |      8       |       Kritis      |   Tidak dilindungi  |
|      19     |          Ulin         |      9       |       Rentan      |      Dilindungi     |
|      20     |     Garung/warung     |      10      |      Terancam     |   Tidak dilindungi  |
|      21     |         Gemor         |      1       |       Rentan      |   Tidak dilindungi  |
|      22     |        Jelatang       |      2       |      Terancam     |   Tidak dilindungi  |
|      23     |       Jeranjang       |      3       |       Rentan      |   Tidak dilindungi  |
|      24     |        Kayu ara       |      4       | Mendekati Ancaman |      Dilindungi     |
|      25     |      Kayu gading      |      5       |       Rentan      |   Tidak dilindungi  |
|      26     |         Laban         |      6       | Mendekati Ancaman |      Dilindungi     |
|      27     |         Mahang        |      7       |       Rentan      |   Tidak dilindungi  |
|      28     |       Mentialing      |      8       |      Terancam     |      Dilindungi     |
|      29     |         Nyatoh        |      9       |       Rentan      |   Tidak dilindungi  |
|      30     |         Nyatu         |      10      |      Terancam     |   Tidak dilindungi  |
|      31     |         Pangal        |      1       |      Terancam     |   Tidak dilindungi  |
|      32     |       Pasak bumi      |      2       |   Resiko Rendah   |      Dilindungi     |
|      33     |         Rengas        |      3       |      Terancam     |      Dilindungi     |
|      34     |       Resak hiru      |      4       |   Resiko Rendah   |   Tidak dilindungi  |
|      35     |         Suren         |      5       |      Terancam     |   Tidak dilindungi  |
|      36     |        Renault        |      6       |       Rentan      |   Tidak dilindungi  |
|      37     |        Sungkai        |      7       |      Terancam     |   Tidak dilindungi  |
|      38     |         Tebaul        |      8       |       Rentan      |   Tidak dilindungi  |
|      39     |         Terap         |      9       |       Kritis      |      Dilindungi     |
|      40     |        Ketumbo        |      10      |       Rentan      |   Tidak dilindungi  |
|      42     |          sapi         |      5       |       takde       |         mama        |
+-------------+-----------------------+--------------+-------------------+---------------------+

Tekan Enter untuk kembali ke menu user...
```

```
==================================================
‖                  MEMBUAT LAPORAN               ‖
==================================================
Masukkan isi laporan Anda: Kebakaran Hutan Hebat       
Laporan berhasil dibuat, berikut isi laporannya.
Isi laporan: Kebakaran Hutan Hebat
ID User: 3
ID Admin: 5
|     -------------------------------------------------------------------       |
|                               PERINGATAN!!!                                   |
|     -------------------------------------------------------------------       |
|      Jika laporan anda tidak valid, admin dapat menghapus laporan anda        |
|     -------------------------------------------------------------------       |
Tekan Enter untuk kembali ke menu user...
```

### Tampilan Menu CRUD Admin & Sort Search

```
==================================================
‖                   LOGIN ADMIN                  ‖
==================================================

Masukkan nama admin: Khalil
Masukkan password: **********
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 1

Masukkan nama ekosistem: contoh hewan
Masukkan lokasi geografis: contoh lokasi
Masukkan status ekosistem: contoh status
|         -----------------------------------------------------       |
|          Berhasil Memasukan Data ke Database Ekosistem Darat        |
|         -----------------------------------------------------       |

Tekan Enter untuk kembali ke menu user...
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 2
+--------------+--------------------------------+----------+-------------------------------------------------------------------------------+------------------+
| id_ekosistem |         nama_ekosistem         | id_admin |                                lokasi_geografis                               | status_ekosistem |
+--------------+--------------------------------+----------+-------------------------------------------------------------------------------+------------------+
|      1       |     Ekosistem Hutan Primer     |    1     | Taman Nasional Kutai dan Kayan Mentarang dan Gunung Soeharto dan Gunung Lumut |  sangat rentan   |
|      2       | Ekosistem Hutan Dataran Rendah |    2     |                         Berau dan Taman Nasional Kutai                        | cukup signifikan |
|      3       |       Ekosistem Mangrove       |    1     |                             Kawasan Delta Mahakam                             |   cukup rentan   |
|      4       |     Ekosistem Padang Lamun     |    4     |                        wilayah pesisir Kalimantan Timur                       |      rentan      |
|      5       |     Ekosistem Lahan Basah      |    1     |                            Kecamatan Muara Ancalong                           |      rentan      |
|      6       |       Ekosistem Kerangas       |    2     |                            Cagar Alam Kersik Luway                            | cukup signifikan |   
|      7       |        Ekosistem Gambut        |    3     |                Kutai Kartanegara dan sebagian kecil Kutai Timur               |      rentan      |   
|      8       |        Ekosistem Sabana        |    4     |                             Kabupaten Kutai Timur                             |   cukup normal   |   
|      9       |    Ekosistem Hutan Sekunder    |    1     |                           Hampir semua bagian Kaltim                          |   cukup rentan   |   
|      10      |    Ekosistem Hutan Riparian    |    1     |           Sungai Mahakam dan sungai-sungai kecil di Kalimantan Timur          |  sedikit rentan  |   
|      20      |          adjawijdawjd          |    1     |                                   mcewmwemfd                                  |   awmdlawmlad    |   
|      22      |             awdwa              |    1     |                                    wwawdad                                    |      adwad       |   
|      23      |          contoh hewan          |    1     |                                 contoh lokasi                                 |  contoh status   |   
+--------------+--------------------------------+----------+-------------------------------------------------------------------------------+------------------+   

Tekan Enter untuk kembali ke menu admin...
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 3
Masukkan ID ekosistem darat yang akan diupdate: 23
Data yang akan diupdate:

+--------------+----------------+----------+------------------+------------------+
| id_ekosistem | nama_ekosistem | id_admin | lokasi_geografis | status_ekosistem |
+--------------+----------------+----------+------------------+------------------+
|      23      |  contoh hewan  |    1     |  contoh lokasi   |  contoh status   |
+--------------+----------------+----------+------------------+------------------+
Masukkan nama ekosistem baru (biarkan kosong jika tidak ingin mengubah): contoh fix
Masukkan lokasi geografis baru (biarkan kosong jika tidak ingin mengubah): lokasi baru
Masukkan status ekosistem baru (biarkan kosong jika tidak ingin mengubah): status baru
|        --------------------------------------------------------       |
|         Data Ekosistem Darat Berhasil Diperbarui Pada Database        |
|        --------------------------------------------------------       |

Tekan Enter untuk kembali ke menu admin...
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 4
Masukkan ID ekosistem darat yang ingin dihapus: 23
Data yang akan dihapus:

+--------------+----------------+----------+------------------+------------------+
| id_ekosistem | nama_ekosistem | id_admin | lokasi_geografis | status_ekosistem |
+--------------+----------------+----------+------------------+------------------+
|      23      |   contoh fix   |    1     |   lokasi baru    |   status baru    |
+--------------+----------------+----------+------------------+------------------+
Apakah Anda yakin ingin menghapus data ini? (y/n): y
Data berhasil dihapus dari tabel ekosistem darat.

Tekan Enter untuk kembali ke menu admin...
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 5
Masukkan urutan (asc/desc): desc
Data yang sudah diurutkan:
+--------------+--------------------------------+----------+------------------------------------------+------------------+
| id_ekosistem |         nama_ekosistem         | id_admin |             lokasi_geografis             | status_ekosistem |
+--------------+--------------------------------+----------+------------------------------------------+------------------+
|      23      |          contoh hewan          |    1     |              contoh lokasi               |  contoh status   |
|      22      |             awdwa              |    1     |                 wwawdad                  |      adwad       |
|      20      |          adjawijdawjd          |    1     |                mcewmwemfd                |   awmdlawmlad    |
|      10      |    Ekosistem Hutan Riparian    |    1     |  Sungai Mahakam dan sungai-sungai kecil  |  sedikit rentan  |
|              |                                |          |           di Kalimantan Timur            |                  |
|      9       |    Ekosistem Hutan Sekunder    |    1     |        Hampir semua bagian Kaltim        |   cukup rentan   |
|      8       |        Ekosistem Sabana        |    4     |          Kabupaten Kutai Timur           |   cukup normal   |
|      7       |        Ekosistem Gambut        |    3     |   Kutai Kartanegara dan sebagian kecil   |      rentan      |
|              |                                |          |               Kutai Timur                |                  |
|      6       |       Ekosistem Kerangas       |    2     |         Cagar Alam Kersik Luway          | cukup signifikan |
|      5       |     Ekosistem Lahan Basah      |    1     |         Kecamatan Muara Ancalong         |      rentan      |
|      4       |     Ekosistem Padang Lamun     |    4     |     wilayah pesisir Kalimantan Timur     |      rentan      |
|      3       |       Ekosistem Mangrove       |    1     |          Kawasan Delta Mahakam           |   cukup rentan   |
|      2       | Ekosistem Hutan Dataran Rendah |    2     |      Berau dan Taman Nasional Kutai      | cukup signifikan |
|      1       |     Ekosistem Hutan Primer     |    1     | Taman Nasional Kutai dan Kayan Mentarang |  sangat rentan   |
|              |                                |          |   dan Gunung Soeharto dan Gunung Lumut   |                  |
+--------------+--------------------------------+----------+------------------------------------------+------------------+

Tekan Enter untuk kembali ke menu admin...
```

```
==================================================
‖                MENU EKOSISTEM DARAT            ‖
==================================================
| 1. Create                                      |
| 2. Read                                        |
| 3. Update                                      |
| 4. Delete                                      |
| 5. Sort                                        |
| 6. Search                                      |
| 7. Kembali                                     |
==================================================
Pilih menu: 6
Masukkan nama ekosistem yang ingin dicari: mangrove
Data ditemukan:
+--------------+--------------------+----------+-----------------------+------------------+
| id_ekosistem |   nama_ekosistem   | id_admin |    lokasi_geografis   | status_ekosistem |
+--------------+--------------------+----------+-----------------------+------------------+
|      3       | Ekosistem Mangrove |    1     | Kawasan Delta Mahakam |   cukup rentan   |
+--------------+--------------------+----------+-----------------------+------------------+

Tekan Enter untuk kembali ke menu admin...
```


