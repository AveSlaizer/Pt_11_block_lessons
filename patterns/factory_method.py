from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        raise NotImplementedError


class Logistics(ABC):

    @abstractmethod
    def create_transport(self):
        raise NotImplementedError


class Truck(Transport):

    def deliver(self):
        print("Доставка груза транспортом типа Грузовик")


class Ship(Transport):

    def deliver(self):
        print("Доставка груза транспортом типа Корабль")


class RoadLogistics(Logistics):

    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):

    def create_transport(self):
        return Ship()


if __name__ == "__main__":
    road_log = RoadLogistics()
    truck = road_log.create_transport()
    truck.deliver()
