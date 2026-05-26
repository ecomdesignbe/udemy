'''
    Créer un générateur de mot de passe

    Dans cet exercice, nous allons créer un générateur de mot de passe aléatoire.

    À l'aide du module string et du module random, vous allez devoir générer un mot de passe aléatoire de la longueur spécifiée dans la variable taille (ici, 8).

    Votre mot de passe doit pouvoir contenir des lettres minuscules, majuscules, n'importe quel *chiffre de 0 à 9 et n'importe quel caractère spécial (!"#$%&' etc...).

    import string
    import random

    taille = 8
'''

import string
import random

taille = 8

mot_de_passe = ''.join(random.choices(string.hexdigits + string.punctuation, k=taille))
print(mot_de_passe)
