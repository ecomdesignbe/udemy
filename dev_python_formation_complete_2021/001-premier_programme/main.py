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
''' 
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")        
    return reponse_nom

reponse_nom = demander_nom()

print("Vous vous appelez " + reponse_nom)
''' 

# Exemples -> Variable Globales et paramètres <-
'''
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
print("Vous vous appelez " + nom1 + ", vous avez " + str(age1) + " ans")
print("L'an prochain vous aurez " + str(age1+1) + " ans")

print("Vous vous appelez " + nom2 + ", vous avez " + str(age2) + " ans")
print("L'an prochain vous aurez " + str(age2+1) + " ans")
'''

# Exercice 4 : Créer une fonction afficher_informations_personne | paramètres: nom, age 
'''
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")
    return nom, age


# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
'''


# Exemples -> Conditions et variables <-
'''
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    if age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    return nom, age


# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
'''

# Exercice 5 : Condtions age > 60 : Vous êtes senior | age < 10 : Vous êtes enfant
'''
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    if age >= 60:
        print("Vous êtes Senior")
    elif age == 17:
        print("Vous êtes presque majeur")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 11:
        print("Vous êtes mineur")
    elif age <= 10 :
        print("Vous êtes un enfant")
    return nom, age


# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)
'''

# Exemples -> And / Or <-
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


def afficher_informations_personne(nom, age):
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age+1) + " ans")

    if age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes un senior")
    elif age < 10:
        print("Vous êtes un enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    return nom, age


# Demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# Demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Afficher les résultats
afficher_informations_personne(nom1, age1)
afficher_informations_personne(nom2, age2)


# Exemples -> Boucles For <-
'''
# CONSTANTES
NB_PERSONNES = 3
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demande_age(nom)
    afficher_informations_personne(nom, age)
'''

# Exemples -> Chaines formatées <-
'''
print(f"Vous vous appeler {nom}, vous avez {age} ans")
print("L'an prochain vous aurez %s" % (age+1))
print("Vous vous appeler %s, vous avez %s ans" %(nom, age))
print("toto", 20, "ans", "taille:", 1.70)
'''


