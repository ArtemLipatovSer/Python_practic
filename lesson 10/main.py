                                            # Множества
# users = {'Tom', 'Bob', 'Alice', 'Tom'}
# # могут быть только уникальные значения, повторяющихся не может быть.
# # Нет привязки к элементам, элементы расположены хаотично
# print(users)
# print(len(users))

# Второй способ создания множетсв:
# users = set()
# print(users)
# # Добавить элементы
# users.add('Sam')
# users.add('Tom')
# users.add('Sam')
# print(users)
# # Удалить элементы
# users.remove('Tom')
# print(users)
# delUser = 'Sam'
# if delUser in users:
#     print('123')
# Второй метод удаления
# users = {'Tom', 'Bob', 'Alice'}
# users.discard('Tom')
# print(users)
# users.clear()
# print(users)

# перебераем множество
# Множнство меняет положение элементов постоянно
# users = {'Tom', 'Bob', 'Alice'}
# for user in users:
#     print(user)
#
# # Копирование множества
# users2 = users.copy()
# users2.remove('Alice')
# print(users, users2)

# users = {'Tom', 'Sam', 'Alice'}
# users2 = {'Bob', 'Kate', 'Tom'}
# # # Объединение множеств
# users3 = users.union(users2)
# print(users3)
# # Пересечения множеств
# users3 = users.intersection(users2)
# # Перезаписть текущего множества
# users.intersection_update(users2)
# print(users, users3)

# # Разность множеств (обираем общие элементы)
# users = {'Tom', 'Sam', 'Alice'}
# users2 = {'Bob', 'Kate', 'Tom'}
# # Первый способ
# # users.difference(users2)
# # print(users.difference(users2))
# # users.difference_update(users2)
# # print(users)
# # Второй способ
# print(users - users2)
#
# # Итерированная разность, добавляется все кроме пересекаемых
# print(users ^ users2)
# print(users.symmetric_difference(users2))
# users.symmetric_difference_update(users2)
# print(users)

# Задание 1
# number = [int(num) for num in input().split()]
# newSet = set()
# for elem in number:
#     if elem in newSet:
#         print('Yes')
#     else:
#         print('No')
#         newSet.add(elem)
# print(newSet)

# # Задание 2
# text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore ' \
#        'magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo ' \
#        'consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.' \
#        ' Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# text = [word.lower() for word in text.split()]
# print(text)
# wordSet = set()
# # for word in text:
# #      wordSet.add(word)
# [wordSet.add(word) for word in text]
# print(f'Исходные данные {len(text)} --- Уникальные элементы {len(wordSet)}')

# user = {'Tom', 'Bob', 'Alice', 'Kate', 'Ann'}
# user2 = {'Tom', 'Bob'}
# # Явлеятся ли подмножество множеством
# print(user2.issubset(user))
# # А в множество входит что то еще (все ли в юзер2 входит в юзер)
# print(user.issuperset(user2))

# # Ограниченное множество для секьюрити
# users = frozenset({'Tom', 'Tim', 'Alice'})
# # В этом множестве нельзя применить метод адд, что-то из него удалить, объединить с дургим, метод update и тд
# print(users)
# users2 = {'Tom', 'Sam'}
# # Можно сделать так, но возвращается новый объект
# print(users - users2)
# print(users)

# Упаковка и распаковка
# # Первый способ распаковки
# x, y = 1, 2
# print(f'{x=},{y=}')
# x, y, z = 1, [2,3,4], 98
# print(f'{x=},{y=},{z=}')
# Распкаковка словарей
# x,y,z = {'red':'красный', 'blue':'синий', 'green':'зеленый'}
# print(f'{x=},{y=},{z=}')
# x,y,z = {'red':'красный', 'blue':'синий', 'green':'зеленый'}.items()
# print(f'{x=},{y=},{z=}')
# # распаковка во время цикла
# dict = {'a':1000, 'b':2000, 'c':3000}
# for key,elem in dict.items():
#     print(f'{key=}, {elem=}')

# arr = [('Tom',38, 'Google'), ('Bob', 27, 'Amazon'), ('Alice', 25, 'Cisco')]
#
# for name,age,company in arr:
#     print(f'{name=}, {age=}, {company=}')

# for elem in enumerate([1,2,3,4,5,6,7]):
#     print(elem)
#
# people = ('Tom', 38, 'Google')
# name,_,company = people
# print((_))

# # Упаковка
# num = 1
# num2 = 2
# num3 = 3
#
# numbers = num, num2, num3
# print(numbers)
# # Если добавим звездочку и numbers - тогда создаем массив
# *numbers, = num, num2, num3
# print(numbers)
# # магические звезды
# head, *tail = [1,2,3,4,5,6,7,22]
# print(head)
# print(tail)

# x,*y,z = {'red':'красный', 'blue':'синий', 'green':'зеленый', 'yellow':'желтый'}
# print(x)
# print(y)
# print(z)

# num1 = [1,2,3]
# num2 = [4,5,6]
#
# num3 = [*num1, *num2]
# print(num3)
#
# dict1 = {'red':'красный', 'blue':'синий'}
# dict2 = {'green':'зеленый'}
# dict3 = {*dict1, *dict2}
# print(dict3)
# dict3 = {**dict1, **dict2}
# print(dict3)

# распаковка функции
# def fun(*args):
#     print(args)
#
# fun(1,2,3)

# def fun(**args):
#     print(args)
#     for key,elem in args.items():
#         print(key,elem)
# fun(lg1=1,lg2=2,lg3=3)

tom = {'name': 'Tom', 'age': 34, 'company': 'yandex'}

def print_person(name, age, company):
    print(f'Neme: {name}\n'
          f'Age: {age}\n'
          f'Company: {company}')

print_person(**tom)

