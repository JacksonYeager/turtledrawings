import turtle 
import random

leo=turtle.Turtle() #creates turtles leo and dona 
dona=turtle.Turtle()

def silly_squiggle(color):#creates a function with color as a parameter 

    if color=="random": #assignes a random color if parameter is "random"
        color = random.choice(["red", "orange", "yellow",
                               "green", "blue", "purple"])
        
    leo.pencolor(color) #sets pen/fill color, begins fill  
    leo.fillcolor(color)
    leo.begin_fill()
    
    for i in range(10): #loop to create a random figure
        distance = random.randint(1,100)
        angle =random.randint(1,90)
        leo.forward(distance)
        leo.right(angle)
        
    leo.end_fill() #ends fill and repositions the turtle 
    leo.penup()
    leo.forward(100)
    leo.pendown()
    
silly_squiggle("random")#calls 2 functions 
silly_squiggle("violet")

def spiral(t): #creates a function with t for turtle in parameter 

    t.speed(10) #sets a faster speed  
    t.penup()  #(for the most part) repositions turtle from other shapes
    t.forward(300)
    t.pendown()
    
    rainbow=["red", "orange", "lightgreen", #creates a list of colors
              "cyan", "violet"]
    color=0
    
    for i in range(1, 100): #draws spiral shape and iterates list of colors 
        if color>4:
            color=0
        t.pencolor(rainbow[color])
        t.forward(i)
        t.right(71)
        color+=1
        
spiral(dona) #calls 2 functions
spiral(leo)
