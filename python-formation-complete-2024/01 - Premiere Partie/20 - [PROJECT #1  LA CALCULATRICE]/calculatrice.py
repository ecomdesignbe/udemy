'''
[PROJECT #1  LA CALCULATRICE]

    Vous voici arrivé au premier projet de cette formation.

    Rien de bien incroyable encore, on va se laisser un peu de temps avant de réaliser un site web qui analyse les donnes de la bourse en temps rel

    Ce projet de la calculatrice reviendra dans la suite du cours sous différentes formes, chaque fois avec une petite difficulté supplémentaire.

    Dans la premire version de ce projet, vous allez devoir créer une calculatrice en ligne de commande qui demande l'utilisateur de saisir deux nombres 
    et qui affiche ensuite le résultat de l'addition de ces deux nombres.

    Rien de bien compliqué si vous avez suivi attentivement toutes les sessions et réalisé avec soin les quiz et exercices de code jusqu'ici.

'''

nombre_a = int(input("Veuillez entrer un premier nombre : "))
nombre_b = int(input("Veuillez entrer un deuxième nombre : "))

resultat = nombre_a + nombre_b
print(f"Le résultat de l'addition du nombre {nombre_a} avec le nombre {nombre_b} est égal à {resultat}")