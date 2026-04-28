'''
Le jeu du nombre mystère
    On continue avec un programme un peu plus marrant que les projets précédents.

    Dans ce projet, tu vas devoir recréer le jeu du nombre mystre.

    L'ordinateur va choisir un nombre entre 1 et 100 et ton objectif est de trouver ce nombre

    Bien entendu, tu as droit un nombre limité d'essais pour trouver le nombre.

    Tu vas donc devoir utiliser un module que l'on a vu dans les parties précédentes, les boucles, la fonction input.

    Bref, là encore, beaucoup de notions qui individuellement ne sont pas compliquées, 
    mais qu'il va falloir que tu saches agencer ensemble dans une logique particulière.
'''
import random

nbre_mystere = random.randint(1, 100)
tentative = 10

print("Bienvenue dans le jeu du nombre mystère !")
print(f"Vous avez {tentative} essais")

while tentative > 0:
    nbre = int(input("Entrez votre nombre : "))

    if nbre == nbre_mystere:
        print(f"Bravo, vous avez trouvé le nombre mystère {nbre_mystere} !")
        break
    else:
        tentative -= 1

        if nbre < nbre_mystere:
            print("Le nombre mystère est plus grand")
        else:
            print("Le nombre mystère est plus petit")

        if tentative > 0:
            print(f"Il vous reste {tentative} essais")
        else:
            print(f"Vous avez perdu ! Le nombre mystère était {nbre_mystere}")



    
    



