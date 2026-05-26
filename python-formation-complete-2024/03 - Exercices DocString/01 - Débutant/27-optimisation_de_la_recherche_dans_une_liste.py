'''
    Optimisation de la recherche dans une liste

    Vous avez une liste d'éléments et devez fréquemment vérifier si un élément spécifique est présent dans cette liste.

    Écrivez une fonction est_present qui prend une liste d'éléments et un élément à rechercher.

    La version initiale de la fonction effectue cette vérification de manière inefficace (en O(n)).

    Vous devrez modifier cette fonction pour la rendre plus efficiente (en O(1)).

    Exemple
    >>> liste = [1, 2, 3, 4, 5]
    >>> est_present(liste, 3)
    True
    >>>liste = [1, 2, 3, 4, 5]
    >>> est_present(liste, 6)
    False

    def est_present(liste, element):
        pass
'''
def est_present(liste, element):
    if element in liste:
        return True
    else:
        return False

liste = [1, 2, 3, 4, 5]
est_present(liste, 3)

liste = [1, 2, 3, 4, 5]
est_present(liste, 6)

'''
def est_present(liste, element):
    return element in set(liste)
'''

