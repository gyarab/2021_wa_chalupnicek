# import turtle 
from turtle import *
import math

def domecek(size):
    diagonal = math.sqrt(2 * size ** 2)

    forward(size)
    left(90)
    forward(size)
    left(45)
    forward(diagonal/2)
    left(90)
    forward(diagonal/2)
    left(135)
    forward(size)
    right(135)
    forward(diagonal)
    right(135)
    forward(size)
    right(135)
    forward(diagonal)   
    left(45)

domecek(20)
domecek(20)
domecek(20)

# speed(1)

# for i in range(8):
#     domecek(i * 10)

exitonclick()