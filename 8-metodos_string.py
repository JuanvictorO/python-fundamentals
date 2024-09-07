movieName = "Avengers: Endgame"

movieDescription = '''
  Avengers: Endgame is a 2019 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. 
  It is the direct sequel to Avengers: Infinity War (2018) and the 22nd film in the Marvel Cinematic Universe (MCU). 
  The film was directed by Anthony and Joe Russo, written by Christopher Markus and Stephen McFeely, and features an ensemble cast including Robert Downey Jr., 
  Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, Brie Larson, Karen Gillan, Danai Gurira, Benedict Wong, Jon Favreau, Bradley Cooper, Gwyneth Paltrow, and Josh Brolin.
'''

print(movieName.upper()) # AVENGERS: ENDGAME
print(movieName.lower()) # avengers: endgame
print(movieName.capitalize()) # Avengers: endgame
print(movieName.title()) # Avengers: Endgame
print(movieName.swapcase()) # aVENGERS: eNDGAME
print(movieName.count("e")) # 3
print(movieName.find("e")) # 4
print(movieName.rfind("e")) # 15
print(movieName.index("e")) # 4
print(movieName.rindex("e")) # 15
print(movieName.startswith("A")) # True
print(movieName.endswith("e")) # True
print(movieName.islower()) # False
print(movieName.center(50, "=")) # ==============Avengers: Endgame==============
print(movieName.replace("Endgame", "Infinity War")) # Avengers: Infinity War
print(movieName.split(":")) # ['Avengers', ' Endgame']
# Count every e in the movieDescription and return their position
count = 0
position = 0
while True:
    position = movieDescription.find("e", position)
    if position == -1:
        break
    count += 1
    position += 1
print(count)