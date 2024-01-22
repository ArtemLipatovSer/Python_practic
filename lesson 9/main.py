# print('Начало программы')
#
# try:
#     string = '5'
#     number = int(string)
#     print(number + 5)
# except:
#     print('Преобразование прошло неудачно')
# finally:
#     print("Блок Try завершился")
# print('Конец программы')

# try:
#     number = int(input("Введите число "))
#     print('10 / Введенное число -->', "10"/number)
# except ValueError:
#     print('Преобразование прошло неудачно')
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except BaseException:
#     print('Не предусмотренная ошибка')
# # Выделяет ошибка по их типу, если такой тип не указан то высвячивается отработка ошибки общая BaseEx... (то же что и просто except)

# try:
#     number = int(input("Введите число "))
#     print('10 / Введенное число -->', "10"/number)
# except BaseException as e:
#     print('Не предусмотренная ошибка',e)
# # as e указывает что за ошибка

# try:
#     number = int(input("Введите число "))
#     if number == 0:
#         raise Exception('На ноль делить нельзя')
#     print('10 / Введенное число -->', 10/number)
# # except BaseException as e:
# #     print('Не предусмотренная ошибка',e)
# except Exception as e:
#     print(e)

# import user_fulFanc

# num = user_fulFanc.user_input()
# print(num)
# Импортируем все но нужно указывать метод вызова

# from user_fulFanc import print_hello
# num = print_hello()
# print(num)
# импортируем только что то выбранное

# from user_fulFanc import *
# num = print_hello()
# # Инпортируем все без вызовов методов

# from collFunc.user_fulFanc import *
# num = print_hello()
# # Если лежит в другой папке то в строке импорта мы должны прописать папку через точку

# import collFunc.user_fulFanc
#
# num = collFunc.user_fulFanc.print_hello()

# import random

# number = random.random()
# print(number)
#
# number = random.randint(1,1000)
# print(number)
# # Рандом целых чисел
#
# number = random.randrange(10,100,2)
# print(number)
# # Рандом чисел с шагом два (четные числа)

# a = [i for i in range(1,10)]
# random.shuffle(a)
# print(a)
# # Перемешивание массива

import requests

r = requests.get('https://jsonplaceholder.org/posts/1')
print(r.text)

a = r.json()
print(a['slug'])
