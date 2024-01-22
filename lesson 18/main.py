# class Point2D:
#     __slots__ = ('__x', 'y', )
#
#     def __init__(self, x, y):
#         self.y = 1
#         self.__x = 1
#
#     def inputData(self):
#         self.__x = input()
#         self.y = input()
#
#     def __str__(self):
#         return f'{self.__x = }, {self.y = }'
#
#     def calc(self):
#         self.__x += 1
#         del self.y
#         self.y = 0
#
#     def x(self, value):
#         return self.__x
#
# class Point2DCopy:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def calc(self):
#         self.x *= 1
#         del self.y
#         self.y = 0
#
#     def append_z(self, value):
#         self.z = value
#
#     def __str__(self):
#         return f'{self.x = }, {self.y = }'
#
#
# pt = Point2D(13, 42)
# pt.calc()
# pt2 = Point2DCopy(13, 42)
# pt2.calc()
# pt2.append_z(213)
#
# import timeit
#
# t1 = timeit.timeit(pt.calc)
# t2 = timeit.timeit(pt2.calc)
# print(pt, ')(', pt2)
# print(t1, ') (', t2)
# print(pt2.__dict__)
#
#
# # # print(pt.__dict__)
# # # pt.z = 4
# # # print(pt.__dict__)
# # # Чтобы не было доступа к свойствам класса можно использовать колекцию слотс
# # print(pt.__slots__)
# # # pt.z = 4
# # # Добавлять нельзя, но менять уже имеющиеся значения можно
# # del pt.y
# # # print(pt.y)
# # pt.y = 3
# # print(pt.y)
# # print(pt)
# # # Когда удаляем свойство оно его не видит, но от есть в слотс, поэтому его можно восстановить


# class User:
#     # __slots__ = ('__name', '__password', '__age')
#
#     def __init__(self, name, password, age):
#         self.__name = name
#         self.__password = password
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str):
#             self.__name = value
#         else:
#             print('Error')
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, value):
#         if isinstance(value, str):
#             self.__password = value
#         else:
#             print('Error')
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, value):
#         if isinstance(value, int):
#             self.__age = value
#         else:
#             print('Error')
#
#
# user = User('Tom', '123', 123)
# user.name = 123
# user.password = 123
# user.age = "123"
#
# print(user.__dict__)
# user._User__age = "1234"
#
# print(user.age)
# print(user.name)
# print(user.password)

class Point2D:
    __slots__ = ('_x', '_y', '_length')

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._length = (self._x * self._x + self._y * self._y) * 0.5

    def calc_length(self):
        self._length = (self._x * self._x + self._y * self._y) * 0.5

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, int):
            self._x = value
            self.calc_length()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, int):
            self._y = value
            self.calc_length()

    @property
    def length(self):
        return self._length


pt = Point2D(1, 2)
pt.x = 8
print(pt.length)


class Point3D(Point2D):
    __slots__ = '_z'

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z
        self._length = (self._x * self._x + self._y * self._y + self._z * self._z) * 0.5

    def calc_length(self):
        self._length = (self._x * self._x + self._y * self._y + self._z * self._z) * 0.5

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        if isinstance(value, int):
            self._z = value
            self.calc_length()

pt3 = Point3D(1, 2, 3)
# pt3.z = 2
# print(pt3.__dict__)

# print(pt3.__slots__)
print(pt3.length)
pt3.x = 1
print(pt3.length)
