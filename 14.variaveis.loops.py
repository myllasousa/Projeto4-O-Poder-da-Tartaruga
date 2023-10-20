from turtle import *
shape("turtle")
speed(11)
pensize(6)

color("Red")

lados = 4
angulo = 360 / lados

for count in range(4):
    forward(100)
    left(angulo)

done()
