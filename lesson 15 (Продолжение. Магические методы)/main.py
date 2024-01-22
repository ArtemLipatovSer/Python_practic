# object
#
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.z = 0
#         self.__x = x
#         self.__y = y
#
#     def __setattr__(self, key, value):
#         # Можно запретить менять значения какому нибудь атрибуту
#         if key == 'z' and value < 0:
#             raise ValueError('Число должно быть больше!')
#         print('setattr', key, value)
#         return object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):
#         if item == '_Point__x':
#             raise ValueError('Private attribute')
#         print('__getattribute__', item)
#
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item): #Помогает тогда когда мы хотим получить не существующий метод, если бы не он вылетала бы ошибка
#         if item == 'c':
#             raise AttributeError('Метод изменился, смотри документацию')
#         raise AttributeError('Такого метода и не было')
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1,2)
# # print(pt1.x)
# # print(pt1.__dict__) #__dict__ показывает инфломацию о том или ином методе, который мы указываем (или классе)
# # # Если атрибуты делаем приватными (__х), выводится они не будут (но можно найти следующи образом _Point.__x
# # # print(pt1._Point__x)
# # print(pt1._Point__x)
# # В итоге гет атрибьют нужен для того чтобы обезопасить систему, чтобы не было доступа к другим атрибутам в классе
#
# # # Setattr:
# # pt1.z = 300
# # print(pt1.z)
# # pt1.z = -1
# # print(pt1.z)
#
# # getattr
# # print(pt1.f)
# print(pt1.c)
from pprint import pprint


# тоже самое только по другому методу (более современному)
# class Point3D:
#     _x = Integer()
#     _y = Integer()
#     _z = Integer()
#     def __init__(self, x, y, z):
#         self.verify_coord(x)
#         self.verify_coord(y)
#         self.verify_coord(z)
#
#         self._x = x
#         self._y = y
#         self._z = z
#
#     @property # Геттер
#     def x(self):
#         print('ПРОИЗОШЕЛ ВЫЗОВ Х')
#         return self._x
#
#     @x.setter
#     def x (self, coord):
#         print('УСТАНОВКА ЗНАЧЕНИЯ ДЛЯ Х')
#         self.verify_coord(coord)
#         self._x = coord
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError('Координата должна быть инт')
#
# pt1 = Point3D(1, 2, 3)
# print(pt1.x)
# print(Point3D.__dict__)
# pt1.x = 6
# print(pt1.x)

# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if type(coord) != int:
#             raise TypeError('Координата должна быть инт')
#
#     def __set_name__(self, owner, name):  # Для установки значение для свойства
#         self.name = '__' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         print(f'__set_: {self.name}, {instance}')
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# pt1 = Point3D(1, 2, 3)
#
# print(pt1.__dict__) # Дискрипторы!


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     # def info(self):
#     #     print('Кошка - имя ', self.name) вместо этого ниже
#     def __str__(self): # Получение информации о класса
#         return f'Кошка - имя {self.name}'
#
# cat = Cat('Мурка')
# # cat.info()
# print(cat)


# class Market:
#     def __init__(self):
#         self.gods = []
#
#     def append(self, dict):
#         self.gods.append(dict)
#
#     def show(self):
#         pprint(self.gods)
#
#     def __len__(self):
#         return len(self.gods)
#
# shop = Market()
#
# shop.append({'Товар 1': 1})
# shop.append({'Товар 2': 4})
# shop.append({'Товар 3': 7})
# shop.append({'Товар 4': 3})
# shop.show()
# print(len(shop))



# Следующее задание

class Clock:

    def __init__(self, seconds: int):
        if isinstance(seconds, int):
            self.seconds = seconds
        else:
            raise TypeError('Секунды должны быть Int')

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('C Int складываем только int и clock')
        sc = other if(isinstance(other, int)) else other.seconds
        return Clock(self.seconds + sc)


c1 = Clock(1000)
print(c1.get_time())

c2 = c1 + 150
print(c2.get_time())

c3 = c1 + c2
print(c3.get_time())
