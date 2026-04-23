"""Premier programme
Formation Python
apprendre la programmation"""

def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int
            
# demander le nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")

# demander l'age
age = demander_age()

# Afficher les résultats
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")


