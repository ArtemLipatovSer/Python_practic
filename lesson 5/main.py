# # text = 'hellow world'
# #
# # print(text[0])
# # print(text[-1])
# #
# # text = '''hellow
# # world'''
# # print(text)
#
# # text = 'hello World'
# # print(text[0:5:1])
# # # с нуля до пятого элемента с шагом 1
#
# # text = ['hello World!', 'hello World.', '132456?']
# #
# # for index, elem in enumerate(text):
# #     text[index] = elem[0:-1:1]
# # print(text)
# # # удаление знаков препинания
#
# text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et ' \
#        'dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet ' \
#        'clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, ' \
#        'consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, ' \
#        'sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea ' \
#        'takimata sanctus est Lorem ipsum dolor sit amet.'
#
# # arrText = text.split('. ')
# # print(arrText)
# #
# # for elem in arrText:
# #     print(elem.lower())
# # #     текст в нижним регистре
# # print(elem.upper())
# # #     текст в верхнем регистре
#
# arrText = text.split(' ')
# # print(arrText)
# # for i in range(0,len(arrText), 1):
# #     arrText[i] = arrText[i][0].upper() + arrText[i][1::1]
# #
# # print(arrText)
#
# # for i, elem in enumerate(arrText):
# #     arrText[i] = list(arrText[i])
# #     for j in range(len(arrText[i])):
# #         if j % 2 == 0:
# #             arrText[i][j] = arrText[i][j].lower()
# #         else:
# #             arrText[i][j] = arrText[i][j].upper()
# #     arrText[i] = ''.join(arrText[i])
# # print(' '.join(arrText))
#
# text = 'hellow World'
# print(text.isalpha())
# # Проверка строки на дургие символы, если только алфавитные то будет тру, если что то другое в том числе проблем, то фолсе
# print(text.islower())
# # Проверка на нижний регистр, если один высокий то фолсе иначе тру
# print(text.isupper())
# # Проверка на нижний регистр
#
# text2 = '123465'
# print(text2.isdigit())
# print(text2.isnumeric())
# # Проверка на цифры
#
# text3 = 'title'
# print(text3.title())
# # Заглавная буква

# welcome = 'Hellow world! world'
# index = welcome.find('wor')
# print(welcome[index:index+3])

# phone = ' +7(800)555-75-35 '
# edit_phone = phone.replace('-', '')
# edit_phone = edit_phone.replace('(', '')
# edit_phone = edit_phone.replace(')', '')
# edit_phone = edit_phone.replace('7', '8', 1)
# # заменяю старый символ на новый. Последняя единица говорит сколько нужен менять, если бы у нас были еще семерки в номере они тоже бы поменялись
# print(edit_phone)
#
# print(edit_phone.count('5', 1, 6))
# # Количество вхождений от и до либо везде
#
# print(edit_phone.strip())
# # удаление пробелов, стрип - везде, lstrip - в конце, rstrip - в начале


# text = 'hello world! Goodby!'
# print(text.startswith('hello'))
# print(text.endswith('!'))
# # Начало строки с чего то либо конец строки чем то

# text = input('Введите строку: ')
#
# numDigit, numString = 0, 0
#
# for elem in text:
#     if elem.isdigit():
#         numDigit += 1
#     elif elem.isalpha():
#         numString += 1
# print(f'Кол-во букв - {numString}; \nКол-во цифр - {numDigit}')

# text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et ' \
#        'dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet ' \
#        'clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, ' \
#        'consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, ' \
#        'sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea ' \
#        'takimata sanctus est Lorem ipsum dolor sit amet.'
#
# arrText = text.split('. ')
#
# element = input('Что искать: ')
#
# print(f'Количество вхождения во всем тексте - {text.count(element)}')
#
# for index, el in enumerate(arrText):
#     print(f'В предложении № {index+1} вхождений - {el.count(element)}')
#
# userText = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore ' \
#            'et dolore magna aliquyam erat, sed diam voluptua.'
# userInput = input('find-->')
#
# if userText.count(userInput) != 0:
#     changeInput = input('change-->')
#     changeText = userText.replace(userInput, changeInput)
#     print(changeText)
# else:
#     print('--> ERROR')
import random

a = [random.randint(1, 10) for i in range(10)]

# for i in range(10):
#     a.append(random.randint(1,10))
print(a)

[print(random.randint(1, 10) for i in range(10))]
