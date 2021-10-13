# i = 1
# while i <= 20:
#     print(i * 7)
#     i = i + 1

i = 1
result = 7
seven = 7
while i <= 20:
    print(result)
    result = result + seven
    i = i + 1

eur = 1
exchange_rate = 1.65
max_eur = 16385
while eur < max_eur:
    print(eur, "euro = ", eur * exchange_rate, "dollar")
    eur *= 2

a, b = 1, 1
print("1 1")
print("1 1")
while a <= 12:
    if a % 2:
        b = b * 3
        print(b, a)
    else:
        print(b, a)
    a = a + 1