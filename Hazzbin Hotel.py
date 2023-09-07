import datetime

#Habitaciones disponibles del Hotel Hazzbin"
rooms = {
    "floor_1": {"single1": True, "single2": True, "single3": True, "single4": True, "single5": True},
    "floor_2": {"single6": True, "single7": True, "single8": True, "single9": True, "single10": True},
    "floor_3": {"double1": True, "double2": True, "double3": True, "double4": True, "double5": True},
    "floor_4": {"double6": True, "double7": True, "double8": True, "double9": True, "double10": True},
    "floor_5": {"luxury1": True, "luxury2": True, "luxury3": True, "luxury4": True, "luxury5": True}
}

#Verificación de disponibilidad de habitación
def disponibility(floor, type_room):
    return rooms[floor].get(type_room, False)

def validating_dates(initial_date, final_date):
    today = datetime.date.today()
    limit = today + datetime.timedelta(days=60)
    if initial_date < today:
        return "The initial date must be equal or after today"
    if final_date <= initial_date:
        return "The final date must be after the initial date"
    if final_date > limit:
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
if len(name) < 1:
    name = "Antonio Wilson"

phonenum = input("Phone Number: ")
if len(phonenum) < 1:
    phonenum = "555-123-2658"

email = input("Email: ")
if len(email) < 1:
    email = "elcacas@hazbin.com"

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
floor = None

#Reservación de la habitación
rooms[floor][type_room] = False

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

#register_reservation()