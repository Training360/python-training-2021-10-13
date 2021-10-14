# Összegzés tétele
# Egész számokat tartalmazó lista elemeit adjuk össze
numbers = [10, 24, 21, 25, 2, 234, 64, 234, 534]

sum = 0
for number in numbers:
    sum += number
print(sum)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1

# Szélsőérték keresés tétele
min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print(min)

# Van egy nevek listája, keresd ki belőle
# a leghosszabbat!
names = ["John", "John John John John", "Jack", "John Doe"]

max_name = names[0]
max_length = len(names[0])
for name in names:
    if len(name) > max_length:
        max_name = name
        max_length = len(name)
print(max_name)

max_name = names[0]
for name in names:
    if len(name) > len(max_name):
        max_name = name
print(max_name)