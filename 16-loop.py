# Utilize um exemplo pra cada estrutura de loop do python.

# For loop
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# List comprehension
numbers = [1, 2, 3, 4, 5]
squaredNumbers = [number**2 for number in numbers]
print(squaredNumbers)

# Dictionary comprehension
squaredNumbersDict = {number: number**2 for number in numbers}