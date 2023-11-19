
# TASKS (DAY 2) - home:
# 01 (static property)
# Animal adli class yaradin:
class Animal:
    passport = True  # boolean field ler
    vaccine = True

    # init methodu vasitəsi ilə ona name, age, color, height, year fieldləri təyin edin:
    def __init__(self, name, age, color, height, year):
        self.name = name
        self.age = age
        self.color = color
        self.height = height
        self.year = year

    # get_color və get_height adli funksiyalar yazın (əlavə get_info adlı funksiya ilə
    # bütün məlumatları return edən funskiya da yazın):
    def get_color(self):
        return self.color

    def get_height(self):
        return self.height

    def get_info(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Color": self.color,
            "Height": self.height,
            "Year": self.year
        }

    # classmethod - lar yazin:
    @classmethod
    def opposite_passport(cls):
        cls.passport = not cls.passport

    @classmethod
    def opposite_vaccine(cls):
        cls.vaccine = not cls.vaccine

    @classmethod
    def reverse_passport_and_vaccine(cls):
        cls.passport = not cls.passport
        cls.vaccine = not cls.vaccine


# Object yaratmadan passport və vaccine fieldlərini print edin:
print("Passport:", Animal.passport)
print("Vaccine:", Animal.vaccine)

# 2 fərqli object yaradın:
dog = Animal("Blue", 3, "Golden", 0.7, 2023)
cat = Animal("Peanut", 2, "Gray", 0.4, 2023)

# Bu objectlər üçün get_color funskiyasın çağırıb print edin:
print(dog.get_color())
print(cat.get_color())

# Bu objectlər üçün passport və vaccine fieldlərin də çağırıb print edin:
print("Animal eShopper Passport:", dog.passport)
print("Animal eShopper Vaccine:", dog.vaccine)
print("Animal 2 Passport:", cat.passport)
print("Animal 2 Vaccine:", cat.vaccine)

# Daha sonra yuxarıda yaratdığımız objectləri bu classmethodları çağırdıqdan sonra da
# print edib nəticəsinə baxın:
Animal.opposite_passport()
Animal.opposite_vaccine()

print("Animal eShopper Passport:", dog.passport)
print("Animal eShopper Vaccine:", dog.vaccine)
print("Animal 2 Passport:", cat.passport)
print("Animal 2 Vaccine:", cat.vaccine)


Animal.reverse_passport_and_vaccine()

print("Animal eShopper Passport:", dog.passport)
print("Animal eShopper Vaccine:", dog.vaccine)
print("Animal 2 Passport:", cat.passport)
print("Animal 2 Vaccine:", cat.vaccine)


# TASKS (DAY 2):
# 01 (static property)


class Country:
    continent = "Asia"  # Static property

    # Constructor-da (init method) ad, dil, erazi, olke kodu parametrləri yaradın:
    def __init__(self, name, language, region, country_code):
        self.name = name
        self.language = language
        self.region = region
        self.country_code = country_code

    @classmethod
    def get_continent(cls):
        return cls.continent


# Object yaradaraq və yaratmadan hansı materik oldugun print edin:
print("Continent:", Country.continent)

# Object yaradaraq isə digər fieldləri print edin:
country = Country("Japan", "japanese", "Asia", 81)

print("Continent:", country.get_continent())
print("Name:", country.name)
print("Language:", country.language)
print("Region:", country.region)
print("Country Code:", country.country_code)

# 02 (class method)
# ?

# 03 (class method)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}"

    @classmethod
    def user_input(cls):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        return cls(name, surname)


person = Person.user_input()

print(person)

# 04 (static method)


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def is_underage(age):
        return age < 18


person1 = Person("Narmin", "Mailova", 20)

print(person1.get_full_name())
print(f"{person1.get_full_name()} is underage: {Person.is_underage(person1.age)}")

