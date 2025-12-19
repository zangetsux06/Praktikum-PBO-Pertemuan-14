# diskon_service.py
import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""
    
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Nyalakan debugger di sini untuk mengecek (opsional)
        # pdb.set_trace() 
        
 
        jumlah_diskon = harga_awal * persentase_diskon
        
        harga_akhir = harga_awal - jumlah_diskon
        
        return harga_akhir

# --- UJI COBA (Main Program) ---
if __name__ == '__main__':
    calc = DiskonCalculator()
    
    # Skenario: Harga 1000, Diskon 10%
    # Harapan: 900
    # Realita (karena Bug): Minus 9000
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil: {hasil}")