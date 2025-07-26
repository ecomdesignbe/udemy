# --- PARTIE 1 ---


personne = {'nom': 'Mélanie', "age": 25, "taille": 1.60}


# print(personne)
# print(personne['nom'])
# print(personne['age'])

"""personne['nom'] = "Claire"
personne['poste'] = "Développeur"
achat = ("Chocolat", "beurre", "fromage")
personne['achats'] = achat
# print(personne)

for i in personne:
    print(f"clef: {i} - valeur: {personne[i]}")"""


# --- PARTIE 2 ---

# noms age, taille

personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)
]

def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

# Jacques
infos = obtenir_informations("Jacques", personnes)
# print(infos)

personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)
}

infos = personnes_dict.get("Martin")
if not infos:
    print("La clef n'existe pas")
else:
    print(infos)