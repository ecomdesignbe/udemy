# FICHIERS TEXTE
#
# ouvrir (open) <- nom du fichier, mode
# ecrire (write) / lire (read)
# fermer (close)
#

f = open("mon_fichier.txt", "r")

"""texte = f.readline()
print(texte, end="")
texte = f.readline()
print(texte)"""

for line in f:
    print(line, end="")


f.close()


