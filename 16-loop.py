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

moveList = ['up', 'down', 'left', 'right']
moveList = [move.upper() for move in moveList]

movieList = ['star wars', 'star trek', 'lord of the rings', 'harry potter']
movieList = [movie for movie in movieList if 'o' in movie]

while True:
    search = input('Search for a movie: ')
    if search == 'exit':
        break
    if search in movieList:
        print('Movie found')
    else:
        print('Movie not found')
