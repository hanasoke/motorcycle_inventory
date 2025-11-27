from models.motor import Motor

class MotorController: 
    def __init__(self, model, view):
        self.model = model 
        self.view = view 
        
    def tambah_motor(self): 
        kode = input("Kode Motor: ")
        merek = input("Merek: ")
        tipe = input("Tipe: ")
        stok = int(input("Stok: "))
        harga = float(input("Harga: "))
        
        motor = Motor(kode, merek, tipe, stok, harga)
        self.model.tambah(motor)
        self.view.tampilkan_pesan("Motor berhasil ditambahkan!")
        
    def tampilkan_motor(self):
        data = self.model.semua()
        self.view.tampilkan_semua(data)
        
    def hapus_motor(self): 
        kode = input("Kode motor yang dihapus: ")
        m = self.model.cari(kode)
        if m: 
            self.model.hapus(m)
            self.view.tampilkan_pesan("Berhasil dihapus!")
        else: 
            self.view.tampilkan_pesan("Motor tidak ditemukan!")