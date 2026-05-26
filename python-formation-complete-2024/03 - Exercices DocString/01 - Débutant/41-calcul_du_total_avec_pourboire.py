'''
    Calcul du total avec pourboire

    Objectif
    Vous allez écrire une fonction Python qui calcule le montant total d'une addition en tenant compte d'un pourboire exprimé en pourcentage.

    Spécifications

    Nom de la fonction: calculer_total_addition

    Paramètres:

    montant (int ou float): le montant de l'addition, en euros. Doit être >= 0.

    pourcentage_pourboire (int ou float): le pourboire en pourcentage (ex: 10 pour 10%). Doit être >= 0.

    Valeur de retour: float — le total à payer (montant + pourboire), arrondi à 2 décimales.

    Gestion d'erreurs:

    Si montant < 0 ou pourcentage_pourboire < 0: lever ValueError.

    Si les types ne sont pas numériques: lever TypeError.

    Exemples attendus

    calculer_total_addition(50, 10) -> 55.0

    calculer_total_addition(48.9, 12.5) -> 55.01

    calculer_total_addition(0, 15) -> 0.0

    Conseils

    Convertissez le pourcentage en fraction (ex: 10% -> 0.10) avant de calculer le pourboire.

    Utilisez round(valeur, 2) pour arrondir le total à deux décimales.

    Tâches
    1) Valider les entrées (types et valeurs non négatives).
    2) Calculer le pourboire puis le total.
    3) Arrondir le total à deux décimales et le retourner.
    4) Tester votre fonction avec les exemples fournis.

    def calculer_total_addition(montant, pourcentage_pourboire):

    Retourne le montant total à payer (montant + pourboire).
    - montant: nombre >= 0
    - pourcentage_pourboire: pourcentage du pourboire (ex: 10 pour 10%)
    À faire:
    1) Valider les entrées (lever ValueError si négatives)
    2) Calculer le pourboire et le total
    3) Arrondir le résultat à 2 décimales

    # TODO: implémenter la fonction
    pass


    if __name__ == '__main__':
        # Quelques exemples à tester quand votre fonction sera prête:
        # print(calculer_total_addition(50, 10))         # attendu: 55.0
        # print(calculer_total_addition(48.9, 12.5))     # attendu: 55.01
        # print(calculer_total_addition(0, 15))          # attendu: 0.0
        # calculer_total_addition(-5, 10)                # devrait lever ValueError
        pass
'''

def calculer_total_addition(montant, pourcentage_pourboire):
    '''
    Retourne le montant total à payer (montant + pourboire).
    - montant: nombre >= 0
    - pourcentage_pourboire: pourcentage du pourboire (ex: 10 pour 10%)
    À faire:
    1) Valider les entrées (lever ValueError si négatives)
    2) Calculer le pourboire et le total
    3) Arrondir le résultat à 2 décimales
    '''
    # TODO: implémenter la fonction

    # Validation
    if montant < 0 or pourcentage_pourboire < 0:
        raise ValueError("Les valeurs ne peuvent pas être négatives")

    # Calcul du pourboire
    pourboire = montant * (pourcentage_pourboire / 100)

    # Calcul du total
    total = montant + pourboire

    return round(total,2)

if __name__ == '__main__':
    # Quelques exemples à tester quand votre fonction sera prête:
    print(calculer_total_addition(50, 10))         # attendu: 55.0
    print(calculer_total_addition(48.9, 12.5))     # attendu: 55.01
    print(calculer_total_addition(0, 15))          # attendu: 0.0
    calculer_total_addition(-5, 10)                # devrait lever ValueError
    pass




