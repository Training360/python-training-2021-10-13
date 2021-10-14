def print_info():
    name = "John Doe"
    print("Függvényen belül: " + name)
    return name

def append_chars(name):
    print("trallala")
    return "xxx" + name + "xxx"

employee = print_info()
print("Függvényen kívül: " + employee)

employee = append_chars("John")
print(employee)

append_chars("Jack")