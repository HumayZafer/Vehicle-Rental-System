

from Customer import Customer


class vehicle:
    def __init__(self, vehicle_id, make, model, year, rental_rate):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.is_available = True

    def display_vehicle_details(self):
        print(f"Vehicle Id:{self.vehicle_id}")
        print(f"Make:{self.make}")
        print(f"Model:{self.model}")
        print(f"Year:{self.year}")
        print(f"Rental Rate: $(self.rental_rate)/day")
        print(f"Availabile:{'Available' if self.is_available else 'Rented'}")

    def calculate_rental_charges(self, days):
        return self.rental_rate * days

class Car(vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, car_type, num_doors):
        super().__init__(vehicle_id, make, model, year, rental_rate)
        self.car_type = car_type # example Suv, Sedan, Jeep
        self.num_doors = num_doors
    def display_vehicle_details(self):
        super().display_vehicle_details()
        print(f"Car Type:{self.car_type}")
        print(f"Number of Doors:{self.num_doors}")

class motorcycle(vehicle):
    def __init__(self, vehicle_id, make, model, year, rental_rate, engine_capacity, type_of_bike):
        super().__init__(vehicle_id, make, model, year, rental_rate)
        self.engine_capacity = engine_capacity
        self.type_of_bike = type_of_bike  #example sports, cruiser

    def display_vehicle_details(self):
        super().display_vehicle_details()
        print(f"Engine Capacity:{self.engine_capacity}")
        print(f"Type_of Bike:{self.type_of_bike}")

class VehicleRentalSystem:
    def __init__(self):
        self.vehicles = [] #list to store all vehicle
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_available_vehicle(self):
        print("Available Vehicle:")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                vehicle.display_vehicle_details()
                print("_" * 30)

    def rent_vehicle(self, customer, vehicle_id, days):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                rental_charges = vehicle.calculate_rental_charges(days)
                vehicle.is_available = False     # it mark the vehicle as rented
                rental_detail = {"vehicle_id": vehicle_id, "make": vehicle.make, "model": vehicle.model, "days": days, "charge": rental_charges}
                customer.add_rental_details(rental_detail)
                print(f"Vehicle {vehicle_id} rented successfully for ${rental_charges}.")
                return (
                    print(f"Vehicle {vehicle_id} is not available for rent."))


# Example
if __name__ == "__main__":
    # Sign-up, Log in customer
    customer1 = Customer.sign_up("Ethan Carter", "Ethan@gmail.com", "password123", "12345678", "DL123456", "CNIC12314352")
    logged_in_customer = Customer.login("Ethan@gmail.com", "password123")

    rental_system = VehicleRentalSystem()

    car1 = Car("C001", "Toyota", "Corolla", 2020, 50, "Sedan", "4")
    car2 = Car("C002", "Honda", "Civic",2021,60, "Sedan", "4")
    bike1 = motorcycle("M001", "Yamaha", "R15", 2019, 40, "1500cc", "Sports")
    bike2 = motorcycle("M002", "Harley Davidson", "Street 750", 2020, 80, "750cc", "Cruiser")

    rental_system.add_vehicle(car1)
    rental_system.add_vehicle(car2)
    rental_system.add_vehicle(bike1)
    rental_system.add_vehicle(bike2)

    rental_system.display_available_vehicle()
    if logged_in_customer:
        rental_system.rent_vehicle(logged_in_customer, "C001", 5)