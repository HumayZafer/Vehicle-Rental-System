import random
from Customer import Customer

class Customermanager(Customer):
    def __init__(self, name, email, password, contact_number=None, driving_license=None, cnic=None):
        super().__init__(name, email, password, contact_number, driving_license, cnic)
        self.loyalty_points = 0 #initialize loyalty points
        self.random_discount = 0 # hold randomly assigned discount

    def assign_random_discount(self):
        self.random_discount = random.randint(5,20)
        print(f"Assigned {self.random_discount}% random discount to {self.name}")
        return self.random_discount

    def earn_loyalty_points(self, cost):
        #add loyalty points based on rental cost
        earned_points = cost # $1 = 1 point
        self.loyalty_points += earned_points
        print(f"{self.name} earned {earned_points} loyalty points. Total: {self.loyalty_points} points")

    def apply_loyalty_discount(self):
        if self.loyalty_points >= 300:
            loyalty_discount = 15
        elif self.loyalty_points >= 200:
            loyalty_discount = 10
        elif self.loyalty_points >=100 :
            loyalty_discount = 5
        else:
            loyalty_discount = 0

        print(f"{self.name} qualifies for {loyalty_discount}% loyalty discount")
        return loyalty_discount

    def get_total_discount(self):

        #combine random discount and loyalty discount, apply higher of the two
        loyalty_discount = self.apply_loyalty_discount()
        total_discount = max(self.random_discount,loyalty_discount)
        print(f"Total discount for {self.name}: {total_discount}%")

    def redeem_loyalty_points(self, points_to_redeem):

        #redeeem loyalty points
        if points_to_redeem <= self.loyalty_points:
            self.loyalty_points -= points_to_redeem
            print(f"{self.name} redeemed {points_to_redeem} loyalty points. Remaining: {self.loyalty_points} points.")
            return True
        else:
            print(f"Insufficient points. {self.name} only has {self.loyalty_points} points.")
            return False


'''# Example
if __name__ == "__main__":
    customer1 = Customer.sign_up("Ethan Carter", "Ethan@gmail.com", "password123", contact_number="12345678",
                                 driving_license="Dl1234356", cnic="cnic12314352")
    customer2 = Customer.sign_up("Abdullah", "Abdullah2@gmail.com", "password12345")

    # Login
    logged_in_customer = Customer.login("Abdullah2@gmail.com", "password12345")

    if logged_in_customer:
        customer_manager = Customermanager(
            logged_in_customer.get_name(), logged_in_customer.email, logged_in_customer.password,
            logged_in_customer.contact_number, logged_in_customer.driving_license, logged_in_customer.cnic
        )

        # Simulate a rental and earn loyalty points
        rental_cost = 250  # Customer rented a vehicle for $250
        customer_manager.earn_loyalty_points(rental_cost)

        # Assign a random discount
        customer_manager.assign_random_discount()

        # Get total discount (random + loyalty points)
        customer_manager.get_total_discount()

        # Redeem loyalty points for discount
        customer_manager.redeem_loyalty_points(100)

        # Get the new total discount after redeeming points
        customer_manager.get_total_discount()'''