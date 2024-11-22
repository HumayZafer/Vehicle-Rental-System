


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

