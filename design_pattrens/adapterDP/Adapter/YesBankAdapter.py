from .BankAdapterInterface import BankAdapterInterface

class YesBankAdapter(BankAdapterInterface):

    def __init__(self):
        from design_pattrens.adapterDP.banks.yesBank import yesBank
        self.yes_bank = yesBank()


    def get_balance(self):

        try:
            return self.yes_bank.get_balance()
        except Exception as e:
            print(f"Error getting balance from Axis Bank: {e}")
            return None


