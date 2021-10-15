products = {"orange": 30, "apple": 50, "bread": 10}
print(products["orange"])
print(products["apple"])

products["orange"] = 29
print(products)

products["milk"] = 16
print(products)

my_products = {}
print(my_products)
my_products["bread"] = 88
print(my_products)

del(products["orange"])
print(products)

# products = {}
# products.clear()
# print(products)

for key in products.keys():
    print(key + ": " + str(products[key]))

for value in products.values():
    print(value)

products = {"orange": 30, "apple": 50, "bread": 10}

if "orange" in products:
    print("Narancs benne van")

if "phone" in products:
    print("Telefon benne van")

for item in products.items():
    print(item[0] + " " + str(item[1]))

print(products.items())

for key, value in products.items():
    print(key + " " + str(value))

i, j = [1, 2]
print(i)
print(j)

for key in products:
    print(key + ": " + str(products[key]))
