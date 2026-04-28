'''
La liste de courses

    Dans ce projet, vous allez devoir crer un programme qui permette de gérer une liste de courses.

    Comme pour la calculatrice, ce projet reviendra plusieurs fois dans la formation avec chaque fois un niveau de difficult supplémentaire.

    Dans cette première version, on va réaliser une version simple de la liste de courses avec la création d'une liste en mémoire laquelle on ajoute et on enlève des éléments.

    La liste ne sera donc pour l'instant pas sauvegardée sur le disque (c'est l'objet de la 2e partie de ce projet que vous retrouverez plus tard), 
    mais cela vous permettra de mettre en pratique la gestion des listes et l'interaction avec l'utilisateur ainsi que l'utilisation des boucles.

    Tout un programme !

    Bonne chance avec ce projet
'''

liste = []

while True:
    print("\n1. Ajouter")
    print("2. Supprimer")
    print("3. Afficher")
    print("4. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        element = input("Élément à ajouter : ")
        liste.append(element)
        
    elif choix == "2":
        element = input("Élément à supprimer : ")
        if element in liste:
            liste.remove(element)
        else:
            print("Introuvable")
            
    elif choix == "3":
        print("Liste :", liste)
        
    elif choix == "4":
        break
        
    else:
        print("Choix invalide")


