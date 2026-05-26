'''
    Tronquer le nombre de décimales

    Dans cet exercice, nous voulons arrondir et tronquer le nombre de décimales après la virgule de la variable nombre, 
    par le nombre contenu dans la variable decimales.

    La variable resultat devra donc contenir le nombre décimal 2938.489.
    
    nombre = 2938.48872
    decimales = 3
'''

nombre = 2938.48872
decimales = 3

resultat = round(nombre, decimales)

print(resultat)