class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled=False):
        self.__color = __color
        self.__sides = []
        self.filled = bool(filled)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and r in range(256):
            if isinstance(g, int) and g in range(256):
                if isinstance(b, int) and b in range(256):
                    self.__color = r, g, b

    def set_color(self, r, g, b):
        self.__is_valid_color(r, g, b)
        return r, g, b

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for i in sides:
                if i > 0 and isinstance(i, int):
                    continue
                else:
                    return False
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [*sides]
        elif len(sides) == 1 and self.sides_count == 12 and sides[0] > 0:
            self.__sides = []
            for i in range(12):
                self.__sides.append(*sides)
        elif len(sides) == 1 and self.sides_count == 3 and sides[0] > 0:
            self.__sides = []
            for i in range(3):
                self.__sides.append(*sides)
        else:
            self.__sides = self.sides

    def __len__(self):
        summa = 0
        for i in self.__sides:
            summa += i
        return summa


class Circle(Figure):
    sides_count = 1

    def __init__(self, __sides, __color):
        super().__init__(__sides, __color)
        self.sides = [__sides] * self.sides_count
        self.__radius = __sides / 6.28

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __sides, __color):
        super().__init__(__sides, __color)
        self.sides = [__sides] * self.sides_count

    def get_square(self):
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __sides, __color):
        super().__init__(__sides, __color)
        self.sides = [__sides] * self.sides_count

    def get_volume(self):
        return self.sides[0] ** 3


cube1 = Cube(6, (222, 35, 130))
circle1 = Circle(10, (200, 200, 100))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
