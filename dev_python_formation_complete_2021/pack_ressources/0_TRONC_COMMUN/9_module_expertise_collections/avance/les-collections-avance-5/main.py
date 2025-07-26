# LES COLLECTIONS : LISTES / TUPLES
# Swapper deux éléments (échanger)

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

'''t = noms[0]  # Jean
noms[0] = noms[4]  # Jean <- Zoe
noms[4] = t'''

#                     Zoe      Jean
noms[0], noms[4] = noms[4], noms[0]

print(noms)
