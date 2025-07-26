# Exemples -> print - input - str - try <-
''' 
nom = "Toto"
print("Je m'appelle " + nom + " ! ")
print("Mon nom est bien " + nom + " ! ")
'''

'''
nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_prochain = int(age) + 1
except ValueError:
    print("Erreur: Vous devez rentrer un nombre pour l'age")
else:
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age_prochain) + " ans")
'''

# Exercice 1 : Demander le nom de l'utilisateur / Afficher le nom de l'utilisateur + son age
''' 
nom_utilisateur = input("Quel est ton nom ? ")
age_utilisateur = input("Quel est ton âge ? ")
print("Vous vous appelez " + nom_utilisateur + ", vous avez " + age_utilisateur + " ans.")
''' 


# Exemples -> while <-
''' 
nom = input("Quel est votre nom ? ")

age = 0

while age == 0:
    try:
        age_str = int(input("Quel est votre age ? "))
    exept ValueError:
        print("ERREUR: Vous devez rentrer un nombre pour l'age")

print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")
'''

# Exercice 2 : Tester si le nom de l'utilsateur est vide ou non
''' 
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")
print(nom)
''' 


# Exemples -> fonctions <-
'''
def demander_age():
    age_int = 0
    while age_int == 0:
        age_chaine = input("Quel est votre age ? ")
        try:
            age_int = int(age_chaine)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int

# Demander le nom
nom = ""
while nom == "":
    nom = input("Quel est votre nom ? ")

# Demander l'age
age = demander_age()

# Afficher les résultats
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")
'''

# Exercice 3 : Créer une fonction demander_nom | var = reponse_nom | return reponse_nom

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")        
    return reponse_nom

reponse_nom = demander_nom()

print("Vous vous appelez " + reponse_nom)
