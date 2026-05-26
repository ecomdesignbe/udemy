'''
    Additionner les valeurs d'un dictionnaire

    Dans cet exercice, vous devez additionner toutes les valeurs du dictionnaire ensemble.

    Votre script doit donc retourner le nombre entier 8700 dans la variable resultat.

    employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
'''

employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}

resultat = sum(employes.values())

print(resultat)