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

# Számlálás tétele
# Adott egész számok listája,
# írd ki, hány páros szám van benne!
numbers = [10, 24, 21, 25, 2, 234, 64, 234, 534]
number_of_even = 0
for number in numbers:
    if number % 2 == 0:
        number_of_even += 1

print(number_of_even)

# Eldöntés tétele
# Szerepel-e Jack?
names = ["John", "Jack", "Jane"]
for name in names:
    if name == "Jack":
        print("Van Jack!")
        break

# Szűrés
# Számok listájából válogasd ki egy másik
# listába a páros számokat
numbers = [10, 24, 21, 25, 2, 234, 64, 234, 534]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# Transzformáció (map)
# Hozz létre egy új listát,
# ami a nevek hosszát tartalmazza!
names = ["John", "John John John John", "Jack", "John Doe"]
length_of_names = []
for name in names:
    length_of_names.append(len(name))
print(length_of_names)
