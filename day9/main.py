##nested dictionary.....

student = {
    "name": "Gabriel Odeh",
    "profile": {
        "bio": "my name is gabriel and i am a student of talent nation.",
        "age": 23,
        "monitization status": False
    },
    "skills": {
        "languages": ["Python", "Go"],
        "frameworks": ["FastAPI"]
    }
}

print(student["profile"]["bio"])

print()
print("==============Assignment============")

employee = {
    "name": "Gabriel odeh",
    "Department": "Computer Ai/Machine learning",

    "contact": {
        "phone": "08111883595",
        "email": "gabbyjessie44@mail.com"
    },
    "address": {
        "city": "otukpo",
        "state": "benue state",
        "country": "nigeria"
    }
}
print(employee["contact"]["email"])
print(employee["address"]["city"])

employee["contact"]["phone"] = "09169270082"
print(employee["contact"]["phone"])

print