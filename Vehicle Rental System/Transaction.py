import random
import datetime



import Reservation


class Transaction(Reservation):
    def __init__(self, customer, vehicle, rental_duration, total_cost, payment_method):
        super().__init__(customer , vehicle, rental_duration, total_cost)
        self.transaction_id = random.randint(1000, 9999)
        self.payment_method = payment_method
        self.transaction_date = datetime.datetime.now()

    def get_transaction_summary(self):
        return f"Transaction Id: {self.transaction_id}\n{self.get_summary()}\nPayment Method: {self.payment_method}\n Transaction Date: {self.transaction_date}"

    def process_transaction(self):
        print(f"Processing transaction {self.transaction_id} for {self.customer}")
        return True

#Child Class Epay

class Epay(Transaction):
    def __init__(self, customer, vehicle, rental_duration, total_cost, debit_credit, card_number, expiration_date):
        super().__init__(customer, vehicle, rental_duration, total_cost, "Epay")
        self.debit_credit = debit_credit #Debit or Credit
        self.card_number = card_number
        self.expiration_date = expiration_date

    def get_payment_details(self):
        return f"Payment Method: {self.debit_credit}\nCard Number: **** **** **** {self.card_number[-4:]}\nExpiration Date: {self.expiration_date}"

    def process_payment(self):
        #payment process
        if self.card_number and self.expiration_date:
            print(f"Processing{self.debit_credit} payment for card ending in {self.card_number[-4:]}")
            return True
        else:
            print("Invalid payment details")
            return False

#child class Invoice
class Invoice(Transaction):
    def __init__(self, customer, vehicle, rental_duration, total_cost, email_address):
        super().__init__(customer, vehicle, rental_duration, total_cost, "Invoice")
        self.email_address = email_address

    def send_invoice(self):
        invoice_details = f"Sending invoice to {self.email_adddress}:\n{self.get_transaction_summary()}"
        #sending email
        print(invoice_details)
        print(f"Invoice sent to {self.email_address}.")

    def get_invoice_summary(self):
        return f"Invoice for {self.customer} for the vehicle {self.vehicle} with total cost: {self.total_cost}. Sent to: {self.email_address}"

# child class
class Cash(Transaction):
    def __init__(self, customer, vehicle, rental_duration, total_cost):
        super().__init__(customer, vehicle, rental_duration, total_cost, "Cash")

    def get_payment_details(self):
