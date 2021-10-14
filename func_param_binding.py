def print_employee(name, age=20):
    print("Name: " + name)
    print("Age: " + str(age))


print_employee("John Doe", 30)  # sorrendi kötés
print_employee(age=30, name="John Doe")  # név szerinti kötés
print_employee("Jack Doe")