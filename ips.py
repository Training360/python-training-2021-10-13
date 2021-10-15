# Írd ki az ip-címeket!
# Írd ki az ip-címek első tagját! 132.78.113.41
# Ebből a legkissebbet!

from json import load

file = open("MOCK_DATA.json", encoding="utf-8")
content = load(file)
min = 255
for item in content:
    ip = item["ip_address"]
    prefix = int(ip.split(".")[0])
    if prefix < min:
        min = prefix
print(min)
