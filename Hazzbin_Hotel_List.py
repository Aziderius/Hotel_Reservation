import datetime

#Listas de las habitaciones por piso
rooms_available_single1 = []
rooms_available_single2 = []
rooms_available_double1 = []
rooms_available_double2 = []
rooms_available_luxury = []

# Diccionario para mapear los tipos de habitación a las listas correspondientes
room_lists = {
    "single": [rooms_available_single1, rooms_available_single2],
    "double": [rooms_available_double1, rooms_available_double2],
    "luxury": [rooms_available_luxury]
}

#lista de reservaciones
list_reservations = []

#funciones de cliente y reservacion
class Client:
    def __init__(self, name, phonenum, email):
        self.name = name
        self.phonenum = phonenum
        self.email = email

class Reservation:
    def __init__(self, client, initial_date, final_date, type_room, num_room, floor):
        self.client = client
        self.initial_date = initial_date
        self.final_date = final_date
        self.type_room = type_room
        self.num_room = num_room
        self.floor = floor

#Función para validación de fechas segun condiciones
def validating_dates(initial_date, final_date):
    today = datetime.date.today()
    if initial_date < today:
        return "The initial date must be after today"
    if final_date <= initial_date:
        return "The final date must be after the initial date"
    if (final_date - initial_date).days > 60:
        return "You can't make a reservation with more than 60 days in advance"
    
while True:
    #Entradas de datos del cliente
    print("Welcome to Hazzbin Hotel reservation system,")
    print("please fill the fields correctly.")

    name = input("Full name: (or write done to finish) ").upper()
    if name == "DONE":                 #para terminar el loop
        break
    if any(reservation.client.name.upper() == name.upper() for reservation in list_reservations):
        print("\nThis name is already registered.\n")
        continue

    phonenum = input("Phone Number: ")
    try:
        phonenum = int(phonenum)
    except:
        print("please enter your phone number correctly")
        continue
    if any(reservation.client.phonenum == phonenum for reservation in list_reservations):
        print("\nThis phone number is already registered.\n")
        continue

    email = input("Email: ")
    if any(reservation.client.email == email for reservation in list_reservations):
        print("\nThis email is already registered.\n")
        continue

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

    date_validation_result = validating_dates(initial_date, final_date)
    if date_validation_result:
        print(date_validation_result)
        continue

    type_room = input("Type of room (single, double, luxury): ")
    type_room = type_room.lower()

    if type_room in room_lists:
        room_list = room_lists[type_room]
        if all(len(rooms) >= 5 for rooms in room_list):
            print("\nThere's no more rooms available for this type.\nPlease choose another room type\n")
            continue
        for rooms in room_list:
            if len(rooms) < 5:
                num_room = f"{type_room}{len(rooms) + 1}"
                rooms.append(num_room)
                break 
    else:
        print("please write the type room correctly")
        continue

    if num_room in rooms_available_single1:
        floor = "Floor 1"
    elif num_room in rooms_available_single2:
        floor = "Floor 2"
    elif num_room in rooms_available_double1:
        floor = "Floor 3"
    elif num_room in rooms_available_double2:
        floor = "Floor 4"
    elif num_room in rooms_available_luxury:
        floor = "Floor 5"
    
    reservation = Reservation(Client(name, phonenum, email), initial_date, final_date, type_room, num_room, floor)
    list_reservations.append(reservation)

    print("\nReservation succesfully!\n")

print("\nRooms reserved: ")
print("Floor 1:", rooms_available_single1)
print("Floor 2:", rooms_available_single2)
print("Floor 3:", rooms_available_double1)
print("Floor 4:", rooms_available_double2)
print("Floor 5:", rooms_available_luxury, "\n")

#Mensaje de confirmación con datos del cliente
print("Reservations:")
for reservation in list_reservations:
    print(f"Client: {reservation.client.name}")
    print(f"Phone number: {reservation.client.phonenum}")
    print(f"Email: {reservation.client.email}")
    print(f"Initial date: {reservation.initial_date}")
    print(f"Final date: {reservation.final_date}")
    print(f"Reserved room: {reservation.num_room} on {reservation.floor}")
    print("------------")
