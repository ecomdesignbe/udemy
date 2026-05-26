'''
    Récupérer seulement les éléments pairs d'une liste

    Dans cet exercice, nous avons une liste qui contient 50 nombres.

    Le but de cet exercice est de récupérer dans la liste nombres_pairs, uniquement les nombres pairs de la liste nombres.

    nombres = range(51)
    nombres_pairs = []
'''


nombres = range(51)
nombres_pairs = []

for nombre in nombres:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)

print(nombres_pairs)