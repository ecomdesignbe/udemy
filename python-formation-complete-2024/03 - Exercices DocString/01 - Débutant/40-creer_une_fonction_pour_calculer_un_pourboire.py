'''
    Créer une fonction pour calculer un pourboire

    Dans cet exercice, nous allons créer une fonction qui calcule le montant total d'une addition en fonction d'un pourboire et d'une réduction :

    Écrire une fonction Python calculer_montant_final(prix_base, pourcentage_pourboire, reduction) qui calcule un montant final à partir 
    d'un prix de base, d'un pourboire (en %) et d'une réduction (en %).

    La fonction doit d'abord ajouter le pourboire au prix, puis appliquer la réduction sur le nouveau montant.

    Le résultat doit être arrondi à un chiffre après la virgule.

    À noter
    Pour arrondir un nombre, vous pouvez utiliser la fonction round et lui passer en argument le nombre de décimales à garder.
    Exemple attendu
    calculer_montant_final(100, 15, 10) doit retourner 103.5.

'''
def calculer_montant_final(prix_base, pourcentage_pourboire, reduction):
    calcul_hors_reduc = prix_base + (pourcentage_pourboire * prix_base / 100)
    calcul_avec_reduc = reduction * calcul_hors_reduc / 100
    return calcul_hors_reduc - calcul_avec_reduc


print(calculer_montant_final(100, 15, 10))



