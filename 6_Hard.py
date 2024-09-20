class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled):  # __sides(список сторон (целые числа))
        # __color(список цветов в формате RGB), filled(закрашенный, bool)
        self.__color = __color
        self.__sides = __sides
        self.filled = bool(filled)

    def get_color(self):  # Метод get_color, возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, r, g, b):  # проверяет корректность переданных значений перед установкой нового цвета.
        # Корректный цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        if isinstance(r, int) and r in range(256):
            if isinstance(g, int) and g in range(256):
                if isinstance(b, int) and b in range(256):
                    self.__color = r, g, b

    def set_color(self, r, g, b):  # изменяет атрибут __color на соответствующие значения, предварительно проверив
        # их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        self.__is_valid_color(r, g, b)
        return r, g, b

    def get_sides(self):  # должен возвращать значение атрибута __sides.
        if self.__is_valid_sides() is True:
            self.set_sides()
        return self.__sides

    def __is_valid_sides(self, *sides):  # принимает неограниченное кол-во сторон, возвращает True если все стороны
        # целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        if isinstance(sides, int) and sides > 0:
            if len(self.__sides) == self.sides_count:
                return True
        else:
            return False

    def __len__(self):  # должен возвращать периметр фигуры.
        pass

    def set_sides(self, *new_sides):  # должен принимать новые стороны, если их количество не равно sides_count,
        # то не изменять, в противном случае - менять.
        if len(new_sides) == self.sides_count:
            return self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides, __color, filled):  # Атр. __radius, рассчитать исходя из длины окружности
        # (одной единственной стороны).
        super().__init__(__sides, __color, filled)
        self.__radius = __sides / 6.28
        if __sides == self.sides_count:
            """self.__sides = [__sides] * self.sides_count В этом условии нужно разбираться"""
        else:
            self.__sides = [1] * self.sides_count
        print(self.__sides)

    def get_square(self):  # Возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        pass


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color, filled):
        super().__init__(__sides, __color, filled)
        if __sides == self.sides_count:
            """self.__sides = [__sides] * self.sides_count В этом условии нужно разбираться"""
        else:
            self.__sides = [1] * self.sides_count
        print(self.__sides)

    def get_square(self):  # Возвращает площадь треугольника. (можно рассчитать по формуле Герона).
        pass


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides, __color, filled):  # Переопределить __sides сделав список из 12 одинаковы сторон
        # (передаётся 1 сторона)
        super().__init__(__sides, __color, filled)
        if __sides == self.sides_count:  # В этом условии нужно разбираться
            self.__sides = [__sides] * self.sides_count
        else:
            self.__sides = [1] * self.sides_count
        print(self.__sides)

    def get_volume(self):  # возвращает объём куба.
        pass



cube1 = Cube(6, (222, 35, 130), False)
cube2 = Cube(2, (56, 120, 48), True)
circle1 = Circle(10, (200, 200, 100), True)  # (Стороны, цвет, заливка)
triangle1 = Triangle(4, (251, 80, 150), True)


# # Проверка на изменение цветов:
# circle1.set_color(55, 66, 77)  # Изменится
# print(circle1.get_color())
# cube1.set_color(300, 70, 15)  # Не изменится
# print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5, 5, 5)  # Не изменится
print(cube1.get_sides())
cube1.set_sides(4)  # Изменится
print(cube1.get_sides())
cube2.set_sides(5)
print(cube2.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())


#
# # Проверка периметра (круга), это и есть длина:
# print(len(circle1))
#
# # Проверка объёма (куба):
# print(cube1.get_volume())