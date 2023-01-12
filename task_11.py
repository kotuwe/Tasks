class Dessert:
    desert = ['cake', 'cheesecake', 'Tiramisu', 'apple pie', 'cupcake']

    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self) -> True or False:
        if self.name is None and self.calories is None:
            return False
        for i in self.desert:
            if i == self.name and self.calories < 200:
                return True
            return False

    def is_delicious(self) -> True or False:
        if self.name is None and self.calories is None:
            return False
        for i in self.desert:
            if self.name == i:
                return True
        return False


dt = Dessert('cake', 190)
dt2 = Dessert('cheesecake', 250)
dt3 = Dessert('ssss', 180)
dt4 = Dessert()

print(dt.name, dt.is_healthy())
print(dt.name, dt.is_delicious())

print(dt2.name, dt2.is_healthy())
print(dt2.name, dt2.is_delicious())

print(dt3.name, dt3.is_healthy())
print(dt3.name, dt3.is_delicious())

print(dt4.name, dt4.is_healthy())
print(dt4.name, dt4.is_delicious())
