'''
    Corriger la déclaration de la liste

    Le but de cet exercice est de trouver et réparer l'erreur présente dans le code.

    Vous devez modifier le code dans la console afin de ne plus avoir d'erreurs lors de l'exécution du script.

    if isinstance(list, range):
        import builtins
        list = builtins.list
    # ^^^ Ne modifiez pas les lignes de code ci-dessus

    list = range(3)
    list2 = range(5)

    resultat = list(list2)
'''

if isinstance(list, range):
    import builtins
    list = builtins.list
# ^^^ Ne modifiez pas les lignes de code ci-dessus

liste = range(3)
list2 = range(5)

resultat = list(list2)
