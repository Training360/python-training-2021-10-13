from random import randrange

def eat_recursion(n):
    print("You are... " + str(n))
    eat_recursion(n + 1)


def numbers():
    return [1, 6]


print(randrange(0,10))

my_numbers = numbers()
print(my_numbers[1])

eat_recursion(1)
