# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat

while True:
    commande = input("Commande : ")
    if commande == "exit":
        break

    resultat = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)  # dir sur PC

    print(resultat.stdout)
    print(resultat.stderr)
