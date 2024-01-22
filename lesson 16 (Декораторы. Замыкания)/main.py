# Замыкание в функции для примера

# def say_name(name):
#     print('Начало выполнения')
#
#     def say_goodby():
#         print('Goodbye', name)
#
#     return say_goodby
#
# f = say_name('Tom')
# f()
# f()

# # Счетчик методом замыкания
# def outer():
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(n)
#
#     return inner
#
# fn = outer()
# fn()
# fn()
# fn()
# f = outer()
# f()
# f()

# # Тот же счетчик только классом
# class OuterClass:
#     def __init__(self):
#         self.n = 0
#
#     def inner(self):
#         self.n += 1
#         print(self.n)
#
# Cls = OuterClass()
# Cls.inner()
# Cls.inner()
# Cls.inner()

# def multiply():
#
#     n = 2
#     def inner():
#         nonlocal n
#         n *= 2
#         return n
#     return inner
#
# f = multiply()
# print(f())
# print(f())
# print(f())

#
# def multiply(n):
#     def inner(m):
#         return n * m
#     return inner
#
# f = multiply(2)
# print(f(5))
# print(f(6))
# print(f(7))


# # Генерация паролей
# import random
# import string
#
#
# def password_gen(length):
#     def gen_pass():
#         characters = string.ascii_letters + string.digits + string.punctuation
#         password = ''.join([random.choice(characters) for i in range(length)])
#         print(password)
#
#     return gen_pass
#
#
# fn = password_gen(8)
# fn()
# fn()


# # Самостоятельный пример
# def calc(z, num):
#     res = 0
#
#     def result(a):
#         nonlocal res
#         if z == '+':
#             res = num + a
#         elif z == '-':
#             res = num - a
#         else:
#             return 'Error'
#         return res
#     return result
#
#
# f = calc('*', 10)
#
# print(f(5))

#                                         # ДЕКОРАТОРЫ
#
# def func_decorator(func):
#     def wrapper(*args, **kwargs): # Любая последовательность аргументов и любая последовательность неименованных аргументов
#         print('*'*10)
#         func(*args, **kwargs)
#         print('*'*10)
#     return wrapper
#
# @func_decorator
# def test():
#     print('Hello World')
#
# @func_decorator
# def test2(name):
#     print('Hello everyone', name)
#
# # f = func_decorator(test)
# # f()
# #
# # f2 = func_decorator(test2)
# # f2()
#
# test() # Помечаем в самой функции над ней @func_decorator и он автоматом ее присваивает, без дополнительной инициализации
#
# test2('Tom')

import time
import sys
sys.setrecursionlimit(30000000)

def testTime(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        dt = time.time() - st
        print(f'Время работы - {dt}')
        return res
    return wrapper

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# print(time.time())
# time.sleep(5)
# print(time.time())

fn = testTime(factorial)

fn(100000)
