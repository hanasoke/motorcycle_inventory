class MotorcycleModel: 
    def __init__(self):
        self.data = []
        
    def add(self, motorcycle):
        self.data.append(motorcycle)
        
    def all(self):
        return self.data 
    
    def search(self, code):
        for m in self.data: 
            if m.code == code: 
                return m 
        return None 
    
    def delete(self, motorcycle):
        self.data.remove(motorcycle)