"""Premier programme
Formation Python
apprendre la programmation"""

nom = input("Quel est votre nom ? ")

# str -> chaine "" / int -> nombre
age = 0
while age == 0:
    try:
        age = int(input("Quel est votre age ? "))
    except ValueError:
        print("ERREUR: Vous devez rentrer un nombre pour l'age")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")


# str / int
# input -> str

