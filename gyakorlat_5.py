line = ""
i = 1
while i <= 20:
    result = i * 7

    if result % 3 == 0:
        line += (str(result) + " * ")
    else:
        line += str(result) + " "
    i = i + 1
print(line)

stars = 1
while stars < 7:
    # print("*" * stars)
    line = ""
    number = 0
    while number < stars:
        line += "*"
        number += 1
    print(line)
    stars = stars + 1