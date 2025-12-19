# Laporan Debugging (Tugas Mandiri)

**Nama:** Andi Reza  
**NIM:** 2411102441164

## 1. Skenario Bug (Simulasi)
Sesuai instruksi tugas mandiri, saya sengaja menambahkan logika PPN 10% (`* 1.1`) pada baris akhir perhitungan. Akibatnya, Unit Test `test_diskon_standar_10_persen` mengalami kegagalan (Fail).

## 2. Temuan Error
- **Ekspektasi (Harapan):** 900.0
- **Aktual (Kenyataan):** 990.0000000000001
- **Analisis Awal:** Ada selisih sekitar 90 poin (10% dari harga setelah diskon).

## 3. Proses Debugging (Penelusuran)
Saya menggunakan `pdb.set_trace()` untuk memeriksa nilai variabel saat *runtime*:

1. **Cek Harga Awal:**
   (Pdb) p harga_awal
   1000

2. **Cek Jumlah Diskon:**
   (Pdb) p jumlah_diskon
   100.0
   *(Nilai ini benar, berarti rumus diskon sudah aman)*.

3. **Cek Harga Sebelum Return:**
   (Pdb) p harga_awal - jumlah_diskon
   900.0
   *(Seharusnya ini hasil akhirnya)*.

4. **Cek Harga Akhir (Variable Return):**
   (Pdb) p harga_akhir
   990.0000000000001
   *(DITEMUKAN: Nilai berubah menjadi lebih besar)*.

## 4. Kesimpulan & Perbaikan
**Akar Masalah:** Ditemukan operasi perkalian `* 1.1` pada baris `harga_akhir` yang menyebabkan nilai bertambah 10% (PPN tidak sengaja terhitung).

**Solusi:** Menghapus `* 1.1` dari rumus agar perhitungan kembali murni diskon saja.
