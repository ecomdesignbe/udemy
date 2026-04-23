# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# FONCTIONS RÉCURSIVES
'''def a(n, limit):
    if n > limit:
        return
    print("n:", n)
    a(n*n, limit)

a(2, 100000)'''

def demander_choix_utilisateur(min, max):
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + " :")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("ERREUR: Vous devez rentrer un nombre entre", min, " et ", max)
            return demander_choix_utilisateur(min, max)
        return reponse_int
    except:
        print("ERREUR: Vous devez rentrer un nombre")
        return demander_choix_utilisateur(min, max)


choix = demander_choix_utilisateur(1, 4)
print("Choix de l'utilisateur:", choix)