class Dessert:
    desert = ['cake', 'cheesecake', 'Tiramisu', 'apple pie', 'cupcake']

    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, calories):
        self._calories = calories

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


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self) -> True or False:
        if self.flavor == 'black licorice':
            return False
        return True


dt = JellyBean('cake', 190, 'black licorice')
dt2 = JellyBean('cheesecake', 250, 'Fruit')
dt3 = JellyBean('Tiramisu', 180)
dt4 = JellyBean()

print(dt.name, dt.is_healthy())
print(dt.name, dt.is_delicious())

print(dt2.name, dt2.is_healthy())
print(dt2.name, dt2.is_delicious())

print(dt3.name, dt3.is_healthy())
print(dt3.name, dt3.is_delicious())

print(dt4.name, dt4.is_healthy())
print(dt4.name, dt4.is_delicious())