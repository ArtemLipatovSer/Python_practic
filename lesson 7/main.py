# def hello(name): return f'Hello, {name}'
# def goodbye(name): return f'Goodbye, {name}'
#
# check = int(input('input 1 or 2'))
# if check == 1:
#     message = hello
# else:
#     message = goodbye
#
# print(message('Tom'))

# def one(a, b): return a + b
#
#
# def two(a, b): return a - b
#
#
# def three(a, b): return a * b
#
#
# def four(a, b): return int(a / b)
#
#
# check = int(input('1 - сложение \n'
#                   '2 - вычетание \n'
#                   '3 - умножение \n'
#                   '4 - деление \n'))
#
# if check == 1:
#     funResult = one
# if check == 2:
#     funResult = two
# if check == 3:
#     funResult = three
# if check == 4:
#     funResult = four
#
# print(funResult(10, 5))

# def sum(a, b): return a + b
# def multiply(a, b): return a * b
#
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f'Результат - {result}')
#
# def input_user_value():
#     num1 = int(input("Введите число: "))
#     num2 = int(input("Введите число: "))
#     check = int(input("Выберите: \n\t 1. Сложить, \n\t 2. Умножить\n\t -->"))
#     if check == 1:
#         func = sum
#     else:
#         func = multiply
#     return num1, num2, func
#
# num1, num2, operation = input_user_value()
# do_operation(num1, num2, operation)
#
#
# # Лямда выражения (присваивает функцию ниже, лямбда только возвращает значение)
# sum = lambda a,b: a+b

#
# def do_func(operation):
#     print('*******')
#     operation()
#     print('*******')
#
#
# do_func(lambda: print('Hello'))

#
# name = 'Tom'
#
# def say_hi():
# globale используем данные из глобальной области данных
#     global name
#     name = 'Egor'
#     print('Hello ', name)
#
# def say_bye():
#     print('Goodbye ', name)
#
# say_hi()
# say_bye()

# n = 3
# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         # Не используем локальную область данных
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
# outer()

#
# total = 0
#
# def calculate_total(a, b, c):
#     global total
#     total = total + a
#     total = total + b
#     total = total + c
#
# calculate_total(1, 2, 3)
# print(total)


# def outer():
#     n = 5
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

#
# def multiply(n):
#     def inner(m): return n * m
#     return inner
#
# fn = multiply(5)
# fn(2)
# print(fn(2))

# def average():
#     count_num = 0
#     sum_of_num = 0
#
#     def inner(num):
#         nonlocal count_num, sum_of_num
#         sum_of_num += num
#         count_num += 1
#         print(sum_of_num/count_num)
#     return inner
#
# fn = average()
# fn(1)
# fn(10)
# fn(10)


# Написать функцию с использованием замыкания, котрая принимала бы имя и фамилию в список и выводила на экран
# колличество дабавленных пользователей в весь список

def fioMan():
    countMan = 0
    people = list()
    def addMan(fio):
        nonlocal countMan, people
        people.append(fio)
        countMan += 1
        print('Список людей - ', *people, ',', '\n', 'Количество людей - ', countMan, '\n', sep='')
    return addMan

fn = fioMan()
fn('Смирнов Сергей')
fn('Петров Сергей')
fn('Журавлев Сергей')