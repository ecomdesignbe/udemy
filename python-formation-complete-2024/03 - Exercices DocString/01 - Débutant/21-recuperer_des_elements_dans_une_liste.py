'''
    Récupérer des éléments dans une liste
    
    Dans cet exercice, dans lequel vous devez récupérer plusieurs éléments de la liste.

    Pour réussir cet exercice, vous devez récupérer :

    Dans une variable premier le premier élément de la liste ("Pierre")

    Dans une variable dernier le dernier élément de la liste ("Marie")

    Dans une variable deux_premiers les deux premiers éléments de la liste ([Pierre, Paul])

    Dans une variable deux_derniers les deux derniers éléments de la liste ([Paul, Marie]).

    ma_liste = ["Pierre", "Paul", "Marie"]

'''

ma_liste = ["Pierre", "Paul", "Marie"]

premier = ma_liste[0]
dernier = ma_liste[-1]
deux_premiers = ma_liste[:2]
deux_derniers = ma_liste[1:]
print(deux_derniers)