x = {  # dictionaries
    0: "Abir",
    1: 2,
    "Abir": 2,
    10: {
        0: "Abir",
        1: 2,
        "Abir": 2,
    },
}
print(x[0])
print(x["Abir"])
x["touhid"] = "Hi My name is Touhid"
print(x)
x.pop("Abir")
print(x)
print(x[10][0])
print(x.values())
z = {  # dictionaries
    0: "asm",
    1: 2,
    "Abir": 2,
    10: {
        0: "Abir",
        1: 2,
        "Abir": 2,
    },
}
x.update(z)
print(x)