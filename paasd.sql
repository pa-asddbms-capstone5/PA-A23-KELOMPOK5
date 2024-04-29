-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 08 Apr 2024 pada 10.33
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `si_ekodarat`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `nama_admin` varchar(50) NOT NULL,
  `password` char(10) NOT NULL,
  `no_telpon` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id_admin`, `nama_admin`, `password`, `no_telpon`) VALUES
(1, 'Khalil Pradipta Lee', 'khalil7788', '081234567890'),
(2, 'Adinda Salsabilla Naura', 'naura12345', '081234567891'),
(3, 'Nova Nur Fauziah', 'Nova123456', '081234567892'),
(4, 'Muhammad Imam Farizy', 'Imam123456', '081234567893');

-- --------------------------------------------------------

--
-- Struktur dari tabel `ekosistem_darat`
--

CREATE TABLE `ekosistem_darat` (
  `id_ekosistem` int(11) NOT NULL,
  `nama_ekosistem` varchar(50) NOT NULL,
  `id_admin` int(11) NOT NULL,
  `lokasi_geografis` varchar(100) DEFAULT NULL,
  `status_ekosistem` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `ekosistem_darat`
--

INSERT INTO `ekosistem_darat` (`id_ekosistem`, `nama_ekosistem`, `id_admin`, `lokasi_geografis`, `status_ekosistem`) VALUES
(1, 'Ekosistem Hutan Primer', 1, 'Taman Nasional Kutai dan Kayan Mentarang dan Gunung Soeharto dan Gunung Lumut', 'sangat rentan'),
(2, 'Ekosistem Hutan Dataran Rendah', 2, 'Berau dan Taman Nasional Kutai', 'cukup signifikan'),
(3, 'Ekosistem Mangrove', 3, 'Kawasan Delta Mahakam', 'rentan'),
(4, 'Ekosistem Padang Lamun', 4, 'wilayah pesisir Kalimantan Timur', 'rentan'),
(5, 'Ekosistem Lahan Basah', 1, 'Kecamatan Muara Ancalong', 'rentan'),
(6, 'Ekosistem Kerangas', 2, 'Cagar Alam Kersik Luway', 'cukup signifikan'),
(7, 'Ekosistem Gambut', 3, 'Kutai Kartanegara dan sebagian kecil Kutai Timur', 'rentan'),
(8, 'Ekosistem Sabana', 4, 'Kabupaten Kutai Timur', 'cukup normal'),
(9, 'Ekosistem Hutan Sekunder', 1, 'Hampir semua bagian Kalimantan Timur', 'cukup terancam'),
(10, 'Ekosistem Hutan Riparian', 2, 'Sungai Mahakam dan sungai-sungai kecil di Kalimantan Timur', 'sedikit rentan');

-- --------------------------------------------------------

--
-- Struktur dari tabel `laporan`
--

CREATE TABLE `laporan` (
  `id_laporan` int(11) NOT NULL,
  `isi_laporan` varchar(255) DEFAULT 'Tidak ada informasi laporan',
  `id_user` int(11) NOT NULL,
  `id_admin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `laporan`
--

