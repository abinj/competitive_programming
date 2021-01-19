car = ("Ford", "Raptor", "2019", "Red")
print(car)

print(len(car))
print(car[1])
print(car[2:])

hero1 = ("Batman", "Bruce wayne")
hero2 = ("Wonder Women", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)


awesome_team2 = (hero1, hero2)
print(awesome_team2)

print("Diana Prince" in awesome_team)
print(("Wonder Women", "Diana Prince") in awesome_team2)
print(awesome_team.index("Batman"))

case = [1,2,3]
tuple_list = tuple(case)
print(tuple_list)