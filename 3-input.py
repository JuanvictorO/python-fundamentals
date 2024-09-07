# Retorno do input sempre é string
name = input("Enter the movie name:\n")
yearLaunched = int(input("Enter the year of release:\n"))
noteMove = float(input("Enter the movie rating:\n"))
planIncluded = bool(input("Is it included in the plan?\n"))

print(type(name))
print(type(yearLaunched))
print(type(noteMove))
print(type(planIncluded))