# Collections : (Tableaux : Array), Listes, Tuples...
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> modifiable : rajouter/supprimer des éléments ou les modifier
# Plusieurs éléments

# ------------- TUPLES -----------------
# personnes = ("Mélanie", "Jean", "Martin", "Alice")
# print(len(personnes))
# print(personnes[-1]) # -1 pour le dernier element

# for i in range(0, len(personnes)):
#     print(personnes[i])

# for i in personnes:
#    print(i)
#    print(len(i))
#    print(i[-1])

# (0, 1, 2, 3, 4)
# valeurs = range(0, 5)
# print(valeurs[-1])

# ------------- LISTES -------------
"""personnes = ["Mélanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"

# print(personnes)

personnes.append(nouvelle_personne)
del personnes[1]

# print(personnes)


def afficher_personnes(c):
    for i in c:
        print(i)


def modifier_valeur(a):
    a[0] = 10


test = [1, 2, 3, 4]
print(test)
modifier_valeur(test)
print(test)

# afficher_personnes(personnes)"""


# ------------- FONCTIONS ET TUPLES -------------
"""def obtenir_informations():
    return "Mélanie", 37, 1.60

def afficher_informations(nom, age, taille):
    print(f"Informations: Nom: {nom}, age: {age}, taille:{taille}")


infos = obtenir_informations()
afficher_informations(*infos)

print(infos)
print(*infos)  # unpack tuple
print(infos[0], infos[1], infos[2])
# print("nom: " + infos[0])
# print("age: " + str(infos[1]))
# print("taille: " + str(infos[2]))

# nom, age, taille = obtenir_informations()
# afficher_informations(nom, age, taille)"""

# ------------- SLICES -------------
personnes = ("Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul")

# [start:stop:step]

#for i in personnes[::-2]:
#    print(i)

nom = "Jean"
print(nom[::-1])
