# class Person:
#     name = 'Tom'
#
#     def hello(self):  # Self обозначает то что функция принадлежит объекту
#         print('hello world', Person.name)

# class Person:
#     pass
#
# a = 1
# tom = Person() # Происходит инициализация объекта
# print(type(a))
# print(type(tom))


# class Person:
#     # name = 'Tom'
#     def __init__(self):  # Конструктор, кторый создает объекты внутри класса
#         self.name = 'Tom'
#         self.age = self.get_age()
#
#     def hello(self, atr):  # Методы класса # Если мы хотим передать какие-то параметры, делаем это через запятую
#         print('hello world', self.name, f'Возраст {self.age} ' + str(atr))
#
#     def get_age(self):
#         return int(input('Введите возраст: '))
#
#     def __del__(self): # Метод удаления класса
#         print('Удаление класса', str(self))
#
#
# tom = Person()
# tom.hello('12345')
# tom.name = 'Kate'
# tom.hello('12345')
# del tom
# print('Test')  # Класс удаляется в последнюю очередь, чтобы этого не происходило нужно удалить принудительно (del tom)


# Задание (принимать числитель, знаменатель и выводить значение)

# class Drob:
#     def __init__(self, chisl, znam):
#         self.chisl = chisl
#         self.__znam = znam   #self.set_znam(znam) # Если в знаменателе будет 0, от этого нужно перестраховаться методом ниже
#
#     # Натация проперти что-бы обратиться к значению
#     @property
#     def znam(self):
#         return self.__znam # Это самый простой Get-ЕР
#     # Инкапсуляция
#     @znam.setter
#     def znam(self, znam): # Сеттер без гетера работать не будет, он не понимает что такое знам, потому что он закрытый
#         if znam != 0:
#             self.__znam = znam
#         else:
#             print("Неверно")
#
#     def outputTenNumeric(self):
#         return self.chisl / self.__znam
#
#     def __str__(self): # Выводить информацию о класса, когда мы начинам принтить
#         return f'{self.chisl} \n-\n{self.__znam}'
#
#     def integerNum(self):
#         return f'Количество целых чисел = {self.chisl // self.__znam}'
#
#
# a = Drob(5, 1)
# # 0 может быть появится здесь a.znam = 0, нужно запретить обращаться к знаменателю в классе
# a.znam = 0
# print(a)
# print(a.outputTenNumeric())
# print(a.integerNum())

# задание: создать класс персон (name, age), сделать сеттер на свойство age

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age != 0:
#             self.age = age
#         else:
#             print("Неверно")
#
#     def printInfo(self):
#         return self.name, self.age
#
# a = Person('Tom', 12)
# a.age = 0
# print(a.printInfo())

# Сеттер - изменение
# Геттер - получение


# # Переписание функции (перегруз), называется оверрайд
# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print(f'Имя пользователя: {self.__name}')
#
# tom = Person('Tom')
# tom.display_info()
#
# class Employee(Person):
#     # def __init__(self, name):
#     #     self.__name = name
#     #
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # def display_info(self):
#     #     print(f'Имя пользователя: {self.__name}')
#     def __init__(self, name, company):
#         super().__init__(name) # Вызываем инити родительского класса от которого наследуемся
#         self.company = company #Вызываю класс который нужен
#
#     def display_info(self):
#         super().display_info()
#         print('____________________') # Добавили к функции то что нужно
#     def work(self):
#         print(f'{self.name} - работает в {self.company}') # Чтобы не переписывать все можно сделать иначе, наследоваться от предыдущего класса
#
# kate = Employee('Kate', 'Google')
# kate.display_info()
# kate.work()

# Наследования нескольких классов
# class Worker:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
#     def works(self):
#         print(f'{self.name} works')
#
# class Student:
#     def __init__(self, name):
#         self.__name = name
#     @property
#     def name(self):
#         return self.__name
#     def study(self):
#         print(f'{self.name} study')
#
# class WorkingStudent(Worker, Student):
#     def __init__(self, name, college): # Наследовали и добавили новый метод
#         super().__init__(name)
#         self.college = college
#     def studyWorks(self):
#         self.study()
#         super().works() # Методы которые мы инициализируем в этом методе пишем через селф, функции которые мы инициализируем из другого класса пишем через супер
#     def study(self):
#         print(f'{self.name} study in {self.college}')
#
# tom = WorkingStudent('Tom', 'Harvard')
# tom.works()
# tom.study()

# class Test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#
# class Test2(Test):
#     pass
#     def __init__(self, a, b):
#          super().__init__(a, b)
#
# one = Test2(1, 2)
#
# print(one.sum())
# print(one.__dict__)


# num = (x for x in [1,2,3,4,5])
# print(type(num))
# a = list(num)
# print(a)
# print(num)
# b = list(num)
# print(num)
# print(b)
#
# abc = list()
# for i in range(5):
#     abc.append(i)
#
# print(abc)
# print(abc[2])


