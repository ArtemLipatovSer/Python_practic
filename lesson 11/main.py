import os
import json

# # Библиотека оперционной системы
# print(os.name)
# # Где находится файл который мы запускаем
# print(os.getcwd())
# # В этом репозитории можем создать папку
# # os.mkdir('test')
# # Выводит массив файлов репозитория
# print(os.listdir())
# Нормализация пути
# path = 'C:\\Users\\StepAdmin33\\Desktop\\lesson'
# print(os.path.normpath(path))
# # Справшивает дериктория это или нет
# print(os.path.isdir(path))
# # Это ярлык?
# print(os.path.islink(path))
# # Это файл?
# print(os.path.isfile(path))


# path = 'C:\\Users\\StepAdmin33\\Desktop\\lesson'
# print(os.getcwd())
# os.chdir(path)
# # Меняем путь
# print(os.getcwd())
# for i in range(1,10):
#     os.mkdir(f'{i}')
#     tmpPath = path + '\/' + str(i)
#     os.chdir(tmpPath)
#     for j in ['test1', 'test2']:
#         os.mkdir(j)
#     os.chdir(os.pardir)
# # Выше создали папки в папке

# Создали файл 1.txt
print(os.getcwd())
# Открывает файл для r - чтения, w - записи
# myFile = open('1.txt', 'w')
# myFile.write("Hello World")
# Выводим то что написали в пайтоне
myFile = open('1.txt', 'r')
print(myFile.read())

# Что то с файлом сделали затем его зразу закрыли
# with open('hello.txt', 'r') as somefile:
#     # # (здесь мы файлы перезаписываем, если мы поставим атрибут 'a' вместо 'w' то будем добавлять
#     # somefile.write('Hello World1!\n')
#     # somefile.write('Hello World2!\n')
#
#     # # Считываем содержимое
#     # for line in somefile:
#     #     print(line)
#
#     # Еще один способ считывания
#     # str1 = somefile.readline()
#     # print(str1)
#     # str2 = somefile.readline()
#     # print(str2)
#
#     # Еще один способ считывания
#     strs = somefile.read()
#     print(strs)


# Изменяем кодировку
# with open('hello.txt', 'r', encoding='utf-8') as somefile:
#     strs = somefile.read()
#     print(strs)


# Упражнения:
# Создали словарь с данными
dictList = [
    {'tittle': 'Tom',
     'text': 'Lorem ipsum',
     'author': 'Test User'},

    {'tittle': 'Tom2',
     'text': 'Lorem ipsum2',
     'author': 'Test User2'}
]
# Создаем части хтмл страницы
head = '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</head>
<body>
<div class="container" style="display:flex; flex-wrap:wrap; gap:15px">'''

footer = '''</div>
</body>
</html>'''


# В одну из часте засовываем данные из словаря
def createBody(info):
    body = ''
    for value in info:
        body += f'''<div class="card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">{value['tittle']}</h5>
                    <p class="card-text">{value['text']}</p>
                    <a href="#" class="btn btn-primary">{value['author']}</a>
                </div>
        </div>'''
    return body


def outputData(info):
    with open('index.html', 'w') as file:
        file.write(head + createBody(info) + footer)


# outputData(dictList)


# Подключаем библиотеку json
def writeData(info):
    dictInfo = {'articles': info}
    with open('db.json', 'w') as file:
        json.dump(dictInfo, file)


# writeData(dictList)


def readData():
    try:
        with open("db.json", 'r') as file:
            data = json.load(file)
        return data['articles']
    except:
        with open('db.json', 'w') as file:
            json.dump({'articles': []}, file)


if __name__ == '__main__':
    check = int(input('1. Запись\n2. Выгрузка'))
    if check == 1:
        data = readData()
        data.append({'tittle': input('введите название->'),
                     'text': input('text->'), 'author': input('author->')})
        writeData(data)
    elif check == 2:
        data = readData()
        outputData(data)
    else:
        print('Такой команды нет')
# print(readData())
