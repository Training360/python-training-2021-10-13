names = ["John Doe", "Jack Doe", "Jane Doe"]
print(len(names))

print(names[1])
# Szeletelés
print(names[::-1])

don_t_do_at_home = ["Alma", 5, "Korte", 60]
print(don_t_do_at_home[0])
print(don_t_do_at_home[1])

fruits = ["orange"]
fruits.append("apple")
fruits.append("dsgfsdf")
fruits.append("sdfs")
fruits.append("sdfds")
print(fruits)

fruits.insert(0, "alma")
print(fruits)

l = ["aaa", "bbb"]
l += ["ccc"]
print(l)

empty = []
print(empty)
empty += ["aaaa"]
print(empty)

letters = []
letters += "JOHN"
print(letters)

numbers = ["x", "y", "z", "z", "z", "z", "a"]
numbers[1] = "a"
print(numbers)

del(numbers[0])
print(numbers)
numbers.remove("z")
print(numbers)

print("x" in numbers)
print("z" in numbers)

print("a" in "John Doe")
print("o" in "John Doe")

while "z" in numbers:
    numbers.remove("z")
    print(numbers)
