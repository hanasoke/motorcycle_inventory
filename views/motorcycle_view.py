class MotorcycleView:  
    def show_all(self, data):
        print("\n=== MOTORCYCLE DATA ===")
        for m in data: 
            print(f"{m.code} | {m.brand} {m.type} | Stock: {m.stock} | Price: {m.price}")
        
    def show_all(self, message):
        print(message)