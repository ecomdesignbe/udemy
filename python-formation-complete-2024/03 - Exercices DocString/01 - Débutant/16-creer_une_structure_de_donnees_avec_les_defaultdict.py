'''
    Créer une structure de données avec les defaultdict

    L'objectif de cet exercice est de créer une structure de données qui fait correspondre les IDs d'utilisateurs (des entiers) aux noms d'utilisateurs,
    en utilisant un defaultdict.

    Mais si un ID d'utilisateur n'est pas présent dans la structure de données, sa recherche doit retourner la chaîne exacte "Anonyme", comme solution de repli.

    Par exemple :

    users = users()
    users[3] = "John"

    assert users[3] ==  "John"
    assert users[9762] ==  "Anonyme"
    Complétez le code de la fonction users() pour qu'elle renvoie un tel defaultdict personnalisé.

    def users():
        pass
'''

from collections import defaultdict

def users():
    return defaultdict(lambda : 'Anonyme')

u = users()
u[3] = "John"

print(u[3]) 
print(u[9762])
