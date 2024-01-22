from pprint import pprint

# tom = ('Tom', 23)
# print(tom)


# tom = 'Tom', 23
# print(tom)

# test = ['Google', "Yandex"]
# newTuple = tuple(test)
# print(newTuple[0])

# a, b, c = (1,2,3)
# print(a)
# print(b)
# print(c)

# test = ('Tom', 37, 'Google', 'Software developer')
# name, age = test[0:2]
# print(name)
# print(age)

# def print_person(name, age, company):
#     print(f'Name - {name}\nAge - {age}\nCompany - {company}')
# print_person('Tom', 37, 'Google')
# bob = ('Bob', '25', 'Amazon')
# print_person(*bob)

# user = {
#     'name': 'Tom',
#     'age': 20,
#     'company': 'Cisco',
# }
# print(user['name'])
# for key in user:
#     print(f'Ключ - {key}, элемент - {user[key]}')

# telBook = {'Tom': 999, 'Bob': 456, 'Sem': 789, 'Sid': 888}
# [print(key, telBook[key]) for key in telBook]
# for key, value in telBook.items():
#     print(key, value)
# for value in telBook.values():
#     print(value)
# print(telBook)
# print(telBook)
# print(telBook.get('Ram', 'unknown user'))
# get предохраняет от ошибки
# pprint(telBook)
# # del telBook['Sid']
# pprint(telBook)
# # del telBook['Sid']
# # del если удалить элемент которое нет, вылезет ошибка, с поп будет замещаться словом соотвествующим
# Sid = telBook.pop('Sid')
# Sad = telBook.pop('Sad', 'нет')
# # pop удалить элемент
# print(Sid)
# print(Sad)
# pprint(telBook)
# telBook.clear()
# # clear очистить словарь
# print(telBook)

# users = {'Tom': 999, 'Bob': 456, 'Sem': 789, 'Sid': 888}
# student = users.copy()
# # student['Sem'] = 777
# # print('Студенты', student)
# # print('Юзеры', users)
# student['Ram'] = 777
# print(student)
# users.update(student)
# print(users)
# # Update сли словари совпадают то происходит объединение. Элементы те кторые есть в словари они перезаписываются, элементы которых нет добавляются

dict1 = {
    'яблоки': 100,
    'имоны': 60,
    'малина': 250,
}
def find_price(arr, key):
    return arr.get(key, "Такого нет")

def output(arr):
    for key, value in dict1.items():
        print(key, value)

def addProd(arr):
    # goods = (
    #             (
    #                 input('Введите название '),
    #                 int(input('Введите стоимость '))
    #             ),
    #         )
    # goods2 = dict(goods)
    goods2 = {input('Введите название '): int(input('Введите стоимость '))}
    arr.update(goods2)
    print(arr)
def main():
    check = int(input('Что будем делать?\n\t'
                      '1. Узнать цену товара\n\t'
                      '2. Вывести асортимент\n\t'
                      '3. Добавление товара/изменение товара\n'))
    if check == 1:
        print(find_price(dict1, input('Введите название товара\n').lower()))

    elif check == 2:
        output(dict1)

    elif check == 3:
        addProd(dict1)


main()


