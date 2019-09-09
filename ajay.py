from turtle import *

start_pos = [0, 0]
size = 350
a_width = size * .75
a_height = size
j_width = size * .5
j_height = size
y_width = size * .75
y_height = size

def setUp(color, size):
    pencolor(color)
    pensize(size)
    penup()
    start_pos[0] = -600
    start_pos[1] = -175
    setpos(start_pos[0], start_pos[1])
    pendown()
    setheading(0)

def draw_a():
    left(90)
    forward(a_height)
    right(90)
    forward(a_width)
    right(90)
    forward(a_height)
    backward(a_height * .5)
    right(90)
    forward(a_width)

def draw_j():
    left(90)
    forward(j_height)
    right(90)
    forward(j_width)

def draw_y():
    left(90)
    forward(y_height * .5)
    left(90)
    forward(y_width * .5)
    right(90)
    forward(y_height * .5)
    backward(y_height * .5)
    left(90)
    forward(y_width * .5)
    left(90)
    forward(y_height * .5)

def move(dx, dy):
    penup()
    start_pos[0] += dx
    start_pos[1] += dy
    setpos(start_pos[0], start_pos[1])
    pendown()

def draw_ajay(color, pensize):
    setUp(color, pensize)
    draw_a()
    move(a_width + j_width + size * .3, j_height)
    draw_j()
    left(180)
    move(size * .4, -j_height)
    draw_a()
    move(a_width + size * .3, y_height)
    draw_y()

speed('fast')
draw_ajay('#1C0202', size * .2)
draw_ajay('#840F0F', size * .15)
draw_ajay('#BC1515', size * .1)
draw_ajay('#E81818', size * .05)
done()
