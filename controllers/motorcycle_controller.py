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