from design_pattrens.adapterDP.Phonepe import Phonepe


from design_pattrens.adapterDP.Adapter.AxisBankAdapter import AxisBankAdapter
from design_pattrens.adapterDP.Adapter.YesBankAdapter import YesBankAdapter

if __name__ == "__main__":
    p=Phonepe(YesBankAdapter())
    print(p.get_balance())