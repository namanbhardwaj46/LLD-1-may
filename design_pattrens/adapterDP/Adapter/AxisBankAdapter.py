from design_pattrens.adapterDP.Adapter.BankAdapterInterface import BankAdapterInterface
from design_pattrens.adapterDP.banks.AxisBank import  AxisBank

class AxisBankAdapter(BankAdapterInterface):

    def __init__(self):
        self.axis_bank = AxisBank()

    def get_balance(self):

        try:
            return self.axis_bank.bal()
        except Exception as e:
            print(f"Error getting balance from Axis Bank: {e}")
            return None


