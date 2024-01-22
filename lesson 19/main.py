class Anton:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        if name == 'Антон':
            self.name = name
        else:
            print(f'Я не {name}, я Антон')
            self.name = 'Антон'
        self.age = age

    def infoPrint(self):
        print(f'Я {self.name}, мне {self.age}')


a = Anton("123", 13)

a.infoPrint()
