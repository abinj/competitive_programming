random_set = {"Educative", 1408, 1.23, (True, False)}
print(random_set)
print(len(random_set))


empty_Set = set()
print(empty_Set)
empty_Set.add(1)
print(empty_Set)

empty_Set.update([2,3,4])
print(empty_Set)

empty_Set.update([(1,2)])
print(empty_Set)

empty_Set.remove(1)
print(empty_Set)

empty_Set.discard(2)
print(empty_Set)

set_A = {1,2,3,4}
set_B = {5,6,7,8}

#union
print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))

set_A = {1,2,3,4}
set_B = {5,2,7,8}
#intersection
print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))


#difference
print(set_A - set_B)
print(set_B - set_A)



star_wars_dict = {1: "Anakin", 2: "Darth Vader", 3: 1000}
print(star_wars_dict)
star_wars_set = set(star_wars_dict)  # Converting from dictionary
print(star_wars_set)


import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%H:%M:%S"))
print(datetime.datetime.now().strftime("%y:%m:%d"))
