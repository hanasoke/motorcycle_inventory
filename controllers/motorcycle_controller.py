from models.motorcycle import Motorcycle 

class MotorcycleController: 
    def __init__(self, model, view):
        self.model = model 
        self.view = view 
        
    def add_motorcycle(self): 
        code = input("Motocycle Code: ")
        brand = input("Brand: ")
        type = input("Type: ")
        stock = int(input("Stock: "))
        price = float(input("Price: "))
        
        motorcycle = Motorcycle(code, brand, type, stock, price)
        self.model.add(motorcycle)
        self.view.show_message("The Motorcycle has been added!")
        
    def show_motorcycle(self): 
        code = input("The Motorcycle Code has been deleted: ")
        m = self.model.search(code)
        if m: 
            self.model.delete(m)
            self.view.show_message("deleted successfully!")
    
    def show_motorcycle(self): 
        data = self.model.all()
        self.view.show_all(data)
        
    def delete_motorcycle(self): 
        code = input("The Motor Code want to be deleted: ")
        m = self.model.search(code)
        if m: 
            self.model.delete(m)
            self.view.show_message("Deleted Successfully!")
        else:
            self.view.show_message("No Found This Motorcycle!")