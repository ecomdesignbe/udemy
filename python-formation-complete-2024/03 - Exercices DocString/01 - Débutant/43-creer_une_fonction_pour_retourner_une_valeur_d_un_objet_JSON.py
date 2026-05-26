'''
    Créer une fonction pour retourner une valeur d'un objet JSON

    À l'aide de la bibliothèque standard, écrivez une fonction read_object qui lit un objet JSON 
    contenu dans une chaîne de caractères et retourne la valeur associée à la clé donnée en 2e argument, sous la forme d'un objet Python.

    Par exemple :

    >>> read_object('{"x" : [3, "A"], "a" : [1, 2, null]}', "a")
    [1, 2, None]

    json.loads()
    data.get(key, default)

'''
import json

def read_object(data, key):
    d = json.loads(data)
    n = d.get(key, 'none')
    return print(n)

read_object('{"x" : [3, "A"], "a" : [1, 2, null]}', "a")

'''
s = '{"x" : [3, "A"], "a" : [1, 2, null]}'
d = json.loads(s)
print(d)

n = d.get('a', 'none')
print("N:", n)
'''
