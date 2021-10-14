name = "John Doe"
print(len(name))
print(name[3])

lorem = """Lorem Ipsum is simply dummy text of the printing
and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type 
and scrambled it to make a type specimen book. It 
has survived not only five centuries, but also the leap into electronic"""

print(lorem)

# print(name[666])

name = "John Doe"
i = 0
while i < len(name):
    print(name[i])
    i = i + 1

for c in name:
    if c == " ":
        break
    print(c)

name = "John Doe"
age = 35

# A John Doe alkalmazott 35 éves!

print("A", name, "alkalmazott", age, "éves!")
print("A " + name + " alkalmazott" + str(age) + " éves!")

print(f"A {name} alkalmazott {age * 5} éves!")

name = "Jack Doe"

print(name[1:6])
print(name[1:6:2])
print(name[::-1])
print(name[:6])
print(name[2::2])