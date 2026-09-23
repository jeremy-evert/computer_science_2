class Oven:

    def cook(self, food):
        return f"The oven bakes the {food}."

    def can_cook(self, food):
        return food == "pizza"


class Grill:

    def cook(self, food):
        return f"The grill sears the {food}."

    def can_cook(self, food):
        return food == "burgers"    

    def cooking_method(self):
        return "direct heat"


def prepare_meal(appliance, food):
    return appliance.cook(food)
