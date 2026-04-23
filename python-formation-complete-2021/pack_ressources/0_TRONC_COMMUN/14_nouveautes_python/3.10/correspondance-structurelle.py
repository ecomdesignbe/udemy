# CORRESPONDANCE STRUCTURELLE
# (Structural pattern matching)

# switch case -> match case

"""
while True:
    phrase = input("Parlez moi : ")
    if phrase == "bonjour" or phrase == "hello" or phrase == "salut":
        print("Bonjour, comment allez-vous ?")
    elif phrase == "bien":
        print("Je vais bien aussi")
    elif phrase == "bye":
        print("Au revoir")
        break 
    else:
        print("Je n'ai pas compris")
"""
# wildcard _
"""
while True:
    phrase = input("Parlez moi : ")
    match phrase:
        case "bonjour" | "hello" | "salut":
            print("Bonjour, comment allez-vous ?")
        case "bien":
            print("Je vais bien aussi")
        case "bye":
            print("Au revoir")
            break 
        case _:
            print("Je n'ai pas compris")
"""

personne1 = {"nom": "Paul", "infos": (30, "Ingénieur informatique")}
personne2 = {"nom": "Marc", "age": 20}
personne3 = {"nom": "Jean", "age": 17, "metier": "étudiant"}
personne4 = {"nom": "Pierre"}
personne5 = {"nom": "Emilie", "age": 16}

personnes = (personne1, personne2, personne3, personne4, personne5)

for personne in personnes:
    match personne:
        case {"nom": nom, "age": age, "metier": metier}:
            print(f"{nom}, {age} ans, {metier}")
        case {"nom": nom, "infos": (age, metier)}:
            print(f"{nom}, {age} ans, {metier}")
        case {"nom": nom, "age": age} if age >= 18:
            print(f"{nom}, {age} ans")
        case {"nom": nom, "age": age}:
            print(f"{nom}, {age} ans (mineur)")
        case _:
            print("Format non supporté")

