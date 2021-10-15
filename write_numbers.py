from os.path import isfile

print(isfile("numbers.txt"))
print(isfile("numbers_grrrr.txt"))

with open("numbers.txt", encoding="utf-8", mode="a") as f:
    for i in range(10):
        f.write(f"Szam: {i}\n")