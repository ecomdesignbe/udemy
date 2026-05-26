'''
    Modifier le sys path
    
    Dans cet exercice, vous allez devoir modifier la variable path du module `sys.

    Vous devez donc importer ce module et ajouter à la variable path le chemin "/Users/Docstring/mon_module_python".

    '''

import sys
sys.path.append('/Users/Docstring/mon_module_python')
print("Path : ", sys.path)