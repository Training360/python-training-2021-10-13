from datetime import datetime

from requests import get

response = get("https://www.index.hu")
body = response.text
lines = body.splitlines()
count = 0
for line in lines:
    if "koronavírus" in line.lower():
        count += 1

now = datetime.now()
with open("korona.txt", mode="a") as f:
    f.write(f"{now} - {count}\n")