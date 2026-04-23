# __str__ et __repr__

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    # représentation chaine
    # def __str__(self):
    #    return "STR"

    # dev
    def __repr__(self):
        return __class__.__name__ + " " + str(self.__dict__)

personne1 = Personne("Jean", 20)
personne1.AfficherInfos()

print(personne1)
