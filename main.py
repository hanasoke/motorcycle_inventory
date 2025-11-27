from models.motor_model import MotorModel
from views.motor_view import MotorView
from controllers.motor_controller import MotorController

model = MotorModel()
view = MotorView()
controller = MotorController(model, view)

while True: 
    print("""
1. Tambah Motor
2. Lihat Inventory 
3. Hapus Motor
4. Keluar
""")
    pilih = input("Pilih Menu: ")
    if pilih == "1":
        controller.tambah_motor()
    elif pilih == "2":
        controller.tampilkan_motor()
    elif pilih == "3":
        controller.hapus_motor()
    elif pilih == "4":
        break