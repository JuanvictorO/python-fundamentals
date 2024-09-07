# Set (elementos únicos) em python é uma coleção não ordenada e não indexada. Não permite elementos duplicados.
filmList = {"Inception", "The Dark Knight", "Interstellar", "Tenet", "Dunkirk"}
print(type(filmList)) # <class 'set'>
# print(filmList[1]) # TypeError: 'set' object is not subscriptable
print(len(filmList)) # 5
exampleSet = {"Inception", True, 1, 2.5}
print(exampleSet) # {True, 1, 2.5, 'Inception'}

# Adicionar um elemento ao set
filmList.add("The Prestige")
print(filmList) # {'The Dark Knight', 'Inception', 'The Prestige', 'Interstellar', 'Tenet', 'Dunkirk'}

# Remover um elemento do set
filmList.remove("Dunkirk")
print(filmList) # {'The Dark Knight', 'Inception', 'The Prestige', 'Interstellar', 'Tenet'}

# Adicionar item de outro set
filmList.update(exampleSet)
print(filmList) # {1, 2.5, 'The Dark Knight', 'Inception', 'The Prestige', 'Interstellar', True, 'Tenet'}