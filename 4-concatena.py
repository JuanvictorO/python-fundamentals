name = input("Enter the movie name:\n")
yearLaunched = int(input("Enter the year of release:\n"))
noteMove = float(input("Enter the movie rating:\n"))
planIncluded = bool(input("Is it included in the plan?\n"))

print("The movie name is", name)
print("The year of release is", yearLaunched, "\nand the rating is", noteMove)
print(f"Is it included in the plan? {planIncluded}\n"
      f"Type of name: {type(name)}\n"
      f"Type of yearLaunched: {type(yearLaunched)}\n"
      f"Type of noteMove: {type(noteMove)}\n"
      f"Type of planIncluded: {type(planIncluded)}"
      )