# import locale
#
# print(locale.getpreferredencoding(False))

path = "C:\\Windows\\"

with open("sample.txt", encoding="utf-8") as f:
    s = f.read()
    print(s)

with open("sample.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

with open("sample.txt", encoding="utf-8") as f:
    content = f.readlines()
    print(content)

with open("sample.txt", encoding="utf-8") as f:
    i = 0
    for line in f:
        if i == 1:
            break
        print(line.strip())
        i += 1

with open("sample.txt", encoding="utf-8") as f:
    i = 0
    for line in f:
        print(line)
        break
