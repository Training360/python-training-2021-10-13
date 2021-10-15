john = {
    "name": "John Doe",
    "age": 30,
    "salary": 100_000,
    "address": {
        "city": "Budapest",
        "street": "Petofi",
        "number": 10
    },
    "skills": ["java", "python", "javascript"]
}

print(john["address"]["city"])
print(john["skills"][1])

jack = {
    "name": "Jack Doe",
    "age": 40,
    "salary": 200_000
}

print(john["name"])
print(john["salary"])

employees = [
    {"name": "John"},
    {"name": "Jack"}
]
print(employees[1]["name"])