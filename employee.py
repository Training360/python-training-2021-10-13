class Employee:
    """Ez egy alkalmazottat tárol"""

    def __init__(self, first_name, last_name, age):
        print("Konstruktor")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_name(self):
        return self.first_name + " " + self.last_name

    def inc_age(self):
        self.age += 1

john = Employee("John", "Doe", 30)
print(john.first_name)
print(john.last_name)
print(john.age)

print(john.get_name())

john.inc_age()
print(john.age)

jack = Employee("Jack", "Doe", 50)
print(jack.get_name())
print(jack.age)
jack.inc_age()
print(jack.age)

