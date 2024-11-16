class Customer:

    _customers = {}

    def __init__(self, name, email, password, contact_number =None,driving_license =None, cnic =None):
        self.name = name
        self.email = email
        self.password = password
        self.contact_number = contact_number
        self.driving_license = driving_license
        self.cnic = cnic
        self.rental_details = []

    #getters
    def get_name(self):
        return self.name
    def get_contact_number(self):
        return self.contact_number
    def get_driving_license(self):
        return self.driving_license
    def get_cnic(self):
        return self.cnic

    #setters
    def set_name(self, name):
        self.name = name
    def set_contact_number(self, contact_number):
        self.contact_number = contact_number
    def set_driving_license(self, driving_license):
        self.driving_license = driving_license
    def set_cnic(self, cnic):
        self.cnic = cnic
    def add_rental_details(self,details):
        '''Add a customer detail to the account'''
        self.rental_details.append(details)
        print("Rental detail added.")

    def display_rental_details(self):
        '''show all rental details to the customer'''

        if not self.rental_details:
            print("No rental details found.")
        else:
            print("Rental Details:")
            for i, detail in enumerate(self.rental_details, 1):
                print(f"{i}.{detail}")
    @classmethod
    def sign_up(cls, name, email, password, contact_number =None, driving_license =None, cnic =None):
        '''sign-up function to add a customer '''
        if email in cls._customers:
            print("An account with this email already exist")
            return None
        else:
            cls._customers[email] = Customer(name, email, password, contact_number, driving_license, cnic)
            print("sign-up succeessful!")
            return cls._customers[email]
    @classmethod
    def login(cls, email, password):
        if email in cls._customers and cls._customers[email].password == password:
            print("Login successful!")
            return cls._customers[email]
        else:
            print("Invalid email or password")
            return None

# example
#sign-up
customer1 = Customer.sign_up("Ethan Carter", "Ethan@gmail.com", "password123", contact_number= "12345678", driving_license="Dl1234356", cnic="cnic12314352")
customer2 = Customer.sign_up("Abdullah", "Abdullah2@gmail.com", "password12345")

#login
logged_in_customer = Customer.login("Abdullah2@gmail.com", "password12345")

if logged_in_customer:
    logged_in_customer.add_rental_details("Car rental: Toyota  Corolla - 5 days")
    logged_in_customer.display_rental_details()
    logged_in_customer.set_contact_number("01234564536")
    logged_in_customer.set_name("Abdullah")

    print(f"Updated Name: {logged_in_customer.get_name()}")
    print(f"Updated Contact Number: {logged_in_customer.get_contact_number()}")