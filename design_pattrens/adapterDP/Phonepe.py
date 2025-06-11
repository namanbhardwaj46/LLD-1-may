from design_pattrens.adapterDP.Adapter.BankAdapterInterface import BankAdapterInterface

class Phonepe:

    def __init__(self, bank: BankAdapterInterface):
        self.bank = bank


    def get_balance(self):
        try:
            balance = self.bank.get_balance()
            if balance < 0:
                raise ValueError("Balance cannot be negative")
            return balance
        except Exception as e:
            print(f"Error getting balance: {e}")
            return None
