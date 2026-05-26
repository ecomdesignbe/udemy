'''
    Récupérer l'indice de l'itération dans une boucle

    Le but de cet exercice est de récupérer à la fois l'indice et l'élément sur lequel nous bouclons dans chaque itération de la boucle for.

    Votre script doit donc afficher dans ce cas-ci :

    0 Pierre
    1 Paul
    2 Marie

    liste = ["Pierre", "Paul", "Marie"]
'''

liste = ["Pierre", "Paul", "Marie"]

for indx, valeurs in enumerate(liste):
    print(indx, valeurs)
