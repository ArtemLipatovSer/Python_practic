# def greet():
#     print('Hello, Tom')
#
# greet()
#
# def greet(a, b):
#     print(a+b)
#
# greet(10, 11)

# def rangeNumber(*,b, a = 1, word):
#     # звездочка для того что бы аргументы приходили именованные
#     arr = list(range(a,b))
#     for i in arr:
#         if i % 2 != 0:
#             print(i, end=' ')
#     print(word)
#
# rangeNumber(10)
# rangeNumber(10, 1)
# rangeNumber(a = 10, b = 13)
# def printParams (name, /, age, company = 'microsoft'):
#     print(f'{name, age, company}')
#
# printParams('Tom', age=13, company='google')

# def sum(*numbers):
#     # такая звездочка говорит о неограниченном количестве аргументов
#     print(numbers)
#
# sum(1,2,3)
#
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(result)
#
# sum(1,2,3,4)
#
# sum(1,2,3)
#
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     return result
#
# a = sum(1,2,3,4,5)
#
# print(a)

# def factor(num):
#     result = 1
#     if num == 0:
#         return 1
#     else:
#         for i in range(1, num+1, 1):
#             result *= i
#         return  result
#
# print(factor(5))

# функция принимает 4 числа и выводит максимальное из них

# def maxNumber(*num):
#     return max(num)
#
# print(maxNumber(1,20,3,4,33,105))

def funnyNumber(*num):
    part = 3
    partLeft = 0
    partRight = 0
    if len(num) % 2 != 0:
        return 'Число не может быть счастливым'
    else:
        part = int(len(num) / 2)
        for i in range(part):
            partLeft += num[i]
        for i in range(len(num), part, -1):
            partRight += num[i-1]
        if partLeft == partRight:
            return 'Число счастливое'
        else:
            return 'Число не счастливое'

print(funnyNumber(1,2,3,11,7,8))