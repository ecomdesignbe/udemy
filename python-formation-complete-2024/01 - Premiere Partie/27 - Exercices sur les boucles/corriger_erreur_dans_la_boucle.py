'''
Corriger l'erreur dans la boucle

    Le but de cet exercice est de modifier le script afin d'afficher l'index de chaque lettre du mot 'Python'.

    Pour l'instant le script retourne une erreur. À vous de la corriger.

    Votre script doit donc afficher :

    0
    1
    2
    3
    4
    5

     mot = "Python"

    for i in range(mot):
        print(i)   
'''

mot = "Python"

for i in range(len(mot)):
    print(i)