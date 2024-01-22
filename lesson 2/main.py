# firstNumber = 10
# secondNumber = 11
# thirdNumber = 12

# print(firstNumber == secondNumber)
# print(firstNumber != secondNumber)
# print(firstNumber > secondNumber)
# print(firstNumber < secondNumber)
# print(firstNumber <= secondNumber)
# print(firstNumber >= secondNumber)

# print(firstNumber > secondNumber and secondNumber > thirdNumber)
# # логическое И
#
# print(firstNumber > secondNumber or secondNumber < thirdNumber)
# # логическое ИЛИ

# message = 'hello World'
# hello = 'hello'
#
# print(hello in message)
#
# print(hello not in message)
#
# print(type(message))

# a = 10
# b = 50
#
# if a > b:
#     print("True")
# elif a == b:
#     print("Равны")
# else:
#     print("False")

# firstNumber = int(input("Введите число"))
# if firstNumber % 2 == 0:
#     print(" Четное")
# else:
#     print(" Не четное")

# number = int(input("Введите число "))
# if number % 7 == 0 and number != 0:
#     print("Число кратно 7")
# else:
#     print("Число не кратно 7")

# number_1 = int(input("Введите первое число "))
# number_2 = int(input("Введите второе число "))
#
# if number_1 < number_2:
#     print(f"{number_2} больше")
# elif number_1 == number_2:
#     print("Числа равны")
# else:
#     print(f"{number_1} больше")

# firstNum = int(input("Введите первое число "))
# secondNum = int(input("Введите второе число "))
# check = int(input("что считаем(введите число "
#                   "\n\t 1. Площадь"
#                   "\n\t 2. Периметр\n"))
# print("*"*30)
#
# if check == 1:
#     print(f"\tS = {firstNum * secondNum}")
# elif check == 2:
#     print(f"\tP = {2*(firstNum + secondNum)}")
# else:
#     print(f'Такого варианта нет')
# print("*"*30)

# price = int(input("Введите стоимсоть приставки "))
# total = int(input("Введите количесвто приставок "))
# sale = int(input("Введите прицент скидки "))
#
# if 100 > sale > 0:
#     print(f'Стоимость всего заказа - {(price - ((price * sale)/100)) * total}\n'
#           f'Стоимость одной приставки с учетом скидки - {price - ((price * sale)/100)}')
# else:
#     print("Нет такой скидки")

# теренарный операнд
# a = 11
# # b = 0
# # if a > 10:
# #     b = 5
# # else:
# #     b = 10
# b = 10 if a > 5 else 7
# print(b)

# firstNum = int(input("Num 1: "))
# secondNum = int(input("Num 2: "))
#
# print(firstNum if firstNum > secondNum else secondNum)

# firstNum = int(input("Num 1: "))
# secondNum = int(input("Num 2: "))
#
# check = int(input("Что нужно сделать:\n"
#                   "1 - сложить\n"
#                   "2 - вычесть\n"))
# result = firstNum + secondNum if check == 1 else firstNum - secondNum
# print(result)

# luckyNum = input("введите шестизначное число ")
#
# if len(luckyNum) == 6:
#     firstPart = int(luckyNum[0])+int(luckyNum[1])+int(luckyNum[2])
#     secondPart = int(luckyNum[3])+int(luckyNum[4])+int(luckyNum[5])
#     result = "Счастливое" if firstPart == secondPart else "Обычное"
#     print(result)
# else:
#     print("error")

let = input("введите шестизначное число ")

if len(let) == 6:
    print(let[5]+let[4]+let[2]+let[3]+let[1]+let[0])
else:
    print("error")