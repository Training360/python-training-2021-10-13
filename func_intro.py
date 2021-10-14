def print_employee():  # függvény deklaráció
    print("John Doe")
    print("developer")
    print("30")


def print_employee_name(employee_name="Anonymous"):  # formális paraméter
    print("Alkalmazott neve: " + employee_name)


def print_employee_details(name, position, age):
    print(f"""
Alkalmazott neve: {name}
Pozíciója: {position}
Életkora: {age}
    """)

print_employee()  # függvény hívás
print_employee()
print("End")

print_employee_name("John Doe")  # hívás helyén: aktuális paraméter
print_employee_name("Jack Doe")

print_employee_name()
print_employee_details("John Doe", "tester", 30)
print_employee_details("Jack Doe", "DevOps", 25)
# print_employee_details("Jack Doe", "DevOps")
