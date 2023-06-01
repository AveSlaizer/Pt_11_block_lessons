from abc import ABC, abstractmethod


class DescriptionProduct(ABC):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_price(self):
        raise NotImplementedError


class Product(DescriptionProduct):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class CompositeProduct(DescriptionProduct):

    def __init__(self, name):
        self.__name = name
        self.__products = []

    @property
    def products(self):
        return self.__products

    def add(self, product: DescriptionProduct):
        self.__products.append(product)

    def remove(self, product: DescriptionProduct):
        self.__products.remove(product)

    def clear(self):
        self.__products.clear()

    def get_name(self):
        return self.__name

    def get_price(self):
        return sum([x.get_price() for x in self.products])


class Box(CompositeProduct):

    def __init__(self, name):
        super(Box, self).__init__(name)

    def get_price(self):
        return sum([x.get_price() for x in self.products])


if __name__ == "__main__":

    phone = Product("Ipad", 50000)
    set1 = CompositeProduct("Инструменты")
    set1.add(Product("Дрель", 5000))
    set1.add(Product("Лобзик", 6000))
    box = Box("Посылка")
    box.add(phone)
    box.add(set1)
    print(box.get_price())
