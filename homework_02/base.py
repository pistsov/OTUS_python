from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 1000, fuel: int = 0, fuel_consumption:  int = 10.0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption  # liters per 1 km
        self.started: bool = False

    def check_fuel(self):
        if self.fuel > 0:
            return 1
        else:
            raise LowFuelError

    def start(self):
        if not self.started:
            if self.check_fuel():
                self.started = True
        else:
            print("Already started!")

    def move(self, dist: int):  # distance in km
        fuel_move = dist * self.fuel_consumption
        if self.fuel >= fuel_move:
            self.fuel -= fuel_move
        else:
            raise NotEnoughFuel
