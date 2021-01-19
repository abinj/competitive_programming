empty_dict = dict()

phone_book = dict(Batman=46567, Cersei=34567, Ghostbusters=65432)
print(phone_book)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

print(phone_book.get("Batman"))
print(phone_book["Batman"])

phone_book = dict([('Bat_man', 3456),
                   ("Cersei", 3245),
                   ("Ghostburster", 8765)])
print(phone_book)

phone_book["Godzilla"] = 2897

print(phone_book)

del phone_book["Godzilla"]
print(phone_book)

cersei = phone_book.pop("Cersei")
last_added = phone_book.popitem()
print(phone_book)
print(cersei)
print(last_added)
print(phone_book)
print(len(phone_book))
print("Bat_man" in phone_book)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}

second_phone_book = {
    "Catwomen": 4567,
    "Jaime": 4536,
    "Godzilla": 3465
}

phone_book.update(second_phone_book)
print(phone_book)


# dictionary complrehension
houses = {1: "ABC", 2: "BCD",3: "CDE"}
new_houses = {n**2: house + '!' for (n, house) in houses.items()}
print(houses)
print(new_houses)