INSERT INTO `laporan` (`id_laporan`, `isi_laporan`, `id_user`, `id_admin`) VALUES
(1, 'Pencemaran limbah industri di sungai menyebabkan kematian ikan dan kerusakan ekosistem hutan sekitar.', 1, 3),
(2, 'Penebangan liar di hutan menyebabkan kerusakan habitat satwa liar.', 2, 2),
(3, 'Sungai tercemar oleh limbah domestik dan industri, menyebabkan air tidak layak untuk konsumsi.', 3, 4),
(4, 'Pembakaran sampah di hutan mengakibatkan pencemaran udara dan kerusakan lingkungan.', 4, 1),
(5, 'Penggunaan pestisida yang berlebihan menyebabkan kontaminasi tanah dan air di sekitar hutan.', 5, 3),
(6, 'Sungai tercemar oleh limbah pertanian yang mengandung pestisida dan pupuk kimia.', 6, 2),
(7, 'Illegal logging di hutan menyebabkan hilangnya keanekaragaman hayati dan kerusakan ekosistem.', 7, 4),
(8, 'Kebakaran hutan akibat pembakaran lahan untuk perluasan pertanian.', 8, 1),
(9, 'Pencemaran sungai oleh limbah pertambangan menyebabkan berkurangnya populasi ikan.', 9, 3),
(10, 'Penggunaan bahan bakar fosil yang berlebihan menyebabkan polusi udara di sekitar hutan.', 10, 2),
(11, 'Penambangan emas ilegal di hutan mengakibatkan kerusakan lingkungan dan pencemaran air.', 11, 4),
(12, 'Pembangunan infrastruktur di hutan merusak habitat satwa liar dan ekosistem alam.', 12, 1),
(13, 'Penggunaan pupuk dan pestisida kimia di hutan merusak kesuburan tanah dan kualitas air.', 13, 3),
(14, 'Penangkapan ikan secara berlebihan di sungai menyebabkan penurunan populasi ikan.', 14, 2),
(15, 'Pembuangan limbah industri ke sungai mengakibatkan kematian ikan dan kerusakan ekosistem sungai.', 15, 4),
(16, 'Pembalakan liar di hutan menyebabkan hilangnya habitat bagi berbagai jenis satwa liar.', 16, 1),
(17, 'Pencemaran limbah pertanian di sungai mengakibatkan eutrofikasi dan matinya biota air.', 17, 3),
(18, 'Illegal mining di hutan menyebabkan kerusakan lingkungan dan pencemaran air sungai.', 18, 2),
(19, 'Pembuangan sampah plastik di sungai mengakibatkan pencemaran air dan bahaya bagi satwa air.', 19, 4),
(20, 'Pembakaran lahan untuk perkebunan kelapa sawit mengakibatkan hilangnya habitat bagi satwa hutan.', 20, 1),
(21, 'Pencemaran sungai oleh limbah industri menyebabkan berkurangnya ketersediaan air bersih.', 21, 3),
(22, 'Illegal logging di hutan menyebabkan hilangnya keanekaragaman hayati dan kerusakan lingkungan.', 22, 2),
(23, 'Penggunaan pestisida yang berlebihan menyebabkan keracunan tanah dan air di sekitar hutan.', 23, 4),
(24, 'Pembalakan liar di hutan menyebabkan berkurangnya habitat bagi berbagai jenis satwa liar.', 24, 1),
(25, 'Penebangan hutan untuk pembangunan infrastruktur merusak ekosistem dan mengancam keanekaragaman hayati.', 25, 3),
(26, 'Illegal mining di hutan menyebabkan kerusakan lingkungan dan pencemaran air sungai.', 26, 2),
(27, 'Pembuangan limbah industri ke sungai mengakibatkan kematian ikan dan kerusakan ekosistem sungai.', 27, 4),
(28, 'Pembakaran lahan untuk perkebunan kelapa sawit mengakibatkan hilangnya habitat bagi satwa hutan.', 28, 1),
(29, 'Pencemaran sungai oleh limbah industri menyebabkan berkurangnya ketersediaan air bersih.', 29, 3),
(30, 'Illegal logging di hutan menyebabkan hilangnya keanekaragaman hayati dan kerusakan lingkungan.', 30, 2),
(31, 'Penggunaan pestisida yang berlebihan menyebabkan keracunan tanah dan air di sekitar hutan.', 31, 4),
(32, 'Pembalakan liar di hutan menyebabkan berkurangnya habitat bagi berbagai jenis satwa liar.', 32, 1),
(33, 'Penebangan hutan untuk pembangunan infrastruktur merusak ekosistem dan mengancam keanekaragaman hayati.', 33, 3),
(34, 'Illegal mining di hutan menyebabkan kerusakan lingkungan dan pencemaran air sungai.', 34, 2),
(35, 'Pembuangan limbah industri ke sungai mengakibatkan kematian ikan dan kerusakan ekosistem sungai.', 35, 4),
(36, 'Pembakaran lahan untuk perkebunan kelapa sawit mengakibatkan hilangnya habitat bagi satwa hutan.', 36, 1),
(37, 'Pencemaran sungai oleh limbah industri menyebabkan berkurangnya ketersediaan air bersih.', 37, 3),
(38, 'Illegal logging di hutan menyebabkan hilangnya keanekaragaman hayati dan kerusakan lingkungan.', 38, 2),
(39, 'Penggunaan pestisida yang berlebihan menyebabkan keracunan tanah dan air di sekitar hutan.', 39, 4),
(40, 'Pembalakan liar di hutan menyebabkan berkurangnya habitat bagi berbagai jenis satwa liar.', 40, 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `spesies_hewan`
--

CREATE TABLE `spesies_hewan` (
  `id_hewan` int(11) NOT NULL,
  `nama_hewan` varchar(50) NOT NULL,
  `id_ekosistem` int(11) NOT NULL,
  `status_populasi` varchar(50) NOT NULL,
  `status_perlindungan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `spesies_hewan`
--

INSERT INTO `spesies_hewan` (`id_hewan`, `nama_hewan`, `id_ekosistem`, `status_populasi`, `status_perlindungan`) VALUES
(1, 'Alap-alap capung', 4, 'Resiko Rendah', 'Dilindungi'),
(2, 'Baza Jerdon', 9, 'Resiko Rendah', 'Dilindungi'),
(3, 'Elang tikus', 8, 'Resiko Rendah', 'Dilindungi'),
(4, 'Elang Bondol', 10, 'Resiko Rendah', 'Dilindungi'),
(5, 'elang brontok', 9, 'Resiko Rendah', 'Dilindungi'),
(6, 'elang hitam', 9, 'Resiko Rendah', 'Dilindungi'),
(7, 'elang-alap jambul', 9, 'Resiko Rendah', 'Dilindungi'),
(8, 'elang-ikan kecil', 9, 'Mendekati Ancaman', 'Dilindungi'),
(9, 'elang-ular bido', 2, 'Resiko Rendah', 'Dilindungi'),
(10, 'pecuk-ular asia', 2, 'Mendekati Ancaman', 'Dilindungi'),
(11, 'bambangan coklat', 2, 'Resiko Rendah', 'Dilindungi'),
(12, 'cangak laut', 3, 'Resiko Rendah', 'Dilindungi'),
(13, 'kuntul besar', 2, 'Resiko Rendah', 'Dilindungi'),
(14, 'julang emas', 2, 'Resiko Rendah', 'Dilindungi'),
(15, 'kangkareng hitam', 2, 'Mendekati Ancaman', 'Dilindungi'),
(16, 'kangkareng perut-putih', 2, 'Resiko Rendah', 'Dilindungi'),
(17, 'rangkong badak', 2, 'Mendekati Ancaman', 'Dilindungi'),
(18, 'takur tutut', 2, 'Mendekati Ancaman', 'Dilindungi'),
(19, 'cica daun besar', 2, 'Terancam', 'Dilindungi'),
(20, 'bangau tongtong', 2, 'Rentan', 'Dilindungi'),
(21, 'tangkar kambing', 3, 'Resiko Rendah', 'Dilindungi'),
(22, 'burung madu sepah raja', 2, 'Resiko Rendah', 'Dilindungi'),
(23, 'betet ekor panjang', 2, 'Rentan', 'Dilindungi'),
(24, 'serindit melayu', 2, 'Resiko Rendah', 'Dilindungi'),
(25, 'kipasan belang', 9, 'Resiko Rendah', 'Dilindungi'),
(26, 'tiong emas', 2, 'Resiko Rendah', 'Dilindungi'),
(27, 'orangutan', 1, 'Kritis', 'Dilindungi'),
(28, 'bekantan', 10, 'Terancam Punah', 'Dilindungi'),
(29, 'beruang madu', 1, 'Rentan', 'Dilindungi'),
(30, 'kijang muntjak', 1, 'Resiko Rendah', 'Dilindungi'),
(31, 'kucing kuwuk', 2, 'Resiko Rendah', 'Dilindungi'),
(32, 'macan dahan', 1, 'Rentan', 'Dilindungi'),
(33, 'owa kalawat', 1, 'Terancam', 'Dilindungi'),
(34, 'pelanduk napu', 2, 'Resiko Rendah', 'Dilindungi'),
(35, 'rusa sambar', 9, 'Rentan', 'Dilindungi'),
(36, 'cipoh jantung', 2, 'Mendekati Ancaman', 'Tidak Dilindungi'),
(37, 'kadalan beruang', 1, 'Mendekati Ancaman', 'Tidak Dilindungi'),
(38, 'pentis kumbang', 2, 'Mendekati Ancaman', 'Tidak Dilindungi'),
(39, 'sempur hujan darat', 1, 'Mendekati Ancaman', 'Tidak Dilindungi'),
(40, 'takut topi emas', 1, 'Mendekati Ancaman', 'Tidak Dilindungi');

-- --------------------------------------------------------

--
-- Struktur dari tabel `spesies_tumbuhan`
--

CREATE TABLE `spesies_tumbuhan` (
  `id_tumbuhan` int(11) NOT NULL,
  `nama_tumbuhan` varchar(50) NOT NULL,
  `id_ekosistem` int(11) NOT NULL,
  `status_populasi` varchar(50) NOT NULL,
  `status_perlindungan` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `spesies_tumbuhan`
--

INSERT INTO `spesies_tumbuhan` (`id_tumbuhan`, `nama_tumbuhan`, `id_ekosistem`, `status_populasi`, `status_perlindungan`) VALUES
(1, 'Keruing', 1, 'Terancam', 'Tidak dilindungi'),
(2, 'Pasang', 2, 'Rentan', 'Tidak dilindungi'),
(3, 'Putat', 3, 'Rentan', 'Dilindungi'),
(4, 'Meranti merah', 4, 'Terancam', 'Dilindungi'),
(5, 'Pacar cina', 5, 'Resiko Rendah', 'Tidak dilindungi'),
(6, 'Medang', 6, 'Resiko Rendah', 'Tidak dilindungi'),
(7, 'Pulai', 7, 'Terancam', 'Dilindungi'),
(8, 'Terap', 8, 'Terancam', 'Dilindungi'),
(9, 'Merentanak', 9, 'Terancam', 'Tidak dilindungi'),
(10, 'Kenangan', 10, 'Resiko Rendah', 'Tidak dilindungi'),
(11, 'Kayu manis', 1, 'Terancam', 'Dilindungi'),
(12, 'Bangkirai', 2, 'Rentan', 'Dilindungi'),
(13, 'Bengkal', 3, 'Terancam', 'Tidak dilindungi'),
(14, 'Bungur', 4, 'Terancam', 'Tidak dilindungi'),
(15, 'Celangkap laki gunung', 5, 'Rentan', 'Dilindungi'),
(16, 'Darah-darah', 6, 'Kritis', 'Dilindungi'),
(17, 'Empopor', 7, 'Rentan', 'Tidak dilindungi'),
(18, 'Ganitri', 8, 'Kritis', 'Tidak dilindungi'),
(19, 'Ulin', 9, 'Rentan', 'Dilindungi'),
(20, 'Garung/warung', 10, 'Terancam', 'Tidak dilindungi'),
(21, 'Gemor', 1, 'Rentan', 'Tidak dilindungi'),
(22, 'Jelatang', 2, 'Terancam', 'Tidak dilindungi'),
(23, 'Jeranjang', 3, 'Rentan', 'Tidak dilindungi'),
(24, 'Kayu ara', 4, 'Mendekati Ancaman', 'Dilindungi'),
(25, 'Kayu gading', 5, 'Rentan', 'Tidak dilindungi'),
(26, 'Laban', 6, 'Mendekati Ancaman', 'Dilindungi'),
(27, 'Mahang', 7, 'Rentan', 'Tidak dilindungi'),
(28, 'Mentialing', 8, 'Terancam', 'Dilindungi'),
(29, 'Nyatoh', 9, 'Rentan', 'Tidak dilindungi'),
(30, 'Nyatu', 10, 'Terancam', 'Tidak dilindungi'),
(31, 'Pangal', 1, 'Terancam', 'Tidak dilindungi'),
(32, 'Pasak bumi', 2, 'Resiko Rendah', 'Dilindungi'),
(33, 'Rengas', 3, 'Terancam', 'Dilindungi'),
(34, 'Resak hiru', 4, 'Resiko Rendah', 'Tidak dilindungi'),
(35, 'Suren', 5, 'Terancam', 'Tidak dilindungi'),
(36, 'Renault', 6, 'Rentan', 'Tidak dilindungi'),
(37, 'Sungkai', 7, 'Terancam', 'Tidak dilindungi'),
(38, 'Tebaul', 8, 'Rentan', 'Tidak dilindungi'),
(39, 'Terap', 9, 'Kritis', 'Dilindungi'),
(40, 'Ketumbo', 10, 'Rentan', 'Tidak dilindungi');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `nama_user` varchar(50) NOT NULL,
  `password` char(10) NOT NULL,
  `no_telpon` char(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id_user`, `nama_user`, `password`, `no_telpon`) VALUES
(1, 'Andi', 'x3eR4dFs7T', '08123092347'),
(2, 'Budi', 'g6Ht2eKl8P', '08123857394'),
(3, 'Christy', 'n9Jk1pWs5A', '08123374568'),
(4, 'Herman', 'q4Vh6tLy2S', '08123948570'),
(5, 'Deni', 'w2Xe4rFs7D', '08123659874'),
(6, 'Erika', 'e5Rt2yGh9J', '08123746982'),
(7, 'Ferdi', 'r7Tg3Yh8K', '08123564792'),
(8, 'Gita', 't9Uj5Iu4O', '08123874563'),
(9, 'Hani', 'y2Ik8Ol3P', '08123234578'),
(10, 'Joko', 'u1Ad4Fg7H', '08123456789'),
(11, 'Kiki', 'i3Sk6Dl9Q', '08123948562'),
(12, 'Lina', 'o8Dg2Hk5J', '08123849562'),
(13, 'Mira', 'p9Jl1Ks5D', '08123458796'),
(14, 'Nana', 'a2Sd5Fg8H', '08123549682'),
(15, 'Oka', 's3Df6Gh9J', '08123649758'),
(16, 'Putri', 'd4Fg2Hj5K', '08123895746'),
(17, 'Roni', 'f5Gh4Jk7L', '08123956482'),
(18, 'Sari', 'h6Jk8Lm3N', '08123659482'),
(19, 'Toni', 'j7Kl9Mn4B', '08123456789'),
(20, 'Vina', 'k8Lm1Mn5B', '08123945876'),
(21, 'Wati', 'l9Mn2Bo6P', '08123849563'),
(22, 'Yudi', 'z3Cx4Vb7N', '08123659748'),
(23, 'Zara', 'x2Cv5Bn8M', '08123467589'),
(24, 'Rina', 'c6Vb3Nm2K', '08123957682'),
(25, 'Bambang', 'v7Bn4Mc1L', '08123845967'),
(26, 'Dewi', 'b3Nc5Xv8C', '08123659487'),
(27, 'Fani', 'n4Xv6Zc9V', '08123849563'),
(28, 'Gandi', 'm5Zx7Zv1B', '08123958674'),
(29, 'Hesti', 'x8Bv9Cn2M', '08123849562'),
(30, 'Indra', 'd9Cm1Xz4V', '08123845793'),
(31, 'Joni', 'z3Vb5Nm7L', '08123659748'),
(32, 'Kartika', 'x4Bn6Mc9K', '08123467589'),
(33, 'Lani', 'c7Mn8Xz1L', '08123845967'),
(34, 'Mona', 'v9Nc1Bv2C', '08123659487'),
(35, 'Niko', 'b1Xz3Vc5X', '08123849563'),
(36, 'Opik', 'n3Mv4Bx6Z', '08123958674'),
(37, 'Putu', 'm4Nv5Cx7Z', '08123849562'),
(38, 'Rudy', 'b5Mc6Bv8X', '08123845793'),
(39, 'Susi', 'v6Nm7Bn9M', '08123659748'),
(40, 'Tuti', 'c8Bv9Mn1N', '08123467589');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`),
  ADD KEY `idx_id_admin` (`id_admin`);

--
-- Indeks untuk tabel `ekosistem_darat`
--
ALTER TABLE `ekosistem_darat`
  ADD PRIMARY KEY (`id_ekosistem`),
  ADD KEY `id_admin` (`id_admin`),
  ADD KEY `idx_id_ekosistem` (`id_ekosistem`);

--
-- Indeks untuk tabel `laporan`
--
ALTER TABLE `laporan`
  ADD PRIMARY KEY (`id_laporan`),
  ADD KEY `idx_id_laporan` (`id_laporan`),
  ADD KEY `fk_user_id` (`id_user`),
  ADD KEY `fk_admin_id` (`id_admin`);

--
-- Indeks untuk tabel `spesies_hewan`
--
ALTER TABLE `spesies_hewan`
  ADD PRIMARY KEY (`id_hewan`),
  ADD KEY `id_ekosistem` (`id_ekosistem`),
  ADD KEY `idx_id_hewan` (`id_hewan`);

--
-- Indeks untuk tabel `spesies_tumbuhan`
--
ALTER TABLE `spesies_tumbuhan`
  ADD PRIMARY KEY (`id_tumbuhan`),
  ADD KEY `id_ekosistem` (`id_ekosistem`),
  ADD KEY `idx_id_tumbuhan` (`id_tumbuhan`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `idx_id_user` (`id_user`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `laporan`
--
ALTER TABLE `laporan`
  MODIFY `id_laporan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `ekosistem_darat`
--
ALTER TABLE `ekosistem_darat`
  ADD CONSTRAINT `ekosistem_darat_ibfk_1` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`);

--
-- Ketidakleluasaan untuk tabel `laporan`
--
ALTER TABLE `laporan`
  ADD CONSTRAINT `fk_admin_id` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`) ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_user_id` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON UPDATE CASCADE,
  ADD CONSTRAINT `laporan_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`),
  ADD CONSTRAINT `laporan_ibfk_2` FOREIGN KEY (`id_admin`) REFERENCES `admin` (`id_admin`);

--
-- Ketidakleluasaan untuk tabel `spesies_hewan`
--
ALTER TABLE `spesies_hewan`
  ADD CONSTRAINT `spesies_hewan_ibfk_1` FOREIGN KEY (`id_ekosistem`) REFERENCES `ekosistem_darat` (`id_ekosistem`);

--
-- Ketidakleluasaan untuk tabel `spesies_tumbuhan`
--
ALTER TABLE `spesies_tumbuhan`
  ADD CONSTRAINT `spesies_tumbuhan_ibfk_1` FOREIGN KEY (`id_ekosistem`) REFERENCES `ekosistem_darat` (`id_ekosistem`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
