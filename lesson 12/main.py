                                        # Модуль Pickle / Работа с файлами

# user = {'name': 'Tom', 'age': 20}
#
# FILENAME = 'text.txt'
# # with open(FILENAME, 'w') as file:
# #     file.write(user['name'] + '-' + str(user['age']))
# #
# user2 = {}
# with open(FILENAME, 'r') as file:
#     text = file.readline()
#     user2['name'], user2['age'] = text.split('-')
#     print(user2)
#     # Если убрать тире, получится ошибка

import pickle

FILENAME = 'test2.dat'

# name = 'Tom'
# age = 16

# Запись бинарным кодом
# with open (FILENAME, 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
# # Читаем что создали
# with open (FILENAME, 'rb') as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
# print(name, type(age))


users = ['Tom', 16]
with open (FILENAME, 'wb') as file:
    pickle.dump(users, file)

with open (FILENAME, 'rb') as file:
    users = pickle.load(file)
print(users)
# Особенность этого метода работы с файлом - то что мы записали, то и выводим с сохранением типов данных.