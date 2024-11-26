import turtle 
import random
leo=turtle.Turtle()
dona=turtle.Turtle
def silly_shape(color):
    if color=="random":
        color = random.choice(["red", "orange", "yellow","green", "blue", "purple"])
    leo.pencolor(color)
    for i in range(10):
        distance = random.randint(1,100)
        angle =random.randint(1,90)
        leo.forward(distance)
        leo.right(angle)        
silly_shape("random")
silly_shape("red")

def spiral(t):
    for i in range(360):
        t.forward(20)
        t.right(1-i)
spiral(leo)
