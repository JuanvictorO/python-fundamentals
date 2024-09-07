onePieceCrew = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jinbe"]
def printCrew():
    for member in onePieceCrew:
        print(member)
printCrew()

onePieceCrew2 = {
    "Luffy": {
        "role": "Captain",
        "full_name": "Monkey D. Luffy",
    },
    "Zoro": {
        "role": "Swordsman",
        "full_name": "Roronoa Zoro",
    },
    "Nami": {
        "role": "Navigator",
        "full_name": "Nami",
    },
    "Usopp": {
        "role": "Sniper",
        "full_name": "Usopp",
    },
    "Sanji": {
        "role": "Cook",
        "full_name": "Vinsmoke Sanji",
    }
}
print(onePieceCrew2)

import random
def quiz():
    member = random.choice(list(onePieceCrew.keys()))
    print(f"Qual o nome completo de {member}?")
    answer = input("Resposta: ")
    if answer == onePieceCrew[member]["full_name"]:
        print("Resposta correta!")
    else:
        print("Resposta errada!")

quiz()
