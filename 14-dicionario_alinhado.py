import pprint

filmInception = {
  "inception": {
    "year": 2010,
    "director": "Christopher Nolan",
    "rating": 8.8
  }, 
  "theDarkKnight": {
    "title": "The Dark Knight",
    "year": 2008,
    "director": "Christopher Nolan",
    "rating": 9.0
  }
}

pprint.pprint(filmInception)

print(filmInception["inception"]["year"]) # 2010

filmInception["theDarkKnight"]["rating"] == 9.0

print(filmInception["theDarkKnight"]["rating"]) # 9.0

del filmInception["inception"]
  