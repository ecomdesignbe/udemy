'''
Trouver l'erreur dans la fonction

    Dans cet exercice, la fonction multiplicateur_mot retourne une erreur.

    Trouvez cette erreur et modifiez la fonction pour qu'elle ne retourne plus d'erreur.

    Il y a plusieurs façons de fixer cette erreur.

    Votre script doit afficher 5 fois le mot Bonjour à la suite (parce que dans la vie, il est important de faire des scripts bien élevés...) : 

    BonjourBonjourBonjourBonjourBonjour    

        def multiplicateur_mot(mult=5, mot):
            return mot * mult

        mot_multiplie = multiplicateur_mot(mot="Bonjour")
        print(mot_multiplie)  
'''

def multiplicateur_mot(mot, mult=5):
	return mot * mult

mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)