class Human:

    def __init__(self, name, age):
        self.set_age(age)
        self.set_name(name)

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name



    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name

    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 100:
            self.__age = age

if __name__ == '__main__':
    semen = Human(name='Semen', age=25)
    print(semen.get_name())
    print(semen.get_age())
