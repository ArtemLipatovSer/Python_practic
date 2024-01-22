# # # class Point:
# # #     xr = 12
# # #     xm = 10
# # #     # Глобальные переменные класса, могут меняться вне класса
# # #     def __new__(cls, *args, **kwargs):
# # #         print('Вызов __new__' + str(cls))
# # #         return super().__new__(cls) # cls - указатель на класс
# # #
# # #     def __init__(self, x, y):
# # #         print('вызов __init__')
# # #         self.x = x
# # #         self.y = y
# # #         print(f'x = {self.x}, y = {self.y}')
# # #         print(Point.xm)
# # #
# # #
# # # # Point.xm = 12
# # # # print(Point.xm)
# # # # Point1 = Point(1, 2)
# # # # Point2 = Point(3, 2)
# # #
# # # pt1 = Point(1,2)#Происходит только вызов класса new
# # # print(pt1)#Тут лежит none
# #
# # class DateBase:
# #     __instance = None
# #     def __new__(cls, *args, **kwargs):
# #         if cls.__instance is None:
# #             cls.__instance = super().__new__(cls)
# #         return cls.__instance
# #     def __init__(self, user, psw, port):
# #         self.user = user
# #         self.psw = psw
# #         self.port = port
# #
# #     def connect(self):
# #         print(f'Соединение с БД, {self.user}, {self.psw}, {self.port}')
# #
# #
# # DB1 = DateBase('root', '1234', '80')
# # DB1.connect()
# # DateBase.__instance = None
# # DB2 = DateBase('root2', '12345', '88')
# # DB2.connect()
# # print(DB1, DB2)
# #
# # # Если мы делаем без метода new, но получается так что когда мы инициализируем класс, а птом второй раз инициализируем,
# # # получается два класса в разных ячеках памяти, но нам нужно только один, тогда мы используем класс нью, и когда мы каждый раз инициализируем
# # # класс мы тспользуем один и тот же и можно с разными параметрами (стучимся в две двери кторые ведут в одно и тоже место)
#
#
# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#     @classmethod # Используются параметры внутри класса, предназначена для других методов в классе
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     @staticmethod
#     # Следующее задание. Обычная функция (не использует методы и функции класса)
#     def get_square(a, b):
#         return a * b
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# v1 = Vector(-10, 20)
# # Vector.validate(6)
# # print(v1.validate(5))
# print(v1.get_coord())
#
# print(Vector.get_square(10, 15))


# Самостоятельно:

class Review:
    MAX_SIMB = 10

    def __init__(self, avtor, text, numPhone):
        self.avtor = avtor
        self.text = numPhone
        self.text = 'Превышено количество символов в отзыве'
        if self.validate(text):
            self.text = text


    @classmethod
    def validate(cls, arg):
        return len(arg) <= cls.MAX_SIMB

    @staticmethod
    def printReview(text):
        text = text.lowerCase()

    def get_coord(self):
        return self.text


one = Review('qweqe', 'qweqweqwrerwerwr', 'qweqweqwe')
print(one.get_coord())




