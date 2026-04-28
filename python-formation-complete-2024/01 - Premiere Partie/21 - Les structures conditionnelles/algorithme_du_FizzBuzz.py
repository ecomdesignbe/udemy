'''
Algorithme du FizzBuzz

    Le challenge FizzBuzz est un classique pour évaluer les bases de programmation. 

    L'objectif de cet exercice est d'écrire un programme qui affiche les nombres de 1 à 100 avec les exceptions suivantes :

    Pour les multiples de 3, on affiche 'Fizz' à la place du nombre.

    Pour les multiples de 5, on affiche 'Buzz' à la place du nombre.

    Pour les multiples de 3 et 5, on affiche 'FizzBuzz' à la place du nombre.

    Exemple
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    ...
'''


# affiche les nombres de 1 à 100
# multiples de 3, on affiche 'Fizz' à la place du nombre.
# multiples de 5, on affiche 'Buzz' à la place du nombre.
# multiples de 3 et 5, on affiche 'FizzBuzz' à la place du nombre.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:        
        print('Fizz')               
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i += 1    
