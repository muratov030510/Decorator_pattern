class Car:
    def cost(self):
        pass


class Sedan(Car):
    def cost(self):
        return 1500


class Crossover(Car):
    def cost(self):
        return 2200


class WashDecorator(Car):
    def __init__(self, car):
        self.car = car


class FullServiceCarWash(WashDecorator):
    def cost(self):
        return self.car.cost() + 1500


class SelfServiceCarWash(WashDecorator):
    def cost(self):
        return self.car.cost() + 500


car = Sedan()
car2 = Crossover()


vipauto = FullServiceCarWash(car)
print("FullService Car Wash: T", vipauto.cost())


auto_selfserv = SelfServiceCarWash(car)
print("SelfService Car Wash: T", auto_selfserv.cost())


vipauto2 = FullServiceCarWash(car2)
print("FullService Car Wash: T", vipauto2.cost())


auto_selfserv2 = SelfServiceCarWash(car2)
print("SelfService Car Wash: T", auto_selfserv2.cost())
