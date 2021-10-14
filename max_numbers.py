# Kérj be a felhasználótól 5 számot, és válaszd ki a legnagyobbat!
# Írd is ki a beírt 5 számot, egymás mellé!
# 5
# 6
# 3
# Kapott számok: 5, 6, 3
# Ebből a legnagyobb: 6

numbers = []
i = 0
while i < 5:
    number = int(input(f"Add meg a {i + 1}. számot!\n"))
    numbers.append(number)
    i += 1
# print(numbers)

result = "Kapott számok: "
i = 0
for number in numbers:
    result = result + str(number)
    if i != len(numbers) - 1:
        result = result + ", "
    i += 1
print(result)

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"Ebből a legnagyobb: {max}")