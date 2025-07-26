# FICHIERS TEXTE
#
# ouvrir (open) <- nom du fichier, mode
# ecrire (write) / lire (read)
# fermer (close)
#

f = open("mon_fichier.txt", "w")

# f.write("Bonjour\n")
# f.write("Bonjour")
l = ["premiere phrase", "deuxieme phrase", "troisieme"]

f.write("\n".join(l))

f.write("\nFin")

f.close()


