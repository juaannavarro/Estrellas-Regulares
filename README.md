# Estrellas-Regulares
Para hacer la tarea de estrellas regulares hemos creado un repositorio cuya dirección es: https://github.com/juaannavarro/Estrellas-Regulares

La tarea consiste en:

<img width="954" alt="Captura de pantalla 2021-12-19 a las 22 59 54" src="https://user-images.githubusercontent.com/91721668/146819261-eb487a45-996c-443f-89ac-7387e9bbfc73.png">

Para ello hemos creado el siguiente código:

import turtle

def dibujaEstrella(size, points, angle):
    angle2= 360/points+angle

    for x in range(points*2):
        turtle.forward(size)
        if x%2==0:
            turtle.left(180-angle)
        else:
            turtle.right(180-angle2)
        return


def dibujaEstrella2(size, points, puntas, angulos):
    for i,j in zip(puntas, angulos):
        if points == i:
            angle = j

    for x in range(points):
        turtle.forward(size)
        turtle.right(angle)
    return



turtle.clearscreen()

puntas=[5, 7, 8, 9, 10]
angulos=[144,154,135,160,108]
dibujaEstrella2(100, 5, puntas, angulos)
print("Introduzca un número de los que aparecen en 'puntas' en la segunda coordenada de dibujaEstrela2: ")

Aparte del código debemos de crear un diagrama de flujo. Para esta tarea el diagrama es:

<img width="344" alt="Captura de pantalla 2021-12-20 a las 20 18 19" src="https://user-images.githubusercontent.com/91721668/146820795-3b89476b-3e6d-4d93-abd6-f769e2372445.png">



