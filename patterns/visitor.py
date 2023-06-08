class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


class CarVisitor:

    __path: str

    def create_car_info(self, car: Car):
        name = car.get_name()
        color = car.get_color()

        # Записать в файл

        self.__path = "car.txt"

    def get_cat_info(self):
        return self.__path

