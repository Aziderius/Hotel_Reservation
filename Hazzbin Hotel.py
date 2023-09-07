import datetime

#Habitaciones disponibles del Hotel Hazzbin"
rooms = {
    "floor_1": {"single1": True, "single2": True, "single3": True, "single4": True, "single5": True},
    "floor_2": {"single6": True, "single7": True, "single8": True, "single9": True, "single10": True},
    "floor_3": {"doble1": True, "doble2": True, "doble3": True, "doble4": True, "doble5": True},
    "floor_4": {"doble6": True, "doble7": True, "doble8": True, "doble9": True, "doble10": True},
    "floor_5": {"luxury1": True, "luxury2": True, "luxury3": True, "luxury4": True, "luxury5": True}
}

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

def register_reservation():
    print("Welcome to Hazzbin Hotel reservation system,")
    print("please fill the fields correctly.")

    Client.name = input("Full name: ")
    Reservation.client = Client.name
    Client.phonenum = input("Phone Number: ")
    Client.email = input("Email: ")

    Reservation.initial_date = input("Initial reservation date (YYYY-MM-DD): ")
    try:
        initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d').date()
    except ValueError:
        return False, "Invalid Input. Please use 'YYYY-MM-DD' format."
     
    Reservation.final_date = input("Final reservation date (YYYY-MM-DD): ")
    try:
        final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d').date()
    except ValueError:
        return False, "Invalid Input. Please use 'YYYY-MM-DD' format."
    
    Reservation.type_room = input("Type of room (single, doble, luxury): ")

print(f"Reservation complete!")
print(f"Host Name: {Client.name}")
print(f"Phone number: {Client.phonenum}")
print(f"Email: {Client.email}")
print(f"Initial date: {Reservation.initial_date}")
print(f"Final date: {Reservation.final_date}")
print(f"Reserved room: {type_room} in the floor {floor}")
print("Thanks to join us in Hazzbin Hotel!")

register_reservation()