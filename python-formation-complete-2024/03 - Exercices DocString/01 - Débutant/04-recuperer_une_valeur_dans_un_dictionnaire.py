'''
    Récupérer une valeur dans un dictionnaire

    Dans cet exercice, nous allons récupérer la valeur de la clé "prenom", contenue dans le dictionnaire employes.

    Votre script doit donc retourner la chaîne de caractères "Pierre" dans la variable resultat.

    employes = {
            "01": {
                "identite": {
                    "prenom": "Pierre",
                    "nom": "Dupont"
                    }
                }
            }

    resultat =
'''
employes = {
            "01": {
                "identite": {
                    "prenom": "Pierre",
                    "nom": "Dupont"
                    }
                }
            }

# resultat = employes.get('01').get('identite').get('prenom')
resultat = employes['01']['identite']['prenom']

print(resultat)