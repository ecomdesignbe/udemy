# LONGUEUR DES ZIP

noms = ("Jean", "Emilie", "Paul")
ages = (20, 30, 25)

try:
    noms_et_ages = zip(noms, ages, strict=True)
    print(list(noms_et_ages))
except ValueError:
    print("ERREUR : nombre d'éléments différents dans le zip")

