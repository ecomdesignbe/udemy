# FICHIERS TEXTE : EXERCICE
# "Ecrire des nombres"

# nombres.txt
# 1
# 2
# 3
# for
# 10 lignes

f = open("nombre.txt", "w")

for i in range(10):
    # print(i+1)
    f.write(str(i+1)+"\n")

f.close()