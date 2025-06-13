from design_pattrens.decorator.Pizza import Pizza


class BasePizza(Pizza):

    def get_price(self):
        return 100