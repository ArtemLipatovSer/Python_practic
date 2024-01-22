# num = int(input("введите число: "))
#
# for i in range(1, 10):
#     for j in(range(1, 10)):
#         print(f'{i} * {j} = {j * i}')
#     print('*' * 10)

# a = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
# print(a[1][2])
#
# for i in range(len(a)):
#     # print(a[i])
#     for j in range(len(a[i])):
#         print(a[i][j])

# for i in a:
#     for j in i:
#         print(j)

# a = 7
# b = 8
#
# a, b = b, a
#
# print (a, b)

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# for i in range(len(a)):
#     print('*' * 10)
#     # for j in range(len(a[i])):
#     #     print(a[j][i])
#     for j in range(i+1, len(a[i])):
#         a[i][j], a[j][i] = a[j][i], a[i][j]
#
# for el in a:
#     print(el)
# a = [11, 22, 33, 44, 55, 66, 77]
# for i, row in enumerate(a):
#     print(row)

# numbers = [1, 2, 3, 4, 5]
# print(min(numbers))
# print(max(numbers))
# numbers.append(3223)
# numbers.insert(2, 'hellow')
# numbers.extend(['Запихнуть', 'в конец списка'])
# numbers.remove(2)
# print(numbers)
# # numbers.clear()
# # print(numbers)

# a = [1, 2, 3, 4, 3, 6, 8, 8, 9]
#
# while True:
#     check = int(input(f'1. Посмотреть массив\n'
#                       f'2. Добавить элемент\n'
#                       f'3. Удалить элемент\n'))
#     if check == 1:
#         print(a)
#     elif check == 2:
#         a.append(int(input("Что хотите добавить? ")))
#     elif check == 3:
#         remCheck = int(input(f"1. Удалить все\n"
#                              f"2. Первое вхождение\n"))
#         elem = int(input("Что удалить? "))
#         if a.count(elem) >=1:
#             if remCheck == 1:
#                 while a.count(elem) != 0:
#                     a.remove(elem)
#             elif remCheck == 2:
#                 a.remove(elem)
#         else:
#             print('Нет такого элемента')
#     if input('Хотите выйти?(y/n) ') == 'y':
#         break
#
#
#
# # Количество элементов a.count(1) - сколько единиц в массиве
# # Узнать индекс  a.index(1) 1 - значение

# a = [1, 2, 3, 4, 5, 6, 7]
# # a.reverse()
# # b = a.copy()
# # b.reverse()
# # print(a)
# # print(b)
# a.pop(2)  # Удаление элемента по индексу
# print(a)
# Очередь
# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a.insert(0, int(input('>')))
# print(a)
# # a.pop()
# b = a.pop()
# print(a)
# print(b)

# a = []
# a.insert(0, 1)
# print(a)
# a.insert(0, 2)
# print(a)
# a.insert(0, 3)
# print(a)
# a.pop(0)
# print(a)
# a.pop(0)
# print(a)

import random

numOfArray = int(input("Введите количество элементов: "))
arr = list()
sumMin = 0
multi = 1

for i in range(numOfArray):
    arr.append(random.randint(-100, 100))
print(arr)

for i in arr:
    if i < 0:
        sumMin += i

# for i, el in enumerate(arr):
#     if i % 3 == 0:
#         multi += el

for h in range(3, len(arr), 3):
    multi *= arr[h]
    print(h)
# print(sumMin)
print(multi)




