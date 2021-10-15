from datetime import datetime

from requests import get

response = get("https://www.training360.com/")
# print(response.text)
lines = response.text.splitlines()
# print(lines)

# Letölti az Index főoldalát, és megszámolja, hogy hány
# sorban szerepel a koronavírus szó

# Ezt hozzáfűzi a korona.txt állományba.

# Írd ki mellé a dátumot/időt is (lásd lent)

print(datetime.now())

# dátum - szám
# 2021-10-15 13:22:35.954429 - 2
# 2021-10-15 13:22:35.954429 - 2
# 2021-10-15 13:22:35.954429 - 2

