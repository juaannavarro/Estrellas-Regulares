import turtle



def dibujaEstrella(size, points, puntas, angulos):
    for i,j in zip(puntas, angulos):
        if points == i:
            angle = j

    for x in range(points):
        turtle.forward(size)
        turtle.right(angle)
    return





puntas=[5, 7, 8, 9, 10]
angulos=[144,154,135,160,108]
dibujaEstrella(100, 5, puntas, angulos)
print("Introduzca un número de los que aparecen en 'puntas' en la segunda coordenada de dibujaEstrela2: ")

            

