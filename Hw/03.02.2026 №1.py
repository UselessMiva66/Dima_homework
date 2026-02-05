class Potion:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def drink(self):
        return f'Вы выпили {self.name}! , Ваша сила {self.power}' 
power_potion = Potion('sila', 100)
print(power_potion.drink())
