# object

class Car:
    color = 'black'
    transmission = 'manual'
    gear_position = 'N'

    def __init__(self, transmission):
        self.transmission = transmission
        print("mesin sudah siap")

    def drive(self):
        self.gear_position = 'D'
        print('Drive')

    def reverse(self):
        self.gear_position = 'R'
        print('reverse, please check your behind')

    def change_gear(self, gear='N'):
        self.gear_position = gear
        print('Gear position on: ' + self.gear_position)

    def get_gear_position(self):
        return self.gear_position


car1 = Car('manual')
car1.change_gear('D-1')

car2 = Car('automatic')
gear_position = car2.get_gear_position()
print(gear_position)

print('-'*40)

# Inheritance


class Car:
    def fuel(self):
        return 'gas'


class Honda(Car):
    pass


class Tesla(Car):
    def fuel(self):
        return 'electricity'


def get_fuel(Car):
    print(Car.fuel())


get_fuel(Tesla())
get_fuel(Honda())
