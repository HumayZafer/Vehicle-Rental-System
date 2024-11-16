class vehicle:
    def __init__(self, vehicle_id, make, model, year, rental_rate):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.is_available = True

    def display_vehicle_details(self):