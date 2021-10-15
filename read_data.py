# [{"name": "John Doe", "ip": "187.21.23.32"},
# {"name": "John Doe", "ip": "187.21.23.32"},
# {"name": "John Doe", "ip": "187.21.23.32"}]

# data = []
# item = {}
# item["orange"] = 7
# data.append(item)

data = []
with open("MOCK_DATA.csv", encoding="utf-8") as f:
    i = 0
    for line in f:
        if i != 0:
            parts = line.split(",")
            name = parts[0] + " " + parts[1]
            ip = parts[3]
            item = {"name": name, "ip": ip}
            data.append(item)
        i += 1
print(data)
