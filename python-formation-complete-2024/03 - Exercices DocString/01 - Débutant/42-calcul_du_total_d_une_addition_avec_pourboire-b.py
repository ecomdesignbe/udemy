from decimal import Decimal, ROUND_HALF_UP

def calculer_total(addition, pourboire_pourcent):
    """
    Calcule le montant total à payer en ajoutant un pourboire.
    Paramètres:
        addition (float): montant de l'addition hors pourboire
        pourboire_pourcent (float): pourcentage de pourboire (ex: 10 pour 10%)
    Retour:
        float: total à payer, arrondi à 2 décimales
    """
    if not all(isinstance(x, (int, float)) for x in (addition, pourboire_pourcent)):
        raise TypeError("Valeur(s) non numérique (int ou float attendu)")

    if addition < 0 or pourboire_pourcent < 0:
        raise ValueError("Paramètre(s) négatif(s)")

    # Conversion en Decimal pour précision exacte
    addition = Decimal(str(addition))
    pourboire_pourcent = Decimal(str(pourboire_pourcent))

    total = addition + (addition * (pourboire_pourcent / Decimal('100')))
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return float(total)


# Exemples d'utilisation (vous pouvez les modifier pour tester)
print(calculer_total(100, 10))   # attendu: 110.0
print(calculer_total(53.5, 15))  # attendu: 61.53
print(calculer_total(80, 0))     # attendu: 80.0