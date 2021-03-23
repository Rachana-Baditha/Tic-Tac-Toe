import turtle

#Checking win condition
def win_check(player): 
    win = False
    
    if (1 in player) and (4 in player) and (7 in player):
        win = True
        win_line(1)
    elif (2 in player) and (5 in player) and (8 in player):
        win = True
        win_line(2)
    elif (3 in player) and (6 in player) and (9 in player):
        win = True
        win_line(3)
    elif (1 in player) and (2 in player) and (3 in player):
        win = True
        win_line(4)
    elif (4 in player) and (5 in player) and (6 in player):
        win = True
        win_line(5)
    elif (7 in player) and (8 in player) and (9 in player):
        win = True
        win_line(6)
    elif (1 in player) and (5 in player) and (9 in player):
        win = True
        win_line(7)
    elif( 3 in player) and (5 in player) and (7 in player):
        win = True
        win_line(8)
        
    return win

#Drawing winning strike
def win_line(n):
    
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.color("White")
    pen.hideturtle()
    pen.penup()

    #Column Wins
    if n==1:
        pen.goto(-200,300)
        pen.pendown()
        pen.goto(-200,-300)
    
    elif n==2:
        pen.goto(0,300)
        pen.pendown()
        pen.goto(0,-300)
        
    elif n==3:
        pen.goto(200,300)
        pen.pendown()
        pen.goto(200,-300)
        
    #Row Wins
    elif n==4:
        pen.goto(-300,200)
        pen.pendown()
        pen.goto(300,200)
        
    elif n==5:
        pen.goto(-300,0)
        pen.pendown()
        pen.goto(300,0)
        
    elif n==6:
        pen.goto(-300,-200)
        pen.pendown()
        pen.goto(300,-200)
        
    #Diagonal Wins
        
    elif n==7:
        pen.goto(-300,300)
        pen.pendown()
        pen.goto(300,-300)
        
    elif n==8:
        pen.goto(300,300)
        pen.pendown()
        pen.goto(-300,-300)
        



#Draw X
def draw_X(midx, midy):
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.color("White")
    pen.hideturtle()
    
    pen.penup()
    pen.goto(midx-60, midy+60)
    pen.pendown()
    pen.goto(midx+60, midy-60)
    
    pen.penup()
    pen.goto(midx-60, midy-60)
    pen.pendown()
    pen.goto(midx+60, midy+60)
    
#Draw O
def draw_O(midx, midy):
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.color("White")
    pen.hideturtle()
    
    pen.penup()
    pen.goto(midx,midy-60)
    pen.pendown()
    pen.circle(60)
    
#Drawing X and O
def mark_XO(x,y):
    
    global turn
    
    #Box 1
    if ( x>-300 and x<=-100 ) and ( y>100 and y<=300 ):
        
        if 1 in player_1 or 1 in player_2:
            return
        
        if turn%2==1:
            draw_X(-200,200)
            player_1.append(1)
        else:
            draw_O(-200,200)
            player_2.append(1)
            
    #Box 2
    elif ( x>-100 and x<=100 ) and ( y>100 and y<=300 ):
        
        if 2 in player_1 or 2 in player_2:
            return
        
        if turn%2==1:
            draw_X(0,200)
            player_1.append(2)
        else:
            draw_O(0,200)
            player_2.append(2)
            
    #Box 3
    elif ( x>100 and x<=300 ) and ( y>100 and y<=300 ):
        
        if 3 in player_1 or 3 in player_2:
            return
        
        if turn%2==1:
            draw_X(200,200)
            player_1.append(3)
        else:
            draw_O(200,200)
            player_2.append(3)
            
    #Box 4
    elif ( x>-300 and x<=-100 ) and ( y>-100 and y<=100 ):
        
        if 4 in player_1 or 4 in player_2:
            return
        
        if turn%2==1:
            draw_X(-200,0)
            player_1.append(4)
        else:
            draw_O(-200,0)         
            player_2.append(4)
            
    #Box 5
    elif ( x>-100 and x<=100 ) and ( y>-100 and y<=100 ):
        
        if 5 in player_1 or 5 in player_2:
            return
        
        if turn%2==1:
            draw_X(0,0)
            player_1.append(5)
        else:
            draw_O(0,0)
            player_2.append(5)
            
    #Box 6
    elif ( x>100 and x<=300 ) and ( y>-100 and y<=100 ):
        
        if 6 in player_1 or 6 in player_2:
            return
        
        if turn%2==1:
            draw_X(200,0)
            player_1.append(6)
        else:
            draw_O(200,0)
            player_2.append(6)
            
    #Box 7
    elif ( x>-300 and x<=-100 ) and ( y>-300 and y<=-100 ):
        
        if 7 in player_1 or 7 in player_2:
            return
        
        if turn%2==1:
            draw_X(-200,-200)
            player_1.append(7)
        else:
            draw_O(-200,-200)
            player_2.append(7)
            
    #Box 8
    elif ( x>-100 and x<=100 ) and ( y>-300 and y<=-100 ):
        
        if 8 in player_1 or 8 in player_2:
            return
        
        if turn%2==1:
            draw_X(0,-200)
            player_1.append(8)
        else:
            draw_O(0,-200)
            player_2.append(8)
            
    #Box 9
    elif ( x>100 and x<=300 ) and ( y>-300 and y<=-100 ):
        
        if 9 in player_1 or 9 in player_2:
            return
        
        if turn%2==1:
            draw_X(200,-200)
            player_1.append(9)
        else:
            draw_O(200,-200)
            player_2.append(9)
            
    turn+=1

#Setting up board
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("Black")
wn.tracer(0)
    
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
    
#Players
global player_1 
player_1 = []
    
global player_2 
player_2 = []
    
global turn
turn = 1 

wn.onscreenclick(mark_XO)
    
win1 = False
win2 = False
    
#Main Game Loop
while (not win1) and (not win2):
    wn.update()
    
    win1 = win_check(player_1)
    win2 = win_check(player_2)
        
    wn.update()
        
        
