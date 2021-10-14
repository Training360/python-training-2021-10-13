for i in range(0, 9):
    print(i)

# Tuple
names = ("John Doe", "Jane Doe")
print(names[1])
for name in names:
    print(name)

# names.append("Jack Doe")
# names[0] = "Jack Doe"   # 'tuple' object does not support item assignment

def calculate_min_max(numbers):
    min = numbers[0]
    max = numbers[0]
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    return (min, max)

limits = calculate_min_max([10, 6, 78, 4, 16, 68])
print(limits)

(a, b) = calculate_min_max([10, 6, 78, 4, 16, 68])
print(a)
# print(b)

ch = "*"
if "a" <= ch <= "z":
    print("Kisbetu")

