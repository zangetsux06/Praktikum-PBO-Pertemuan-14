# test_diskon.py
import unittest
from diskon_service import DiskonCalculator

class TestDiskonCalculator(unittest.TestCase):
    
    def setUp(self):
        """Persiapan: Dijalankan sebelum setiap test case."""
        self.calc = DiskonCalculator()

    def test_diskon_standar_10_persen(self):
        """Tes 1: Diskon 10% dari 1000 harus 900."""
        hasil = self.calc.hitung_diskon(1000, 10)
        self.assertEqual(hasil, 900.0)

    def test_diskon_nol(self):
        """Tes 2 (Boundary): Diskon 0% harga tidak berubah."""
        hasil = self.calc.hitung_diskon(500, 0)
        self.assertEqual(hasil, 500.0)

    def test_diskon_batas_atas(self):
        """Tes 3 (Boundary): Diskon 100% jadi gratis (0)."""
        hasil = self.calc.hitung_diskon(750, 100)
        self.assertEqual(hasil, 0.0)

    def test_input_negatif(self):
        """Tes 4: Input diskon negatif, harga tidak boleh turun."""
        hasil = self.calc.hitung_diskon(500, -5)
        self.assertGreaterEqual(hasil, 500)

    # --- TUGAS MANDIRI (ADVANCED TEST) ---
    def test_diskon_float(self):
        """Tes 5: Diskon pecahan (33% dari 999)."""
        # 999 * 0.33 = 329.67. Harga akhir = 669.33
        hasil = self.calc.hitung_diskon(999, 33)
        # Gunakan AlmostEqual untuk koma-komaan
        self.assertAlmostEqual(hasil, 669.33, places=2)

    def test_harga_nol(self):
        """Tes 6 (Edge Case): Harga awal 0, hasil tetap 0."""
        hasil = self.calc.hitung_diskon(0, 50)
        self.assertEqual(hasil, 0.0)


        


if __name__ == '__main__':
    unittest.main()