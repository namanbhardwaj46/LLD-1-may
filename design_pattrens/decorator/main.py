from design_pattrens.decorator.BasePizza import BasePizza
from design_pattrens.decorator.addons.Cheese import Cheese
from design_pattrens.decorator.addons.Mushroom import Mushroom

if __name__ == '__main__':

    p1 = BasePizza()
    print(f"Base Pizza Price: {p1.get_price()}")

    p2 = Cheese(p1)

    print(f"Pizza with Cheese Price: {p2.get_price()}")

    p3 = Mushroom(p2)
    print(f"Pizza with Cheese and Mushroom Price: {p3.get_price()}")

    p4 = Cheese(p3)
    print(f"Pizza with Double Cheese and Mushroom Price: {p4.get_price()}")


    print(f"Total Price: {p4.get_price()}")