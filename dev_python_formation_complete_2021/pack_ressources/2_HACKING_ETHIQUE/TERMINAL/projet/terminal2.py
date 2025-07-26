# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat
resultat = subprocess.run("ls -l", shell=True, capture_output=True, universal_newlines=True)  # dir sur PC

print(resultat.stdout)
print(resultat.stderr)