# def decorator(func):
#     def wrapper():
#         print('Начало декоратора')
#         func()
#         print('Конец декоратора')
#     return wrapper
#
# def testFunction():
#     print('Hello World')
#
# dec1 = decorator(testFunction)
#
# dec1()
from pprint import pprint


# def decorator(func):
#     # def wrapper(x, *args, **kwargs):
#         # print(args)
#         # print(kwargs)
#         # print(x)
#     def wrapper(*args, **kwargs):
#         print('Начало декоратора')
#         func(*args, **kwargs)
#         print('Конец декоратора')
#     return wrapper
#
# def testFunction(name, secondMess, lowercase = False):
#     if lowercase:
#         print(f'Hello {name}! {secondMess}'.lower())
#     else:
#         print(f'Hello {name}! {secondMess}')
# dec1 = decorator(testFunction)
#
# dec1('Tom', 'Have a good day', lowercase = True)
# dec1('Test2', '')


#
# def decorator(func):
#     # def wrapper(x, *args, **kwargs):
#         # print(args)
#         # print(kwargs)
#         # print(x)
#     def wrapper(*args, **kwargs):
#         print('Начало декоратора')
#         func(*args, **kwargs)
#         print('Конец декоратора')
#     return wrapper
#
# @decorator
# def testFunction(name, secondMess, lowercase = False):
#     if lowercase:
#         print(f'Hello {name}! {secondMess}'.lower())
#     else:
#         print(f'Hello {name}! {secondMess}')
#
# testFunction('Test3', '')


# def memory_decorator(func):
#     cache = {}
#     def wrapper(*args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         cache[key] = func(*args, **kwargs)
#         print(cache)
#         return cache[key]
#     return wrapper
#
#
# @memory_decorator
# def sumNumbers(*args):
#     sumValue = 0
#     for num in args:
#         if isinstance(num, (int, float)):
#             sumValue += num
#         else:
#             raise ValueError(f'Элемент последовательности, не является числом: \'{num}\'')
#     return sumValue
#
# print(sumNumbers(1,2,3))
# print(sumNumbers(1,2,3,3,4,6))

# С классами

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#         print('__INIT__')
#     def __call__(self, *args, **kwargs):
#         print('__call__') # Класс превращаем в функцию
#         print(args)
#         self.__counter += 1
#         return self.__counter
#
# c = Counter()
# print(c(1,2,3,4))
# print(c())
# print(c())
# print(c())
# print(c())


# class MemoryDecorator:
#     def __init__(self, func):
#         self.func = func
#         self.cache = {}
#
#     def __call__(self, *args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         self.cache[key] = self.func(*args, **kwargs)
#         print(self.cache)
#         return self.cache[key]
#
# @MemoryDecorator
# def sumNumbers(*args, k = None):
#     sumValue = 0
#     for num in args:
#         if isinstance(num, (int, float)):
#             sumValue += num
#         else:
#             raise ValueError(f'Элемент последовательности, не является числом: \'{num}\'')
#     return sumValue
#
#
# memDec = MemoryDecorator(sumNumbers)
#
# # print(memDec(1,2,3,4))
# # print(memDec(1,2,3,4,6,7,8))
#
# pprint(sumNumbers(1,2,3))
# pprint(sumNumbers.cache)


# Класс декоратор, который будет содержать метод call и
# будет принимать в себя функцию возвращающую строки и сохранять в локальном массиве уникальные слова

class MemoryDecorator:
    result = []

    def __init__(self, func):
        self.func = func
        self.arr = []

    def __call__(self, *args, **kwargs):
        tempString = self.func(*args, **kwargs)
        self.find_unicString(tempString)
        print(self.arr)


    def find_unicString(self, String):
        tmpArr = String.split(' ')
        for word in tmpArr:
            if word not in self.arr:
                self.arr.append(word)


def funcWords(testString):
    symbol_to_remove = ',.!?'
    for symbol in symbol_to_remove:
        testString = testString.replace(symbol, '')
    return testString.lower()


a = MemoryDecorator(funcWords)

a('test sdfasdasd qdqwdsadasd')
a('1234')
a('test sdfasdasd qdqwdsadasd')
a('1234')
