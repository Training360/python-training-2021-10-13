# 5.6. Írjon   egy   programot,   ami   meghatározza,   hogy   egy  karakterlánc   tartalmazza-e  az   « e »
# karaktert.

name = "aaaabbaaaa"
for a_char in name:
    if a_char == "e" or a_char == "E":
        print("Talaltam e-t!")
        break

counter = 0
for a_char in name:
    if a_char == "e" or a_char == "E":
        counter += 1
print(counter)

result = ""
counter = 0
for a_char in name:
    result += a_char
    if counter < len(name) - 1:
        result += ", "
    counter += 1
print(result)
result = result[:-1]

result = name[::-1]
print(result)

result = ""
for a_char in name:
    result = a_char + result
print(result)

is_true = True
print(is_true)

print(name == name[::-1])
print(name == result)

print(str(213 + 1+1341 * 231 + 21213) + "retrew")

name[:-1:]