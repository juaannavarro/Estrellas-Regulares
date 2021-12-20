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
        
