import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = ()
        if self.__is_valid_sides(*sides):
            self.__sides = sides
        else:
            one_unit = 1
            i = 0
            while i < self.sides_count:
                self.__sides += (one_unit,)
                i += 1

        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = color

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if sides.__len__() == self.sides_count:
            for side_value in sides:
                if side_value <= 0 or (not isinstance(side_value, int)):
                    return False
            return True
        return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / ( 2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius * self.__radius

    def __len__(self):
        return self.get_sides()[0]


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        tri_sides = self.get_sides()
        half_p = (tri_sides[0] + tri_sides[1] + tri_sides[2]) / 2
        return math.sqrt(half_p * (half_p - tri_sides[0]) * (half_p - tri_sides[1]) * (half_p - tri_sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        self.__sides = ()
        if sides.__len__() == 1 and sides[0] > 0 and isinstance(sides[0], int):
            i = 0
            while i < self.sides_count:
                self.__sides += (sides[0],)
                i += 1
        else:
            one_unit = 1
            i = 0
            while i < self.sides_count:
                self.__sides += (one_unit,)
                i += 1

    def get_volume(self):
        return  self.__sides[0] ** 3

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if new_sides.__len__() == 1 and new_sides[0] > 0 and isinstance(new_sides[0], int):
            i = 0
            while i < self.sides_count:
                self.__sides += (new_sides[0],)
                i += 1



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(f"[{circle1.get_sides()[0]}]")

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# print(f"[{circle1.get_sides()[0]}]")