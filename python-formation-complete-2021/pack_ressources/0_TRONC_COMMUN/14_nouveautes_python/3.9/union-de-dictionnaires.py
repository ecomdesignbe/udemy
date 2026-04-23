# UNION DE DICTIONNAIRES

dict1 = {"Jean" : (20, "Développeur"), "Paul" : (30, "Ingénieur")}
dict2 = {"Emilie" : (30, "Professeur"), "Marc" : (25, "Footballer")}

# repertoire_complet =  dict2 | dict1
dict1 |= dict2  # dict1 = dict1 | dict2

print(dict1)