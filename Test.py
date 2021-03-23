import turtle

def draw_X(midx, midy):
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.color("White")
    pen.hideturtle()
    
    pen.penup()
    pen.goto(midx,midy-60)
    pen.pendown()
    pen.circle(60)

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("Black")

#Making the grid pattern
grid = turtle.Turtle()
grid.color("white")
grid.pensize(10)

grid.penup()
grid.goto(-100,265)
grid.right(90)
grid.pendown()
grid.forward(530)

grid.penup()
grid.goto(100,265)
grid.pendown()
grid.forward(530)

grid.penup()
grid.goto(-265,100)
grid.left(90)
grid.pendown()
grid.forward(530)

grid.penup()
grid.goto(-265,-100)
grid.pendown()
grid.forward(530)

draw_X(200,200)
draw_X(-200,0)
draw_X(0,0)
draw_X(0,-200)


