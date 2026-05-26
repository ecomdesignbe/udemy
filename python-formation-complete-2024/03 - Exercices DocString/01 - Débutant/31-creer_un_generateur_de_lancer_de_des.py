'''
    Créer un générateur de lancer de dés

    Le but de cet exercice est de générer 6 lancer de dés aléatoires, allant de 1 à 6.

    Votre script doit récupérer ces lancers de dés dans la variable lancers.

    Votre script devra donc par exemple retourner les lancer suivants :

    1
    4
    5
    2
    2
    6
'''

import random

lancers = []

i = 0

while i < 6:
    lancers.append(random.randint(1,6))
    i += 1

print(lancers)

