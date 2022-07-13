"""
CS51a Assignment 2
Hasana Parker
1/31/2022

Note: the turtle module imports turtle and allows the ability to draw, The random module allows for the use of random
integers. The purpose of this module is to draw a space scene. For extra credit, I included a spiral in my drawing as
well as making the star function.
"""

from turtle import *
from random import randint

wn = Screen()


def triangle(x, y, side_length):
    """
    The function triangle is making random triangles throughout the picture.
    :param x: (int) x coordinate of triangle
    :param y: (int) y coordinate of triangle
    :param side_length: (int) side length of equilateral triangle
    """
    penup()
    goto((x, y))
    setheading(90)
    pendown()

    begin_fill()
    for i in range(6):     # range is 6 to make the code run 6 times, and draw all sides of the triangle.
        forward(side_length)
        right(120)
    end_fill()


pencolor("#ffd3e8")


def polygon(x, y, num_of_sides, length_of_sides):
    """
    This code is working draw polygons of any number of sides.
    :param x: (int) is the x coordinate of the polygon
    :param y: (int) is the y coordinate of the polygon
    :param num_of_sides: (int) is a value you input for the number of sides you want in the polygon.
    :param length_of_sides: (int) is the value of the length of the polygon and will determine it's size
    :return: none
    """
    penup()
    goto((x, y))
    pendown()
    setheading(90)

    begin_fill()
    for i in range(num_of_sides):
        forward(length_of_sides)
        right(360/num_of_sides)   # the angles in the polygon is determined by the number of sides.
    end_fill()


def add_circles(num_of_circles):
    """
    This is the  code for the creation of the planets. The function add-circles, place random circles of random sizes
    throughout the picture.
    :param num_of_circles: (int) is a values inputted for the desired amount of circles.
    :return: none
    """
    for i in range(num_of_circles):
        penup()
        goto((randint(-300, 400), randint(-300, 400)))  # places the circle in random places on the screen.
        pendown()
        begin_fill()
        circle(randint(40, 70))  # makes the circles random sizes.
        end_fill()


# Setting up the coordinates for my blue planet saturn, as well as the pen color
penup()
goto(-300, 300)
pendown()


def saturn(num_of_saturn):
    """Here is the code for a circle that I wanted to have a fill color different from all the rest
    :param num_of_saturn: (int) value for the number of blue planets wanted
    :return: none
    """
    for i in range(num_of_saturn):
        begin_fill()
        circle(70)
        end_fill()


color("white")
speed(15)


def star(num_of_stars):
    """This function is to draw random stars all over the space. Can't Figure out how to make it so I have multiple
     stars random across the screen
    :param num_of_stars: (int) value for number of stars wanted
    :return: none
    """
    for i in range(num_of_stars):
        penup()
        goto((randint(-420, 420), randint(-393, 393)))
        pendown()
        for j in range(5):    # the code needed to draw one star
            forward(20)
            left(216)


def sun(num_of_lines):
    """ This function is making creating a turtle star as a representation of the sun. The function flower takes the
     parameter num_of_lines to represent the amount of strokes being created.
     :param num_of_lines: (int) the input for this determines the amount of times the lines in the sun are drawn.
     """
    for i in range(num_of_lines):
        forward(200)
        left(170)


def spiral(sides, angle):
    """ This is the code for the spiral in the middle of the screen.
    :param sides:(int) sides in the spiral
    :param angle: (int) angle at which the spiral is turning
    """
    for i in range(sides):
        forward(i * 5)
        right(angle)


def rectangle(x, y, height, length):
    """
    This is the extra practice to make a rectangle. This function generates rectangles across the screen
    and assigns them different colors depending on if the height is greater than the length(color is #B26E63), if the
    length is greater than the height(color is #219EBC), or if it is a square( color is #EF233C).

    :param x: (int) x coordinate of rectangle
    :param y: (int) y coordinate of rectangle
    :param height: (int) is the height of the rectangle
    :param length: (int) is the length of the rectangle
    """
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    for i in range(4):
        forward(length)
        right(90)
        forward(height)
        right(90)

    if height > length:
        color("#B26E63")
    elif length == height:
        color("#EF233C")
    else:
        color("#219EBC")
    end_fill()

# rectangle(300, 90, 100, 50)
# rectangle(300, 60, 50, 50)
# rectangle(300, -160, 50, 100)
# running code to prove code works.


def generate_picture():
    """ generate_picture is a function that will execute all the code in one function. """
    bgcolor("black")
    speed(0)

    fillcolor("#9DA9A0")
    triangle(0, -300, 50)
    triangle(300, 300, 80)
    triangle(100, -100, 90)
    triangle(200, 200, 80)
    triangle(150, 150, 80)
    triangle(250, -250, 80)

    fillcolor("#EDDFEF")
    polygon(420, 200, 8, 50)
    polygon(-420, -300, 8, 50)
    polygon(220, -320, 8, 40)
    polygon(-380, 320, 8, 50)
    polygon(-100, 250, 8, 40)
    polygon(-90, 100, 8, 40)

    star(40)

    fillcolor("#C3BEF7")
    add_circles(6)

    penup()
    goto(-300, 300)
    pendown()
    color("#1C6E8C")
    fillcolor("#1C6E8C")
    saturn(1)

    penup()
    goto(410, 360)
    pendown()
    color("orange")
    sun(100)

    color("white")
    penup()
    goto(0, 0)
    pendown()
    spiral(90, 89)


generate_picture()

exitonclick()
