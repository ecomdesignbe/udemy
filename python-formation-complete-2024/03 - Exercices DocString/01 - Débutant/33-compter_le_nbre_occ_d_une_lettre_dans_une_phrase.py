'''
    Compter le nombre d'occurrences d'une lettre dans une phrase

    Dans cet exercice, nous cherchons à compter le nombre d'occurrences d'une lettre dans une chaîne de caractère.

    Ici, nous cherchons le nombre de fois que la lettre "o" apparaît dans la phrase "Bonjour tout le monde".

    Votre script devra retourner dans ce cas-ci dans une variable resultat le nombre 4 !

    lettre_a_chercher = "o"

    phrase = "Bonjour tout le monde"
'''

lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
resultat = phrase.count(lettre_a_chercher)
print(resultat)   