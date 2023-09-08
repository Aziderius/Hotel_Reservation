import datetime

#Habitaciones disponibles del Hotel Hazzbin"
rooms = {
    "floor1": {"single1": True, "single2": True, "single3": True, "single4": True, "single5": True},
    "floor2": {"single6": True, "single7": True, "single8": True, "single9": True, "single10": True},
    "floor3": {"double1": True, "double2": True, "double3": True, "double4": True, "double5": True},
    "floor4": {"double6": True, "double7": True, "double8": True, "double9": True, "double10": True},
    "floor5": {"luxury1": True, "luxury2": True, "luxury3": True, "luxury4": True, "luxury5": True}
}

#Funcion de Verificación de disponibilidad de habitación


#Función para validación de fechas segun condiciones
def validating_dates(initial_date, final_date):
    today = datetime.date.today()
    limit = today + datetime.timedelta(days=60)
    if initial_date < today:
        return "The initial date must be equal or after today"
    if final_date <= initial_date:
        return "The final date must be after the initial date"
    if initial_date > limit:
        return "You can't make a reservation within more than 60 days of anticipation"
    
class Client:
    def __init__(self, name, phonenum, email):
        self.name = name
        self.phonenum = phonenum
        self.email = email

class Reservation:
    def __init__(self,client, initial_date, final_date, type_room,):
        self.client = client
        self.initial_date = initial_date
        self.final_date = final_date
        self.type_room = type_room

#Entradas de datos del cliente
print("Welcome to Hazzbin Hotel reservation system,")
print("please fill the fields correctly.")

name = input("Full name: ")
if len(name) < 1:                  #solo para test
    name = "Antonio Wilson"        #solo para test

phonenum = input("Phone Number: ")
if len(phonenum) < 1:              #solo para test
    phonenum = "555-123-2658"      #solo para test

email = input("Email: ")
if len(email) < 1:                 #solo para test
    email = "elcacas@hazbin.com"   #solo para test

initial_date = input("Initial reservation date (YYYY-MM-DD): ")
try:
    initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d').date()
except ValueError:
    print("Invalid Input. Please use 'YYYY-MM-DD' format.")
    quit()

final_date = input("Final reservation date (YYYY-MM-DD): ")
try:
    final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d').date()
except ValueError:
    print("Invalid Input. Please use 'YYYY-MM-DD' format.")
    quit()

type_room = input("Type of room (single, double, luxury): ")
type_room = type_room.lower() 

#validating dates
dates = validating_dates(initial_date, final_date)

#rooms disponibility
# Mapeo de tipos de habitaciones a pisos
room_floor_mapping = {
    "single": "floor2",
    "single": "floor1",
    "double": "floor4",
    "double": "floor3",
    "luxury": "floor5"
}

# Verifica si el tipo de habitación proporcionado es válido
if type_room in room_floor_mapping:
    floor = room_floor_mapping[type_room]

    # Busca una habitación disponible en el piso y cambia su valor a False
    for room_to_change, value in rooms[floor].items():
        if value:
            rooms[floor][room_to_change] = False
            found_room = True
            print(f"\nThe room {room_to_change} on the {floor} is now reserved.")
            break

    if not found_room:
        print(f"There is not rooms in this {floor}.")
else:
    print("please, write correctly the type room you want (single, double, luxury).")

#OOP Cliente y  su reservación en Hazzbin Hotel
guest = Client(name, phonenum, email)
guest_reservation = Reservation(guest.name, initial_date, final_date, type_room)

#Mensaje de confirmación con datos del cliente
print(f"\nReservation complete!")
print(f"Host Name: {guest.name}")
print(f"Phone number: {guest.phonenum}")
print(f"Email: {guest.email}")
print(f"Initial date: {guest_reservation.initial_date}")
print(f"Final date: {guest_reservation.final_date}")
print(f"Reserved room: {type_room} in the {floor}")
print("Thanks to join us in Hazzbin Hotel!")