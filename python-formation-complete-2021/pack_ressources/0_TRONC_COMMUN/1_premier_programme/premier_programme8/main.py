"""Premier programme
Formation Python
apprendre la programmation"""

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_prochain = int(age) + 1
except ValueError:
    print("ERREUR: Vous devez rentrer un nombre pour l'age")
else:
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")

