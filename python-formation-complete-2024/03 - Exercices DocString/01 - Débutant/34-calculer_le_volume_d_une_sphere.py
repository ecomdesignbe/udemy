'''
    Calculer le volume d'une sphère

    Dans cet exercice, nous allons calculer le volume d'une sphère ayant pour rayon 10 centimètres.

    La formule pour calculer le volume d'une sphère est :

    (4π/3) × rayon³

    rayon représentant la valeur du rayon (défini dans le code par la variable rayon).

    Récupérez la valeur du volume de la sphère dans la variable volume.

    rayon = 10.0
    volume =
'''
import math 
rayon = 10.0
volume = (4/3) * math.pi * (rayon * rayon * rayon) # (rayon ** 3)

print(volume)