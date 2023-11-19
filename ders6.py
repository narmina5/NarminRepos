# PYTHON INHERITANCE:
class Person:
    def __init__(self, name, surname, height, weight, age):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight
        self.age = age

    def get_physical_properties(self):
        return f'Height: {self.height}\nWeight: {self.weight}'


class Employee(Person):
    def __init__(self, name, surname, height, weight, age, salary, position):
        super().__init__(name, surname, height, weight, age)
        self.salary = salary
        self.position = position


ehmed = Employee('Ehmed', 'Aliyev', 179, 78, 28, 4500, 'Tech Lead')
print(ehmed.get_physical_properties())

# Abstract class:
# eShopper. mütləq ABC -dən inherit olunmalıdı.

# 2. mütləq ən azı eShopper dənə abstractmethod - u olmalıdı.

# 3. abstract class-ın bir başa instance-ı yaradıla bilməz.

# 4. abstract class-dan törənən (inherit edilən) class-ın içərisində, abstract class-da olan
# bütün abstractmethod-lar istifadə edilməlidir.

# TASKS (DAY 7):
# 01
class Car:
    speed = None
    wheel = None
    door = 4


tesla = Car()
tesla.door = 2
print(tesla.door)

bmw = Car()
print(bmw.door)


# 02
class Person:
    def __init__(self, name, surname, age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}'

    # 03
    def get_age(self):
        return self.age


ali = Person('Ali', 'Huseynzade', 33)
print(ali.get_age())


# 04
class Employee(Person):
    def __init__(self, name, surname, age, salary) -> None:
        super().__init__(name, surname, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


memmed = Employee('Memmed', 'Eliyev', 42, 1600)
print(memmed.get_salary())


# TASKS (DAY 7 (class-lar tekrar)):
# 01
class Computer:
    def __init__(self, category, color, ram, camera, os):
        self.category = category
        self.color = color
        self.ram = ram
        self.camera = camera
        self.os = os

    def get_os_and_category(self):
        return f'Category: {self.category}\nOs: {self.os}'

    def get_info(self):
        return f'Category: {self.category}\nColor: {self.color}\nRam: {self.ram}\nCamera: {self.camera}\nOs: {self.os}'

    def set_info(self, new_ram):
        self.ram = new_ram


macOS = Computer('PC', 'silver', '16', 'None', 'Mac OS')
print(macOS.get_info() + '\n')
print(macOS.get_os_and_category())
macOS.set_info(32)
print(macOS.get_info())


# 02
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nAge: {self.age}'

    def get_name(self):
        return self.name


class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Teacher(Employee):
    def __init__(self, name, surname, age, salary, status):
        super().__init__(name, surname, age, salary)
        self.status = status

    def get_status(self):
        return self.status


narmin = Teacher('Narmin', 'Mailova', '20', '5000', 'developer')
print(narmin.get_name(), '-', narmin.get_status())


# 03
class Bird:
    def __init__(self, voice):
        self.voice = voice

    def get_sound(self):
        return 'X'


class Sparrow(Bird):
    def __init__(self, voice):
        super().__init__(voice)

    def get_sound(self):
        return 'Y'


class Swan(Bird):
    def __init__(self, voice):
        super().__init__(voice)

    def get_sound(self):
        return 'Z'


class Eagle(Bird):
    def __init__(self, voice):
        super().__init__(voice)


bird = Eagle('alarm')
print(bird.get_sound())  # get_sound-u override etmir deye output base class-dan olacaq: X


# 04
class A:
    def __init__(self):
        self.__x = 'x'

    def get_info(self):
        return self.__x

    def set_x(self, new_value):
        self.__x = new_value


a = A()
a.__x = 'y'
print(a.__x)
a.set_x('z')
print(a.get_info())


# TASKS (DAY 7 (davami)):
# 01
class Circle:
    def get_area(self) -> int:
        return 30


class Rectangle:
    def get_area(self) -> int:
        return 64


circle = Circle()
rectangle = Rectangle()

shapes = [circle, rectangle]
for shape in shapes:
    print(shape.get_area())


# 02 (TEKRAR)
class A:
    def __init__(self):
        self.__x = 'x'

    def get_info(self):
        return self.__x

    def set_x(self, new_value):
        self.__x = new_value


a = A()
a.__x = 'y'
print(a.__x)
a.set_x('z')
print(a.get_info())


# 03
class Robot:
    def __init__(self, name, model, manufacturer, battery_level):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.battery_level = battery_level

    def get_info(self):
        return f'Name: {self.name}\nModel: {self.model}\nManufacturer: {self.manufacturer}\nBattery level: {self.battery_level}'

    def get_name(self):
        return self.name


class Person(Robot):
    def __init__(self, name, model, manufacturer, battery_level, buyer):
        super().__init__(name, model, manufacturer, battery_level)
        self.buyer = buyer

    def get_buyer(self):
        return self.buyer


class AI(Robot):
    def __init__(self, name, model, manufacturer, battery_level, ai_type):
        super().__init__(name, model, manufacturer, battery_level)
        self.ai_type = ai_type

    def get_ai_type(self):
        return self.ai_type


# 04
class Car:
    door = 4

    def __init__(self, color, speed) -> None:
        self.color = color
        self.speed = speed

    def get_info(self):
        return f'Color: {self.color}\nSpeed: {self.speed}\nDoor: {Car.door}'


mercedes = Car('Asphalt grey', 196)
print(mercedes.get_info())


# 05
class Bird:
    def __init__(self, color, domestic, age):
        self.color = color
        self.domestic = domestic
        self.age = age

    def get_info(self):
        return f'Color: {self.color}\nDomestic: {self.domestic}\nAge: {self.age}'

# ?????
