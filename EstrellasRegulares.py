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


def dibujaEstrella2(size, points, puntas, angulos ):
    for i,j in zip(puntas, angulos):
        if points == i:
            angle = j

    for x in range(points):
        turtle.forward(size)
        turtle.right(angle)
    return
            

