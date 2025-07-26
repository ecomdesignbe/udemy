# ALIAS DE TYPES
# from typing import TypeAlias

class Personne:
    def __init__(self, nom, age, arg = None):
        self.nom = nom
        self.age = age
    
    def afficher(self):
        print(f"Je suis {self.nom}, j'ai {self.age} ans")

class Etudiant(Personne):
    def __init__(self, nom, age, ecole = ""):
        super().__init__(nom, age)
        self.ecole = ecole

    def afficher(self):
        print(f"Je suis {self.nom}, j'ai {self.age} ans" + " - Etudiant en ecole " + self.ecole)

# TypeDeBase: TypeAlias = Etudiant
TypeDeBase = Personne


personne1 = TypeDeBase("Paul", 20)
personne2 = TypeDeBase("Jean", 18, "IUT")

personne1.afficher()
personne2.afficher()