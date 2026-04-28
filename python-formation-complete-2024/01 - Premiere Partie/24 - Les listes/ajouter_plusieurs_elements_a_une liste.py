'''
Ajouter plusieurs éléments à une liste

    Le but de cet exercice est d'ajouter plusieurs éléments dans une liste en une seule fois !

    Mais attention, vous devez ajouter plusieurs éléments dans la liste originale, et non pas imbriquer une liste dans une autre.

    La liste de départ contient les éléments 1, 2 et 3.

    La liste finale doit contenir les éléments 1, 2, 3, 4, 5 et 6. Vous devez donc ajouter les éléments 4, 5 et 6 à la liste originale.

        ma_liste = [1, 2, 3]
'''

ma_liste = [1, 2, 3]

ma_liste.extend([4, 5, 6])

print(ma_liste)