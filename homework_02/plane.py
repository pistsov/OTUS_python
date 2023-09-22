"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo: int = 0
        self.max_cargo: int = max_cargo

    def load_cargo(self, load: int):
        if self.cargo + load <= self.max_cargo:
            self.cargo += load
        else:
            raise CargoOverload
        pass

    def remove_all_cargo(self):
        temp_cargo = self.cargo
        self.cargo = 0
        return temp_cargo
