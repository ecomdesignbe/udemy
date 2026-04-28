"""
Ordonner une chaine de caractère

    Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents dans la chaîne de caractères.

    Vous devez créer une variable chaine_en_ordre qui, à la fin de l'exercice, doit contenir la chaîne de caractères suivante :

    "Anne, Julien, Lucien, Marie, Pierre"

    Attention

    Veillez à bien respecter les virgules et les espaces pour valider l'exercice !

        chaine = "Pierre, Julien, Anne, Marie, Lucien"

"""

chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_en_ordre = chaine.split(", ")
chaine_en_ordre.sort()
chaine_en_ordre = ", ".join(chaine_en_ordre)

print(chaine_en_ordre)

