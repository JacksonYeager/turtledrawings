import turtle as t
t.shape("turtle")

#begins fill as purple
t.fillcolor("purple")
t.begin_fill()

#draws square and ends fill
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

#moves turtle to the right of square
t.penup()
t.forward(120)
t.left(120)
t.pendown()

#begins fill as orange
t.fillcolor("orange")
t.begin_fill()

#draws hexagon and ends fill
for i in range (6):
    t.forward(20)
    t.right(60)
t.end_fill()

#moves turtle above hexagon
t.penup()
t.right(30)
t.forward(100)
t.pendown()

#begins fill as red
t.fillcolor("red")
t.begin_fill()

#draws non regular hexagon and end fill
t.forward(50)
t.right(45)
t.forward(50)
t.right(90)
t.forward(50)
t.right(45)
t.forward(50)
t.right(135)
t.forward(50)
t.left(90)
t.forward(50)
t.end_fill()

#moves turtle to the left
t.penup()
t.right(45)
t.forward(200)
t.pendown()

#begins fill as blue
t.fillcolor("blue")
t.begin_fill()

#draws rectangle and ends fill
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()
