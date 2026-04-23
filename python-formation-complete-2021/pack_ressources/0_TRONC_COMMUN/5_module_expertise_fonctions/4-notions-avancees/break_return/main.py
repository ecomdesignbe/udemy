# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# DIFFÉRENCE ENTRE BREAK ET RETURN
#

def a():
    print("Début de la fonction")
    for i in range(0, 100):
        if i > 20:
            break
        print(i)
    print("Fin de la fonction")
    print("aaa")

a()