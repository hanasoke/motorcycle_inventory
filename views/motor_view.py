class MotorView:  
    def tampilkan_semua(self, data):
        print("\n=== DATA MOTOR ===")
        for m in data: 
            print(f"{m.kode} | {m.merk} {m.tipe} | Stok: {m.stok} | Harga: {m.harga}")
        
    def tampilkan_pesan(self, pesan):
        print(pesan)