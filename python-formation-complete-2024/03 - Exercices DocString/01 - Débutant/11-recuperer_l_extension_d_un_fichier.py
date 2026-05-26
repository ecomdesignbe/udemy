'''
    Récupérer l'extension d'un fichier

    Le but de cet exercice est de récupérer l'extension d'un fichier sans utiliser le module os.

    Dans ce cas-ci, vous devez récupérer l'extension du fichier python.exe.

    Votre script doit retourner l'extension sans le point. Vous devez donc récupérer la chaîne de caractères 'exe' dans la variable extension.

    fichier = "C:/Python36/python.exe"
'''

fichier = "C:/Python36/python.exe"
extension = fichier.split('.')[-1]
print(extension)