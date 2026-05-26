'''
    Trouver la différence entre le plus grand et le plus petit nombre d'une liste

    Créez une fonction difference_max_min, qui prend une liste d'entiers positifs en argument et 
    retourne la différence entre le plus grand et le plus petit entier de la liste.

    Par exemple :

    difference_max_min([1, 3, 7, 2]) devra retourner 6 (7-1)
'''

def difference_max_min(lst_entier):    
    lst_min = min(lst_entier)
    lst_max = max(lst_entier)
    resultat = lst_max - lst_min
    return print(resultat)

difference_max_min([1, 3, 7, 2])
difference_max_min([10, 10, 10, 10])
difference_max_min([100, 50])
difference_max_min([2, 8, 3, 9, 11, 2])