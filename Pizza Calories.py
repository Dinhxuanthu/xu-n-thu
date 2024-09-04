class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.__topping_type = topping_type
        self.__weight = weight

    # Getters
    @property
    def topping_type(self):
        return self.__topping_type

    @property
    def weight(self):
        return self.__weight

    # Setters
    @topping_type.setter
    def topping_type(self, value: str):
        self.__topping_type = value

    @weight.setter
    def weight(self, value: float):
        self.__weight = value
class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight

    # Getters
    @property
    def flour_type(self):
        return self.__flour_type

    @property
    def baking_technique(self):
        return self.__baking_technique

    @property
    def weight(self):
        return self.__weight

    # Setters
    @flour_type.setter
    def flour_type(self, value: str):
        self.__flour_type = value

    @baking_technique.setter
    def baking_technique(self, value: str):
        self.__baking_technique = value

    @weight.setter
    def weight(self, value: float):
        self.__weight = value
class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    # Getters
    @property
    def name(self):
        return self.__name

    @property
    def dough(self):
        return self.__dough

    
    def toppings(self):
        return self.__toppings

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    
    @name.setter
    def name(self, value: str):
        self.__name = value

    @dough.setter
    def dough(self, value: Dough):
        self.__dough = value

    @toppings_capacity.setter
    def toppings_capacity(self, value: int):
        self.__toppings_capacity = value

  
    def add_topping(self, topping: Topping):
        if len(self.__toppings) >= self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.__toppings:
            self.__toppings[topping.topping_type] += topping.weight
        else:
            self.__toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = self.__dough.weight + sum(self.__toppings.values())
        return total_weight

pepperoni = Topping("Pepperoni", 50)
mushrooms = Topping("Mushrooms", 30)
thin_crust = Dough("Whole Wheat", "Crispy", 100)
pizza = Pizza("Pepperoni Pizza", thin_crust, 5)
pizza.add_topping(pepperoni)
pizza.add_topping(mushrooms)

print(f"Total weight of the pizza: {pizza.calculate_total_weight()}g")
