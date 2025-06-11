from design_pattrens.strgy.Factories.PaymentFactory import PaymentFactory
from design_pattrens.strgy.strgies.PaymentCC import CreditCardPayment
from design_pattrens.strgy.strgies.DebitCardPayment import DebitCardPayment

if __name__ == "__main__":
    choice = input("Enter the type of Payment choice CC/DC: ").strip().upper()
    PaymentFactory.create_payment(choice).pay(1000)