i = int(input("Irj be egy szamot"))

if i >= 0:
    print("Pozitiv")
    if i > 100:
        print("Nagyobb mint szaz")
    else:
        print("Kisebb, mint szaz")
else:
    print("Negativ")