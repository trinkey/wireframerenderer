from turtle import Turtle, Screen
from numpy import dot
from math import cos, sin
from time import sleep

'''
POINT FORMATS:

[x, y, z]

x - left and right
y - how far past the screen
z - up and down

middle of screen is 0, 0, 0
screen size: -400, 0, -400 to 400, 0, 400
'''

points = [
    [-100, 100, -100],
    [100, 100, -100],
    [100, 100, 100],
    [-100, 100, 100],
    [-100, -100, -100],
    [100, -100, -100],
    [100, -100, 100],
    [-100, -100, 100]
]

focalLength = 400

connections = [
    [0, 1],
    [0, 3],
    [0, 4],
    [1, 2],
    [1, 5],
    [2, 3],
    [2, 6],
    [3, 7],
    [4, 5],
    [4, 7],
    [5, 6],
    [6, 7]
]

screen = Screen()
draw = Turtle()

screen.setup(800, 800)
screen.bgcolor("#333333")
screen.tracer(0)

draw.pu()
draw.pensize(2)
draw.color("#ffffff")
draw.hideturtle()

degrees = 44

rotationmatrix = [
    [cos(degrees), 0 - sin(degrees), 0],
    [sin(degrees), cos(degrees), 0],
    [0, 0, 1]
]

while True:
    newpoints = []

    for i in points:
        newpoints.append([
            (focalLength * i[0]) // (i[1] + focalLength),
            (focalLength * i[2]) // (i[1] + focalLength)
        ])

    for i in connections:
        draw.goto(newpoints[i[0]][0], newpoints[i[0]][1])
        draw.pd()
        draw.goto(newpoints[i[1]][0], newpoints[i[1]][1])
        draw.pu()

    screen.update()
    draw.clear()
    points = dot(points, rotationmatrix)
    sleep(0.01)
