'''
Tester une condition sur une ligne

    Le but de cet exercice est de tester si quelqu'un est majeur ou non à l'aide d'un opérateur ternaire.

    Votre condition doit donc tenir sur une seule ligne pour être valide !

    Pour valider l'exercice, votre script doit donc contenir uniquement deux lignes : la ligne de déclaration de la variable, et la ligne pour l'opérateur ternaire.

    Dans ce cas-ci, a est égal à 20, votre script devra donc retourner la chaîne de caractères 'Vous êtes majeur !' dans la variable majeur.

    Dans le cas contraire, la variable majeur devra contenir la chaîne de caractères "Vous êtes mineur".

        a = 20
'''

a = 20
majeur = "Vous êtes majeur !" if a == 20 else "Vous êtes mineur"

print(majeur)