s = "indul a kutya es a tyuk aludni"

print(s.split(" "))

s = "qwer,uzuz,zi,ser,pkm"
for word in s.split(","):
    print(word)

names = ["jack", "john", "jane"]
print(",".join(names))

s = "indul a kutya es a tyuk aludni"
print(s.find("t"))

print(s.count("t"))

print("alma".upper())
print("ALMA".lower())
print("alma korte".capitalize())

print("     ewrewrw we rwer wer wer     ".strip())

print("xxxx ewrtwe xxx qew qwer xxx".strip("x").strip())

print("John".upper().strip())