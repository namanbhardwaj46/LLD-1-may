from design_pattrens.strgy.strgies.DebitCardPayment import DebitCardPayment
from design_pattrens.strgy.strgies.PaymentCC import CreditCardPayment


class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type == "CC":
            return CreditCardPayment()
        elif payment_type == "DC":
            return DebitCardPayment()
        else:
            raise ValueError("Unknown payment type")