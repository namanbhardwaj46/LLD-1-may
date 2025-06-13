from design_pattrens.decorator.addons.Addons import Addons


class Mushroom(Addons):

    def get_price(self):
        return self.pizza.get_price() + 15
