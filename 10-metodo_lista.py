filmList = ["Inception", "The Dark Knight", "Interstellar", "Tenet", "Dunkirk"]

print(len(filmList)) # 5
print(filmList[1]) # The Dark Knight
print(filmList.index("Tenet")) # 3
print(filmList.count("Inception")) # 1
filmList.append("The Prestige")
filmList.remove("Dunkirk")
filmList.insert(2, "Memento") # ['Inception', 'The Dark Knight', 'Memento', 'Interstellar', 'Tenet', 'The Prestige']
filmList.sort() # ordena a lista
print(filmList.pop()) # The Prestige

filmsCopy = filmList.copy()
print(filmsCopy)

filmsCopy.clear() # limpa a lista
