movieName = "Avengers: Endgame"
moveName2 = "avengers: endgame"
print(movieName == moveName2) # Case sensitive

movieDescription = '''
  Avengers: Endgame is a 2019 American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. 
  It is the direct sequel to Avengers: Infinity War (2018) and the 22nd film in the Marvel Cinematic Universe (MCU). 
  The film was directed by Anthony and Joe Russo, written by Christopher Markus and Stephen McFeely, and features an ensemble cast including Robert Downey Jr., 
  Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, Brie Larson, Karen Gillan, Danai Gurira, Benedict Wong, Jon Favreau, Bradley Cooper, Gwyneth Paltrow, and Josh Brolin. 
  In the film, the surviving members of the Avengers and their allies attempt to reverse the damage caused by Thanos in Infinity War.
'''
print(movieDescription)

# Multiplicação de strings
line = "="
print(line * 50)

# 2 - procure por uma palavra específica no texto
print("Avengers" in movieDescription)
print("avengers" in movieDescription) # Case sensitive
