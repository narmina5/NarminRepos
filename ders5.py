class Car:  # class not located in memory // class names should start w/ a capital letter
    # color = None  # static property
    # wheel = 4
    # doors = 4
    def __init__(self, model, color, wheel, doors) -> None:
        self.color = color
        self.model = model
        self.wheel = wheel
        self.doors = doors

    def get_info(self):
        return f"Model: {self.model}\nColor: {self.color}\nWheel: {self.wheel}\nDoors: {self.doors}"


tesla = Car("Tesla", "blue", 4, 2)  # object (instance)
bmw = Car("BMW", "black", 4, 4)
print(tesla.model, tesla.color)
print(tesla.model, tesla.wheel)
print(tesla.get_info())

print(bmw.model, bmw.color)
print(bmw.model, bmw.wheel)
# print('=========================================')
print(bmw.get_info())


# '========================================='


class USA:

    def get_capital(self) -> str:
        return 'Washington DC'


class India:

    def get_capital(self) -> str:
        return 'New Delhi'


usa = USA()
india = India()

countries = [usa, india]
for country in countries:
    print(country.get_capital())
# '========================================='

# ENCAPSULATION encapsulates(meaning will make it unreachable)
# some property of a class: .__desc means it's made private


class Academy:
    def __init__(self):
        self.name = "Developia - a"  # is public to everyone (is public)
        self._number = 32  # is public but can't (technically can) be modified (protected member)
        self.__desc = "Developia "  # should NOT change (is private)

    def _get_secret_id(self):
        return 'SECRET ID'


a = Academy()
print(a._number)
# example for modif:
a._number = 42
print(a._number)
a.__desc = 'yeni deyer'  # just print(a.__desc) will give an error
print(a.__desc)
print(a.name)
print(a._get_secret_id())  # we delete one of the _ in front
# '========================================='
