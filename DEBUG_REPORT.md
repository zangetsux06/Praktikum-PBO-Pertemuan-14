Masalah: Test case test_diskon_standar gagal. Ekspektasi 900.0, tetapi Output aktual 990.0.

Penelusuran (Trace): Menggunakan perintah p (print) pada debugger pdb:

p harga_awal -> 1000

p jumlah_diskon -> 100.0 (Benar)

p harga_awal - jumlah_diskon -> 900.0 (Benar)

p harga_akhir -> 990.0 (SALAH)

Analisis: Ternyata ada operasi perkalian * 1.1 di baris return yang menyebabkan hasil akhir bertambah 10%.

Tindakan: Menghapus pengali * 1.1 tersebut agar kode kembali valid.
