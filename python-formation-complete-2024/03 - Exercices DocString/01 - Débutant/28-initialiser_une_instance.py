'''
    Initialiser une instance

    Dans cet exercice, vous devez initialiser l'instance harry_potter et créer un attribut d'instance pour que l'instance ait un prix différent de celui par défaut.

    L'instance harry_potter devra donc avoir un prix de 19,99€.

    L'attribut de classe prix de la classe Livre lui ne doit pas changer et doit rester à 9,99€.

    Attention

    Vous devez créer une méthode pour initialiser l'instance. 
    Vous ne pouvez pas simplement modifier l'attribut prix de l'instance pour lui donner la valeur de 19.99. 
    Si vous faites ceci, l'exercice ne sera pas validé.

    class Livre:
        prix = 9.99

    harry_potter = Livre()
'''

class Livre:
    prix = 9.99
    def __init__(self, prix):
        self.prix = prix

harry_potter = Livre(19.99)

print(harry_potter.prix)