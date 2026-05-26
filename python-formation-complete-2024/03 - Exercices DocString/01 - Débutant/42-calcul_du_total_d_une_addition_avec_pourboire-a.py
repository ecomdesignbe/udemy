'''
    Calcul du total d'une addition avec pourboire

    Objectif

    Écrire une fonction Python calculer_total(addition, pourboire_pourcent) qui retourne le montant total à payer 
    en ajoutant un pourboire exprimé en pourcentage au montant de l'addition.

    Détails

    addition: montant de l'addition hors pourboire (nombre réel, par exemple 53.5)

    pourboire_pourcent: pourcentage du pourboire (nombre réel, par exemple 10 pour 10%)

    La fonction doit retourner le total à payer, arrondi à 2 décimales.

    Règles

    Le pourboire est calculé comme addition * (pourboire_pourcent / 100).

    Le total est addition + pourboire.

    Arrondir le résultat final à 2 décimales avec round(..., 2).

    Optionnel (conseillé): gérer les valeurs négatives en levant une exception ou en affichant un message d'erreur.

    Exemples

    calculer_total(100, 10) doit retourner 110.0

    calculer_total(53.5, 15) doit retourner 61.53 (car 53.5 * 0.15 = 8.025, total 61.525 arrondi à 61.53)

    À faire

    Implémenter la fonction calculer_total.

    Tester votre fonction avec quelques valeurs (y compris 0% de pourboire).

    def calculer_total(addition, pourboire_pourcent):
    """
    Calcule le montant total à payer en ajoutant un pourboire.
    Paramètres:
        addition (float): montant de l'addition hors pourboire
        pourboire_pourcent (float): pourcentage de pourboire (ex: 10 pour 10%)
    Retour:
        float: total à payer, arrondi à 2 décimales
    """
    # TODO: calculer le montant du pourboire à partir du pourcentage
    # TODO: additionner le pourboire au montant de l'addition
    # TODO: retourner le résultat arrondi à 2 décimales
    pass


    # Exemples d'utilisation (vous pouvez les modifier pour tester)
    print(calculer_total(100, 10))   # attendu: 110.0
    print(calculer_total(53.5, 15))  # attendu: 61.53
    print(calculer_total(80, 0))     # attendu: 80.0
'''
def calculer_total(addition, pourboire_pourcent):
    """
    Calcule le montant total à payer en ajoutant un pourboire.
    Paramètres:
        addition (float): montant de l'addition hors pourboire
        pourboire_pourcent (float): pourcentage de pourboire (ex: 10 pour 10%)
    Retour:
        float: total à payer, arrondi à 2 décimales
    """
    if addition <= 0 or pourboire_pourcent < 0:
        raise ValueError('Nombre négatif ou égal à 0')
    # TODO: calculer le montant du pourboire à partir du pourcentage
    pourboire_pourcent = addition * pourboire_pourcent / 100
    # TODO: additionner le pourboire au montant de l'addition
    addition = addition + pourboire_pourcent
    # TODO: retourner le résultat arrondi à 2 décimales
    return round(addition,2)


# Exemples d'utilisation (vous pouvez les modifier pour tester)
print(calculer_total(100, 10))   # attendu: 110.0
print(calculer_total(53.5, 15))  # attendu: 61.53
print(calculer_total(80, 0))     # attendu: 80.0