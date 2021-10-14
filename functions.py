def print_hello():
    """Írj egy függvényt, ami kiírja, hogy "Hello Functions!"""
    print("Hello Functions!")


def sum_numbers(a, b):
    """Írj egy függvényt, ami két paramétert kap, és összeadja ezeket!"""
    return a + b


def count_spaces(s):
    """Írj egy függvényt, ami visszaadja, hogy a paraméterként átadott
    szöveg, hány space karaktert tartalmaz!"""
    count = 0
    for c in s:
        if c == " ":
            count += 1


def calculate_average(numbers):
    """Írj egy függvényt, ami paraméterként átadott lista átlagát
adja vissza"""
    if len(numbers) == 0:
        return 0
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)


def count_vowels(s):
    """Írj egy függvényt, ami visszadja, hogy hány magánhangzó
        van, a paraméterként átadott szövegben!"""
    count = 0
    for c in s:
        if c in "aAeEiIoOuU":
            count += 1
    return count


# print_hello()
# # print(sum_numbers(10, 20))
# result = sum_numbers(10, 20)
# print(result)
# input("grrr")
