class MotorModel: 
    def __init__(self):
        self.data = []
        
    def tambah(self, motor):
        self.data.append(motor)
        
    def semua(self):
        return self.data 
    
    def cari(self, kode):
        for m in self.data: 
            if m.kode == kode: 
                return m 
        return None 
    
    def hapus(self, motor):
        self.data.remove(motor)