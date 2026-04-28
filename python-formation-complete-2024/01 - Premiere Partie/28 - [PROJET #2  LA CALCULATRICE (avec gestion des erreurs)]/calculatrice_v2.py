'''
La calculatrice - Gestion des erreurs

    Vous vous rappelez de la calculatrice ?

    On va améliorer le script que l'on avait fait dans la première partie de ce projet en y ajoutant la gestion des erreurs.

    En effet, en programmation, il ne faut jamais faire confiance l'utilisateur.

    C'est d'ailleurs bien souvent a que sert la moitié du code qu'on écrit : prévenir les risques d'erreurs, de sécurité et autres.

    Dans la deuxième version de ce projet, vous allez devoir créer une calculatrice en ligne de commande qui demande l'utilisateur de saisir deux nombres 
    et qui affiche ensuite le résultat de l'addition de ces deux nombres.

    On va donc également gérer le cas de figure dans lequel l'utilisateur ne rentre pas de donnes valides.

    Bonne chance pour ce second projet !
'''

while True:
    try:
        nombre_a = int(input("Veuillez entrer un premier nombre : "))
        break
    except ValueError:
        print("Veuillez rentrer un nombre valide")

while True:
    try:
        nombre_b = int(input("Veuillez entrer un second nombre : "))
        break
    except ValueError:
        print("Veuillez rentrer un nombre valide")

resultat = nombre_a + nombre_b
print(f"Le résultat de l'addition du nombre {nombre_a} avec le nombre {nombre_b} est égal à {resultat}")

