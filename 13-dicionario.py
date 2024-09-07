# dicionário é uma coleção de dados que contém chave e valor. 
filmInception = [{
    "title": "Inception",
    "year": 2010,
    "director": "Christopher Nolan",
    "rating": 8.8
}, {
    "title": "The Dark Knight",
    "year": 2008,
    "director": "Christopher Nolan",
    "rating": 9.0
}]
print(type(filmInception[0])) # <class 'dict'>
print(type(filmInception)) # <class 'list'>
print(filmInception[0]["title"]) # Inception
print(filmInception[1].get("year")) # 2008
print(filmInception[0].keys()) # dict_keys(['title', 'year', 'director', 'rating'])
print(filmInception[1].values()) # dict_values(['The Dark Knight', 2008, 'Christopher Nolan', 9.0])
print(filmInception[0].items()) # dict_items([('title', 'Inception'), ('year', 2010), ('director', 'Christopher Nolan'), ('rating', 8.8)])

filmInception[0]["new"] = "new"

filmInception[0].update({"rating": 9.0})

filmInception[0].pop("new")