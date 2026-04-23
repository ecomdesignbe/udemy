# afficher_informations_personne
# Paramètres : nom, age
def afficher_informations_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    # print(f"Vous vous appelez {nom}, vous avez {age} ans")
    # print("Vous vous appelez %s, vous avez %s ans" % (nom, age))

    print("L'an prochain vous aurez " + str(age + 1) + " ans")
    # print("L'an prochain vous aurez %s ans" % (age + 1))

    # == egal
    # < inférieur
    # <= inférieur ou égal
    # > supérieur
    # >= supérieur ou égal
    # True / False (Boolean)

    # age == 17 -> Vous êtres presque majeur
    # age == 18 -> Tout juste majeur : Félicitation
    # elif -> else if
    # age > 60 : Vous êtes sénior
    # age < 10 : Vous êtes enfant
    # Adolescent si age >= 12 et age < 18
    #          12 <= age < 18
    # Bebe si age == 1 ou age == 2
    if age == 17:
        print("Vous êtres presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes enfant")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher la taille
    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


# demander le nom
# nom1 = demander_nom()
# nom2 = demander_nom()
# nom1 = "personne1"
# nom2 = "personne2"

# demander l'age
# age1 = demander_age(nom1)
# age2 = demander_age(nom2)


# Afficher les résultats
# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)

NB_PERSONNES = 1

# la boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i + 1)
    age = demander_age(nom)
    afficher_informations_personne(nom, age, 1.60)

print("""
Vous 
    mettez 
        ce que vous voulez
""")

print("toto", 20, "ans", "taille:", 1.70)
