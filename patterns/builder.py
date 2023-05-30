from abc import ABC, abstractmethod


class Engine(ABC):
    pass


class DieselEngine(Engine):
    pass


class Computer(ABC):
    pass


class ServiceComputer(Computer):
    pass


class Car:
    def __init__(self):
        self.engine = None
        self.computer = None
        self.seats = 0


class Builder(ABC):

    @abstractmethod
    def create(self):
        raise NotImplementedError

    @abstractmethod
    def set_engine(self, engine: Engine):
        raise NotImplementedError

    @abstractmethod
    def set_computer(self, computer: Computer):
        raise NotImplementedError

    @abstractmethod
    def set_seats(self, count_seats: int):
        raise NotImplementedError

    @abstractmethod
    def get_car(self):
        raise NotImplementedError


class CarBuilder(Builder):
    __car: Car

    def create(self):
        self.__car = Car()

    def set_engine(self, engine: Engine):
        self.__car.engine = engine

    def set_computer(self, computer: Computer):
        self.__car.computer = computer

    def set_seats(self, count_seats: int):
        self.__car.seats = count_seats

    def get_car(self):
        return self.__car


if __name__ == "__main__":
    car_builder = CarBuilder()
    car_builder.create()
    car_builder.set_seats(4)
    car_builder.set_computer(ServiceComputer())
    car_builder.set_engine(DieselEngine())
    print(car_builder.get_car())
