'''
    Trouver l'erreur dans la fonction

    Dans cet exercice, le script ne retourne pas d'erreur mais n'affiche pas le résultat escompté.

    La fonction addition devrait nous permettre d'additionner deux nombres ensemble.

    Cependant, quand on print la variable resultat, Python nous retourne None, au lieu du résultat de l'addition (ici 15).

    Modifiez la fonction pour que le print de resultat affiche le résultat de l'addition.

    def addition(a, b):
        c = a + b

    resultat = addition(5, 10)
    print(resultat)
'''

def addition(a, b):
	return a + b # ou return c

resultat = addition(5, 10)
print(resultat)