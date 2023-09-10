import datetime

#Listas de las habitaciones por piso
rooms_available_single1 = ["single1", "single2", "single3", "single4", "single5"]
rooms_available_single2 = ["single6", "single7", "single8", "single9", "single10"]
rooms_available_double1 = ["double1", "double2", "double3", "double4", "double5"]
rooms_available_double2 = ["double6", "double7", "double8", "double9", "double10"]
rooms_available_luxury = ["luxury1", "luxury2", "luxury3", "luxury4", "luxury5"]

rooms_reserved_single1 = []
rooms_reserved_single2 = []
rooms_reserved_double1 = []
rooms_reserved_double2 = []
rooms_reserved_luxury = []

#lista de reservaciones
list_reservations = []

#funciones de cliente y reservacion
class Client:
    def __init__(self, name, phonenum, email):
        self.name = name
        self.phonenum = phonenum
        self.email = email

class Reservation:
    def __init__(self, client, initial_date, final_date, type_room, num_room):
        self.client = client
        self.initial_date = initial_date
        self.final_date = final_date
        self.type_room = type_room
        self.num_room = num_room

#Función para validación de fechas segun condiciones
def validating_dates(initial_date, final_date):
    today = datetime.date.today()
    limit = today + datetime.timedelta(days=60)
    if initial_date < today:
        return "The initial date must be equal or after today"
    if final_date <= initial_date:
        return "The final date must be after the initial date"
    if final_date > limit:
        return "You can't make a reservation within more than 60 days of anticipation"
    
while True:
    #Entradas de datos del cliente
    print("Welcome to Hazzbin Hotel reservation system,")
    print("please fill the fields correctly.")

    name = input("Full name: (or write done to finish) ")
    if name == "done":                 #para terminar el loop
        break
    phonenum = input("Phone Number: ")
    email = input("Email: ")
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
    if type_room == "done":
        break
    type_room = type_room.lower()

#Código para modificar listas de las habitaciones sencillas
    if type_room == "single":
        print("Rooms Available:\nFloor 1: ", rooms_available_single1, "\nFloor 2: ", rooms_available_single2)
        num_room = input("Please, write the room you want to reserve: ")
        if num_room == "done":
            break
        if num_room in rooms_available_single1:
            rooms_reserved_single1.append(num_room)
            rooms_reserved_single1.sort()
            rooms_available_single1.remove(num_room)
        if num_room in rooms_available_single2:
            rooms_reserved_single2.append(num_room)
            rooms_reserved_single2.sort()
            rooms_available_single2.remove(num_room)
        else:
            print("This room is unavailable, please choose another room")

#Código para modificar listas de las habitaciones dobles    
    if type_room == "double":
        print("Rooms Available:\nFloor 3: ", rooms_available_double1, "\nFloor 4: ", rooms_available_double2)
        num_room = input("Please, write the room you want to reserve: ")
        if num_room == "done":
            break
        if num_room in rooms_available_double1:
            rooms_reserved_double1.append(num_room)
            rooms_reserved_double1.sort()
            rooms_available_double1.remove(num_room)
        if num_room in rooms_available_double2:
            rooms_reserved_double2.append(num_room)
            rooms_reserved_double2.sort()
            rooms_available_double2.remove(num_room)
        else:
            print("This room is unavailable, please choose another room")
            continue

#Código para modificar la lista de las habitaciones de lujo
    if type_room == "luxury":
        print("Rooms Available:\nFloor 5: ", rooms_available_luxury)
        num_room = input("Please, write the room you want to reserve: ")
        if num_room == "done":
            break
        if num_room in rooms_available_luxury:
            rooms_reserved_luxury.append(num_room)
            rooms_reserved_luxury.sort()
            rooms_available_luxury.remove(num_room)
        else:
            print("This room is unavailable, please choose another room")
    else:
        print("please write the type room correctly")
        continue
    
    reservation = Reservation(Client(name, phonenum, email), initial_date, final_date, type_room, num_room)
    list_reservations.append(reservation)

    print("\nReservation succesfully!\n")

print("\nRooms available: ")
print("Floor 1:", rooms_available_single1)
print("Floor 2:", rooms_available_single2)
print("Floor 3:", rooms_available_double1)
print("Floor 4:", rooms_available_double2)
print("Floor 5:", rooms_available_luxury, "\n")

print("Rooms Occupied: ")
print("Floor 1:", rooms_reserved_single1)
print("Floor 2:", rooms_reserved_single2)
print("Floor 3:", rooms_reserved_double1)
print("Floor 4:", rooms_reserved_double2)
print("Floor 5:", rooms_reserved_luxury, "\n")

#OOP Cliente y  su reservación en Hazzbin Hotel
guest = Client(name, phonenum, email)
guest_reservation = Reservation(guest.name, initial_date, final_date, type_room, num_room)
    
#Mensaje de confirmación con datos del cliente
print("Reservations:")
for reservation in list_reservations:
    print(f"Client: {reservation.client.name}")
    print(f"Phone number: {reservation.client.phonenum}")
    print(f"Email: {reservation.client.email}")
    print(f"Initial date: {reservation.initial_date}")
    print(f"Final date: {reservation.final_date}")
    print(f"Reserved room: {reservation.type_room} in the {reservation.num_room}")
    print("------------")
