# SUPPRIMER PRÉFIXE ET SUFFIXE D'UNE CHAINE

phrase = "emilie a mangé un gateau"

# print(phrase.strip("gateau"))

# removeprefix / removesuffix
print(phrase.removesuffix(" gateau"))
print(phrase.removeprefix("emilie "))
print("Paul " + phrase.removeprefix("emilie ").removesuffix(" gateau") + " flan")
