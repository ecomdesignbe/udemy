# Exemple d'utilisation Tortue approche visuelle
'''
import turtle
t = turtle.Turtle()

t.forward(100)
t.left(90)
t.forward(50)
t.backward(100)
t.right(45)
t.forward(200)

turtle.done()
'''

# Excercice Dessiner un escalier de 5 marches de 30px
''' 
import turtle
t = turtle.Turtle()

for i in range(0, 5):
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.right(90)

t.forward(30)

turtle.done()
'''

# Excercice transformer en une fonction > escalier(taille, nb) 
'''
def escalier(taille, nb):
    import turtle
    t = turtle.Turtle()

    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)

    t.forward(taille)

    turtle.done()

escalier(50, 5)
'''

# Excercice fonction qui dessine un carré > carre(100) 
'''
def carre(n):
    import turtle
    t = turtle.Turtle()

    for i in range(0,4):
        t.forward(n)
        t.left(90)

    turtle.done()

carre(100)
'''

# Excercice fonction qui dessine plusieurs carrés de différentes tailles > carres(taille_depart, nb) / taille = (i+1)*taille_depart / appele la précédente fonction carre
import turtle
t = turtle.Turtle()

# Fonction précédente 
def carre(taille):
    for i in range(0,4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)

carres(50,10)

turtle.done()
