from models.motorcycle_model import MotorcycleModel
from views.motorcycle_view import MotorcycleView
from controllers.motorcycle_controller import MotorcycleController

model = MotorcycleModel()
view = MotorcycleView()
controller = MotorcycleController(model, view)

while True: 
    print("""
1. Add Motorcycle 
2. View Motorcycle Inventory 
3. Delete Motorcycle 
4. Exit
""")
    choose = input("Choose Menu: ")
    if choose == "1":
        controller.add_motorcycle()
    elif choose == "2":
        controller.show_motorcycle()
    elif choose == "3":
        controller.delete_motorcycle()
    elif choose == "4":
        break