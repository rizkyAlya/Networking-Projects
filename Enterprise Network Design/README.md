# Enterprise Network Design – Proyek Jaringan Netlab Corp

## Deskripsi Proyek
Proyek ini merupakan implementasi jaringan untuk **Netlab Corp**, perusahaan di bidang pendidikan dengan 3 cabang: **Jakarta (pusat), Singapura, dan Nusantara**. Tujuan dari proyek ini adalah membangun infrastruktur jaringan yang aman, terstruktur, dan efisien untuk mendukung komunikasi internal, akses server, dan manajemen cabang secara terpadu.

---

## Struktur Perusahaan dan Jumlah Pegawai
Setiap cabang memiliki **4 divisi**: Research and Development, Finance, Telco, dan Engineer. Jumlah pegawai adalah sebagai berikut:

| Cabang       | R&D        | Finance     | Telco       | Engineer    |
|--------------|------------|-------------|-------------|-------------|
| Jakarta      | 48         | 576         | 64          | 240         |
| Singapura    | 32         | 48          | 48          | 64          |
| Nusantara    | 16         | 32          | 37          | 43          |

---

## Infrastruktur Jaringan

### Server
- **Web Server:** Jakarta
- **DNS Server:** Jakarta
- **Email Server:** Singapura

### Koneksi Antar Cabang
- Menggunakan **routing antar cabang** (metode EIGRP)
- Memastikan komunikasi antar cabang lancar dan aman

### VLAN & InterVLAN
- Setiap divisi di setiap cabang memiliki VLAN masing-masing
- Implementasi **InterVLAN routing** untuk komunikasi antar divisi

### IP Addressing
- Menggunakan **DHCP IPv4** (ditempatkan di Jakarta)
- Jumlah maksimal perangkat yang dapat terhubung disesuaikan dengan jumlah pegawai tiap divisi

### Redundansi & Optimasi
- **STP (Spanning Tree Protocol)** untuk mencegah loop
- **EtherChannel** untuk agregasi link dan meningkatkan bandwidth antar switch

---

## Tujuan Implementasi
1. Memastikan setiap anggota divisi dapat berkomunikasi tanpa hambatan
2. Mendukung akses ke server internal dan eksternal
3. Menjaga keamanan dan efisiensi jaringan
4. Mengoptimalkan penggunaan bandwidth melalui EtherChannel dan STP
5. Mengimplementasikan manajemen IP otomatis dengan DHCP

---

## Topologi Jaringan
<img width="2409" height="1599" alt="image" src="https://github.com/user-attachments/assets/17df659d-2c61-4539-a31b-077291c79cde" />

