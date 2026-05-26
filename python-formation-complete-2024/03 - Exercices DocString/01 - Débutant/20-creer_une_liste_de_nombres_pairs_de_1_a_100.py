'''
Créer une liste de nombres pairs de 1 à 100

Dans cet exercice, on continue avec la fonction range, cette fois-ci pour créer une liste de nombres pairs allant de 1 à 100.

Vous devez récupérer cette liste dans une variable resultat.

'''
resultat = []
for i in range(1,101):
    if i % 2 == 0:
        resultat.extend([i])

print(resultat)
