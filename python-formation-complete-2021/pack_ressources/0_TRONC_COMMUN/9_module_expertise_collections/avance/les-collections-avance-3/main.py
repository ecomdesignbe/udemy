# LES COLLECTIONS : LISTES / TUPLES
# Tris : Sort / Sorted

def tri_longeur_caracteres(nom):
    return len(nom)

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# tri par ordre alphabetique STR
# du plus petit au plus grand INT
#noms.sort(key=tri_longeur_caracteres, reverse=True)  # inplace
noms_tries = sorted(noms, key=tri_longeur_caracteres, reverse=True)  # créer une nouvelle liste

print(noms)
print(noms_tries)


