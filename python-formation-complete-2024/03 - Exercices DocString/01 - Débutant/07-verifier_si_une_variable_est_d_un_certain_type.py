'''
    Vérifier si une variable est d'un certain type

    Dans cet exercice, vous allez devoir vérifier que la variable prenom est bien une chaîne de caractères.

    La variable prenom est définie au début du script par une chaîne de caractère.

    Votre script doit vérifier que la variable prenom est bien de type 'chaîne de caractères'.

    Si c'est le cas, vous devez assigner la chaîne de caractères "Première vérification réussie." à la variable resultat.

    La variable prenom est ensuite redéfinie et assignée au nombre 0.

    Vous devez donc tester de nouveau votre condition pour vérifier si la variable prenom contient toujours une chaîne de caractères.

    Si c'est le cas, assignez la chaîne de caractères "Deuxième vérification réussie." à la variable resultat.

    prenom = "Pierre"

    # INSÉREZ LA PREMIÈRE CONDITION
    # Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère.
    # Ici c'est le cas, votre condition doit donc être vraie et la variable resultat doit donc être définie.

    prenom = 0

    # INSÉREZ L'AUTRE CONDITION
    # Cette fois-ci, la variable n'est pas égale à une chaîne de caractère.
    # Votre condition doit donc être fausse et la variable resultat ne doit donc pas être redéfinie.
'''

prenom = "Pierre"

# INSÉREZ LA PREMIÈRE CONDITION
# Votre condition doit vérifier si la variable prenom est bien une chaîne de caractère.
# Ici c'est le cas, votre condition doit donc être vraie et la variable resultat doit donc être définie.

if type(prenom) is str:
    resultat = "Première vérification réussie."
    print(resultat)

prenom = 0

# INSÉREZ L'AUTRE CONDITION
# Cette fois-ci, la variable n'est pas égale à une chaîne de caractère.
# Votre condition doit donc être fausse et la variable resultat ne doit donc pas être redéfinie.

if type(prenom) is str:
    resultat = "Deuxième vérification réussie."
    print(resultat)