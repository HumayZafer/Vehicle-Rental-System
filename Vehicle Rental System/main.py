import datetime
from Customer import Customer
from Vehicles import VehicleRentalSystem, Car, motorcycle
from Customer_Manager import Customermanager
from Reservation import reservation
from Transaction import Transaction, Epay, Invoice, Cash


def main():
    system = VehicleRentalSystem()
    customer_manager = Customermanager(name="", email="", password="")  # Temporary
    customer = None

    # Adding some sample vehicles
    system.add_vehicle(
        Car(vehicle_id=1, make="Toyota", model="Corolla", year=2020, rental_rate=50, car_type="Sedan", num_doors=4))
    system.add_vehicle(
        Car(vehicle_id=2, make="Honda", model="Civic", year=2019, rental_rate=55, car_type="Sedan", num_doors=4))
    system.add_vehicle(
        motorcycle(vehicle_id=3, make="Yamaha", model="YZF-R3", year=2021, rental_rate=40, engine_capacity="321cc",
                   type_of_bike="Sports"))
    system.add_vehicle(motorcycle(vehicle_id=4, make="Harley-Davidson", model="Street 750", year=2018, rental_rate=60,
                                  engine_capacity="750cc", type_of_bike="Cruiser"))

    while True:
        print("\n--- Vehicle Rental System ---")
        print("1. Sign Up")
        print("2. Login")
        print("3. View Available Vehicles")
        print("4. Rent a Vehicle")
        print("5. Make a Reservation")
        print("6. Cancel a Reservation")
        print("7. Apply for Discount and Get Summary")
        print("8. Exit")

        choice = input("Please select an option (1-8): ")

        if choice == "1":
            # Sign up a new customer
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            contact_number = input("Enter your contact number (optional): ")
            driving_license = input("Enter your driving license number (optional): ")
            cnic = input("Enter your CNIC number (optional): ")

            customer = Customer.sign_up(name, email, password, contact_number, driving_license, cnic)

        elif choice == "2":
            # Login a customer
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer = Customer.login(email, password)
            if customer:
                print(f"Welcome back, {customer.get_name()}!")

        elif choice == "3":
            # View available vehicles
            system.display_available_vehicle()

        elif choice == "4":
            # Rent a vehicle
            if customer:
                vehicle_id = int(input("Enter the vehicle ID you want to rent: "))
                days = int(input("Enter the number of rental days: "))
                system.rent_vehicle(customer, vehicle_id, days)
            else:
                print("Please log in first to rent a vehicle.")

        elif choice == "5":
            # Make a reservation
            if customer:
                vehicle_id = int(input("Enter vehicle ID for reservation: "))
                reservation_id = input("Enter reservation ID: ")
                reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
                reservation_date = datetime.datetime.strptime(reservation_date, "%Y-%m-%d")

                # Find the vehicle by ID
                vehicle = None
                for v in system.vehicles:
                    if v.vehicle_id == vehicle_id:
                        vehicle = v
                        break

                if vehicle:
                    reservation.make_reservation(reservation_id, customer, vehicle, reservation_date)
                else:
                    print("Invalid vehicle ID.")
            else:
                print("Please log in first to make a reservation.")

        elif choice == "6":
            # Cancel a reservation
            if customer:
                reservation_id = input("Enter reservation ID to cancel: ")
                reservation.cancel_reservation(reservation_id)
            else:
                print("Please log in first to cancel a reservation.")

        elif choice == "7":
            # Apply discounts and get summary
            if customer:
                customer_manager.assign_random_discount()
                total_cost = float(input("Enter the total rental cost: "))
                customer_manager.earn_loyalty_points(total_cost)
                customer_manager.get_total_discount()

                payment_choice = input("Choose payment method: (1) Epay, (2) Cash, (3) Invoice: ")
                if payment_choice == "1":
                    debit_credit = input("Enter Debit/Credit: ")
                    card_number = input("Enter card number: ")
                    expiration_date = input("Enter expiration date (MM/YY): ")
                    epay_transaction = Epay(customer, vehicle, days, total_cost, debit_credit, card_number,
                                            expiration_date)
                    epay_transaction.process_payment()

                elif payment_choice == "2":
                    cash_transaction = Cash(customer, vehicle, days, total_cost)
                    cash_transaction.process_payment()

                elif payment_choice == "3":
                    email_address = input("Enter your email address for the invoice: ")
                    invoice_transaction = Invoice(customer, vehicle, days, total_cost, email_address)
                    invoice_transaction.send_invoice()

        elif choice == "8":
            # Exit
            print("Thank you for using the Vehicle Rental System!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
