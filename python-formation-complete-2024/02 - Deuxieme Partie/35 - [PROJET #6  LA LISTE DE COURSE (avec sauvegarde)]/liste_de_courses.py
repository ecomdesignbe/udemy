'''
La liste de courses

    On revient avec notre projet sur la liste de courses.

    Cette fois-ci, on va avoir un programme un peu plus intéressants puisqu'ici on s'intresse la sauvegarde de la liste sur le disque dur.

    Il va donc falloir utiliser ce que vous venez d'apprendre sur les fichiers (et notamment le format JSON) pour lire et écrire la liste.

    On commence ainsi à pouvoir retenir les données au-delà de l'exécution de notre script, 
    ce que nous reverrons par la suite plus en détail avec les bases de donnes SQL.

'''
import json
from pathlib import Path
cwd = Path.cwd() 

chemin = f"{cwd}\liste.json"

liste = []

while True:
    print("\n1. Ajouter")
    print("2. Afficher")
    print("3. Quitter")
    
    choix = input("Votre choix : ")
    
    if choix == "1":
        element = input("Élément à ajouter : ")
        liste.append(element)

        with open(chemin, "w") as f:
            json.dump(list(liste), f)        
        
    elif choix == "2":
        with open(chemin, "r") as f:
            liste = json.load(f)
            print(liste)
        
    elif choix == "3":
        break
        
    else:
        print("Choix invalide")


