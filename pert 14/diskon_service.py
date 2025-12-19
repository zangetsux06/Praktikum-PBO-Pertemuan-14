# diskon_service.py
import pdb

class DiskonCalculator:
    """Service untuk menghitung potongan harga."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # pdb.set_trace() # Debugger dimatikan karena kode sudah fix
        
        # Rumus yang BENAR (Dibagi 100)
        jumlah_diskon = (harga_awal * persentase_diskon) / 100
        
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir

if __name__ == '__main__':
    calc = DiskonCalculator()
    # Test manual
    print(f"Hasil: {calc.hitung_diskon(1000, 10)}")