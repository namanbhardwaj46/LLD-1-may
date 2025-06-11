from design_pattrens.strgy.strgies.paymentStrgy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def __init__(self):
        self.name = "Credit Card Payment"

    def pay(self, amount):
        print(f"Processing {self.name} of amount: {amount} via razorpay")
        # Here you would add the logic to process the credit card payment
        # For example, interacting with a payment gateway API
        return True  # Assuming the payment was successful