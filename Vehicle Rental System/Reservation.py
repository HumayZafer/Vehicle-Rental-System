from datetime import datetime
from Customer import Customer
from Vehicles import Car
class reservation:
    _reservation ={}

    def __init__(self, reservation_id, customer, vehicle, reservation_date, status="pending"):
        self.reservation_id = reservation_id
        self.customer = customer
        self.vehicle = vehicle
        self.reservation_date = reservation_date
        self.status= status

    @classmethod

    def make_reservation(cls, reservation_id, customer, vehicle, reservation_date):
        # create a resrvation
        if not vehicle.is_available:
            print(f"Vehicle {vehicle.vehicle_id} is not available for reservation.")
            return None
        #check for duplicate reservation
        if reservation_id in cls._reservation:
            print(f"Reservation ID {reservation_id} already exists.")
            return reservation
    @classmethod

    def cancel_reservation(cls, reservation_id):
        if reservation_id not in cls._reservation:
            print(f"Reservation ID {reservation_id} not found")
            return None

        reservation = cls._reservation[reservation_id]
        reservation.status = 'Canceled'
        reservation.vehicle.is_available = True
        print(f"Reservation {reservation_id} not found.")
        return reservation
    @classmethod

    def display_reservation_details(cls, reservation_id):
        if reservation_id not in cls._reservation:
            print(f"Reservation ID {reservation_id} not found.")
            return None

        reservation = cls._reservation[reservation_id]
        print(f"Reservation ID: {reservation.reservation_id}")
        print(f"Customer Name: {reservation.customer.get_name()}")
        print(f"Vehicle ID: {reservation.vehicle.vehicle_id}")
        print(f"Vehicle Make: {reservation.vehicle.make}")
        print(f"Reservation Date: {reservation.reservation_date}")
        print(f"Status: {reservation.status}")


#Example
customer1 = Customer.sign_up("Ethan Carter", "Ethan@gmail.com", "password123")
car1 = Car("C001", "Toyota", "Corolla", 2020, 50, "Sedan", 4)


reservation1 = reservation.make_reservation("R001", customer1, car1, datetime.now())
reservation.display_reservation_details("R001")
reservation.cancel_reservation("R001")
reservation.display_reservation_details("R001")