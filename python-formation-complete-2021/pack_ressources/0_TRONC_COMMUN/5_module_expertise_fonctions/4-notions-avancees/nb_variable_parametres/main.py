# PYTHON FONCTIONS - NOTIONS AVANCÉES
#
# Nombre variable de paramètres

'''def a(age, taille, numero_telephone):
    print("toto", age, taille, numero_telephone)

a(20, 1.75, "0610101010")'''


def somme(titre, *nombres):
    print("TITRE:", titre)
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme("somme des notes", 15, 11, 18))

