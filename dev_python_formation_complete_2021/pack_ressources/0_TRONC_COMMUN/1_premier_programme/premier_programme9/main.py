"""Premier programme
Formation Python
apprendre la programmation"""

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_int = int(age)  
except ValueError:
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    print("Vous vous appelez " + nom + ", vous avez " + str(age_int) + " ans")
    print("L'an prochain vous aurez " + str(age_int + 1) + " ans")

