from design_pattrens.strgy.strgies.paymentStrgy import PaymentStrategy


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print("DebitCard Payment for amount:"+ str(amount) + " via cashfree")

        # Here you would add the logic to process the debit card payment
        # For example, interacting with a payment gateway API
        return True