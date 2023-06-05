from turtle import Turtle, Screen
import turtle

from sqlalchemy import false
# Python program to draw
# Spiral  Helix Pattern
# using Turtle Programming
 
 #variables
def Gvar():
   global ctrow
   global ctcol
   global gr
   gr=0
   global gc
   gc=0
   global sr
   global visited
   visited={}
   global sc
   global ctv
   ctv=0
   ctrow=0
   ctcol=0
Gvar()

t= Turtle(visible=False)
rows, cols=14,14

grid=[[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    grid[i][0]=1

for i in range(rows):
    grid[i][13]=1
       
for i in range(cols):
    grid[0][i]=1

for i in range(cols):
    grid[13][i]=1
       


#mouse positions
def move_left():
    if(t.xcor()-20>-260):
        t.penup()
        t.setheading(180)
        t.fd(20)
       

def move_right():
    if(t.xcor()+20<-220+480):
      t.penup()
      t.setheading(360)
      t.fd(20)
    

def move_up():
   if(t.ycor()+20<260):
    t.penup()
    t.setheading(90)
    t.fd(20)
  

def move_down():
    if(t.ycor()-20>220-480):

        t.penup()
        t.setheading(270)
        t.fd(20)
       

        
#drawing positions







def fill(x,y,xold,yold):
    
    t.goto(x,y)
    t.fillcolor('black')
    t.pendown()
    t.begin_fill()
    global ctrow
    #grid[ctrow][ctcol]=4
    
    for i in range(4):
        t.fd(40)
        t.rt(90)
    t.penup()
    t.end_fill()

   
        

def check_pos():
    
    startx=-240
    starty=240
    print(t.xcor())
    print(t.ycor())
    for x in range(12):
        
        if(t.xcor()>startx and t.xcor()<startx+40):
           
            for y in range(12):
                
                
               
                
               
                if(t.ycor()<starty and t.ycor()>starty-40):
                
                    grid[y+1][x+1]=1
                    fill(startx,starty,t.xcor(),t.ycor())
                y+=1  
                starty-=40  
        x+=1
        startx+=40





'''
def remove(x,y,xold,yold):
    t.goto(x,y)
    t.fillcolor('white')
    t.pendown()
    t.begin_fill()
    global ctrow
    #grid[ctrow][ctcol]=4
   
    sr=ctrow
    sc=ctcol
    for i in range(4):
        t.fd(40)
        t.rt(90)
    t.penup()
    t.end_fill()
    t.goto(xold,yold)
'''
def remove(x,y,xold,yold,ctcol,ctrow):
    t.goto(x,y)
    t.fillcolor('white')
    t.pendown()
    t.begin_fill()
    grid[ctrow][ctcol]=0
    for i in range(4):
        t.fd(40)
        t.rt(90)
    t.penup()
    t.end_fill()
    
def draw_goal(x,y,xold,yold,ctcol,ctrow):
    t.goto(x,y)
    t.fillcolor('green')
    t.pendown()
    t.begin_fill()
   
    global gc
    global gr

    gr=ctrow
    gc=ctcol

    for i in range(4):
        t.fd(40)
        t.rt(90)
    t.penup()
    t.end_fill()

def goal_pos():
    
  
    startx=-240
    starty=240
    print(t.xcor())
    print(t.ycor())
    for x in range(12):
        
        if(t.xcor()>startx and t.xcor()<startx+40):
            
            for y in range(12):
                
                
                if(t.ycor()<starty and t.ycor()>starty-40):
                    
                    
                 
                    draw_goal(startx,starty,t.xcor(),t.ycor(),x+1,y+1)
                   
                       
                        
                y+=1  
                starty-=40  
        x+=1
        startx+=40


def remove_pos():
  
    startx=-240
    starty=240
    print(t.xcor())
    print(t.ycor())
    for x in range(12):
        
        if(t.xcor()>startx and t.xcor()<startx+40):
            print("x:")
            print(x)
            for y in range(12):
                
                
                if(t.ycor()<starty and t.ycor()>starty-40):
                    
                    grid[y+1][x+1]=0
                 
                    remove(startx,starty,t.xcor(),t.ycor(),x+1,y+1)
                   
                       
                        
                y+=1  
                starty-=40  
        x+=1
        startx+=40


def draw_border():
    t.pendown()
    t.begin_fill()
    for i in range(4):
       t.fd(480)
       t.rt(90)
    
t.penup()
t.end_fill()

 
TURTLE_SIZE = 20

screen = Screen()

t.penup()
t.goto(-240,240)
t.pendown()
t.showturtle()


#screen=Turtle.Screen()
draw_border()
global x
global y
x=-240
y=240
ct=0
dir=90
dir2=40
t.speed(-1)
ct=0
for r in range(12):
   
    for c in range(12):
        t.pendown()
        t.begin_fill()
        t.goto(x,y)
        for i in range(4):
         t.fd(40)
         t.rt(90)
        
        if ct%2==1:
            x-=40
        if ct%2==0:
            x+=40 

    ct+=1
    y-=40
    if ct%2!=0:
        x-=40
    if ct%2==0:
        x+=40
    #x=-240

# import package

def draw_start(x,y,xold,yold,ctcol,ctrow):
    t.goto(x,y)
    t.fillcolor('yellow')
    t.pendown()
    t.begin_fill()
    global sr
    global sc
    
    sr=ctrow
    sc=ctcol
    for i in range(4):
        t.fd(40)
        t.rt(90)
    t.penup()
    t.end_fill()
   
    
# method to action
def start_pos():
    startx=-240
    starty=240
    print(t.xcor())
    print(t.ycor())
    for x in range(12):
        
        if(t.xcor()>startx and t.xcor()<startx+40):
       
            for y in range(12):
                
                
                if(t.ycor()<starty and t.ycor()>starty-40):
                  
                 
                    draw_start(startx,starty,t.xcor(),t.ycor(),x+1,y+1)
                   
                       
                        
                y+=1  
                starty-=40  
        x+=1
        startx+=40
def fillGrid():
    x=0
    i=0
    global sr,sc,gr,gc
    for x in grid:  # outer loop  
        for i in x:  # inner loop  
            print(i, end = " ") # print the elements  
        print()


    
    r=0
    c=0
    print("hi")
    print("sr")
    print(sr)
    print("sc")
    print(sc)
    print("gr")
    print(gr)
    print("gc")
    print(gc)
    for r in range(13):        
        for c in range(13):
            if(grid[r][c]==0 and r>=sr and r<=gr and c>=sc and c<=gc):
               
                array=[r,c]
                grid[r][c]=array
           
            

    x2=0
    i=0
    for x2 in grid:  # outer loop  
        for i in x2:  # inner loop  
            print(i, end = "  ") # print the elements  
        print()


class Node:
   def __init__(self,rrr,ccc):
      self.left = None
      self.right = None
      self.up = None
      self.down= None
      self.datasit=[rrr,ccc]
      self.parent=None

   def insert(self, rrr,ccc):
# Compare the new value with the parent node
      if self.datasit:
         if  rrr==self.datasit:
            if self.left is None:
               self.left = Node(rrr,ccc)
            else:
               self.left.insert(rrr,ccc)
               global ctv
               ctv=1


            if self.right is not None and ctv==1:
               if self.right is None:
                  self.right = Node(rrr,ccc)
               else:
                  self.right.insert(rrr,ccc)
                  ctv=2
            if self.up is not None and ctv==2:
               if self.up is None:
                  self.up = Node(rrr,ccc)
               else:
                  self.up.insert(rrr,ccc)
                  ctv=3 

            if self.down is not None and ctv==3:
               if self.down is None:
                  self.down = Node(rrr,ccc)
               else:
                  self.down.insert(rrr,ccc)
                  ctv=0        
      else:
         self.datasit=[rrr,ccc]


   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.datasit,"ll"),
      if self.right:
         self.right.PrintTree()
      print( self.datasit,"rr"),
      '''
      if self.up:
         self.up.PrintTree()
      print( self.datasit,"uu"),
      if self.down:
         self.down.PrintTree()
      print( self.datasit,"dd"),
      '''




def mainn():

    global sr,sc,gr,gc
    srOld=sr
    scOld=sc
    fillGrid()
    
    path={}
    global visited
    visited = list() 
    fringe = list()

    print("goal pos: ")
    print(gr)
    print(gc)
    print("start pos: ")
    print(sr)
    print(sc)
    print("-------------")
   
    a=0
    print("j: ")
    j=[sr,sc]
    print(j)
    fringe.append(j)
     

    while(a==0):

        print("fringe")
        print(fringe)
        print("visited")
        print(visited)
        ct=0
        childCell=()
        currcell=(fringe[0][0],fringe[0][1])
        if(fringe[0][0]==gr and fringe[0][1]==gc):
            visited.append(fringe[0])
            fringe.pop(0)
            
            print("breaakkkkkkkkkkkkkkkkkkkkkkkk")
            print("fringe")
            print(fringe)
            print("visited")
            print(visited)
            a=8
            break

            

        print("here")
        ct=0
        for i in range(len(visited)):
        
        
            if(visited[i]==fringe[0] ):
            
                ct=1

        if(ct==1):
        
            fringe.pop(0)
            
    #note check for other repeated value in the rest of the fringe not only first element
        else:
        
            print("sr: ")
            print(sr)
            print("sc: ")
            print(sc)

            if(grid[sr-1][sc]!=1):
            
                #print("children")
                #print(grid[sr-1][sc])
                fringe.append(grid[sr-1][sc])
                childCell=(grid[sr-1][sc][0],grid[sr-1][sc][1])
                path[childCell]=currcell

            if(grid[sr+1][sc]!=1):
                print("here2")
                #print("children")
                #print(grid[sr-1][sc])
                fringe.append(grid[sr+1][sc])
                childCell=(grid[sr+1][sc][0],grid[sr+1][sc][1])
                path[childCell]=currcell
        
        
            if(grid[sr][sc-1]!=1):
                
                #print("children")
                #print(grid[sr-1][sc])
                print("here3")
                fringe.append(grid[sr][sc-1])
                childCell=(grid[sr][sc-1][0],grid[sr][sc-1][1])
                path[childCell]=currcell
            if(grid[sr][sc+1]!=1):
                #print("children")
                #print(grid[sr-1][sc])
                print("here4")
                fringe.append(grid[sr][sc+1])
                childCell=(grid[sr][sc+1][0],grid[sr][sc+1][1])
                path[childCell]=currcell
         
            
            visited.append(fringe[0])
            fringe.pop(0)
        
                
        #print(fringe[0][0])
        sr=fringe[0][0]
        sc=fringe[0][1]
    
      #getting path
    goalr=gr
    goalc=gc
    sr=srOld
    sc=scOld
    pathc=list()
    path=list()
    a=0


    '''
    while(a==0):

        if(goalr==sr and goalc==sc):
            break
        if(grid[goalr-1][goalc]!=1):
                
            pathc.append(grid[goalr-1][goalc]!=1)


        if(grid[goalr+1][goalc]!=1):
            print("here2")
            pathc.append(grid[goalr+1][goalc]!=1)

            
        if(grid[goalr][goalc-1]!=1):
            
            pathc.append(grid[goalr][goalc-1]!=1)

        if(grid[goalr][goalc]!=1):
            pathc.append(grid[goalr][goalc+1]!=1)
        
        for i in range(len(pathc)):
            for k in range(len(visited)):
                if(pathc[i]==visited[k]):
                    path.append(pathc[i])
                    val=i
                    break

        goalr=pathc[0][0]
        goalc=pathc[0][1]
    
    print(path)
        
   ''' 
def answer_pos():
        startx=-240
        starty=240
        print(t.xcor())
        print(t.ycor())
        print(len(visited))

        i=0
        for i in range (len(visited)):

            x=1
            y=1
            startx=-240
            starty=240
            for x in range(12):
                
                if(x==visited[i][0]):
            
                    for y in range(12):
                     
                        
                        if(y==visited[i][1]):
                        
                            print(visited[i],x,y,startx,starty)
                            draw_answer(startx-40,starty+40)
                        
                            
                                
                        y+=1  
                        starty-=40  
                x+=1
                startx+=40

def fillGrid2():
    x=0
    i=0
    global sr,sc,gr,gc
    for x in grid:  # outer loop  
        for i in x:  # inner loop  
            print(i, end = " ") # print the elements  
        print()


    
    r=0
    c=0
    print("hi")
    print("sr")
    print(sr)
    print("sc")
    print(sc)
    print("gr")
    print(gr)
    print("gc")
    print(gc)
    for r in range(13):        
        for c in range(13):
            if(grid[r][c]==0 and r>=sr and r<=gr and c>=sc and c<=gc):
               
                array=[r,c]
                grid[r][c]=array
           
            

    x2=0
    i=0
    for x2 in grid:  # outer loop  
        for i in x2:  # inner loop  
            print(i, end = "  ") # print the elements  
        print()

def depth():
    
    global sr,sc,gr,gc
    srOld=sr
    scOld=sc
    fillGrid2()
    visited = list() 
    fringe = list()


    j=[sr,sc]
    print(j)
    fringe.append(j)

    a=0
    while(a==0):

        print("fringe")
        print(fringe)
        print("visited")
        print(visited)
        ct=0
        
        
        if(fringe[0][0]==gr and fringe[0][1]==gc):
            visited.append(fringe[0])
            fringe.pop(0)
            
            print("breaakkkkkkkkkkkkkkkkkkkkkkkk")
            print("fringe")
            print(fringe)
            print("visited")
            print(visited)
            a=8
            break
            

        
        ct=0
        for i in range(len(visited)):
        
        
        
            if(visited[i]==fringe[0] ):
            
                ct=1

        if(ct==1):
        
            fringe.pop(0)
            
    #note check for other repeated value in the rest of the fringe not only first element
        else:
        
            visited.append(fringe[0])
            fringe.pop(0)

            if(grid[sr-1][sc]!=1):
            
                #print("children")
                #print(grid[sr-1][sc])
                fringe.insert(0,grid[sr-1][sc])
            if(grid[sr+1][sc]!=1):
            
                #print("children")
                #print(grid[sr-1][sc])
                fringe.insert(0,grid[sr+1][sc])

        
        
        
            if(grid[sr][sc-1]!=1):
                
                #print("children")
                #print(grid[sr-1][sc])
                fringe.insert(0,grid[sr][sc-1])

            if(grid[sr][sc+1]!=1):
                #print("children")
                #print(grid[sr-1][sc])
                fringe.insert(0,grid[sr][sc+1])
            print("after adding")
            print(fringe)
            
        
        
                

        sr=fringe[0][0]
        sc=fringe[0][1]
    sr=srOld
    sc=scOld
       



        

            
def draw_answer(x,y):
        
        t.goto(-y,-x)
        t.fillcolor('blue')
        t.pendown()
        t.begin_fill()
    
        
        for i in range(4):
            t.fd(40)
            t.rt(90)
        t.penup()
        t.end_fill()

    #answer_pos()  
    
    

def anspath():
    i=0
    print("gggg")
    ccc=visited[0][0]
    rrr=visited[0][1]
    root = Node(rrr,ccc)  
    i+=1 
    while(i<7):
         ccc=visited[i][0]
         rrr=visited[i][1]
         root.insert(rrr,ccc)
         i+=1
             

     
    root.PrintTree()


   



        


        
                
        
        
        
def callDrawOnClick(x,y):
    t.penup()
    t.goto(x,y)
    screen.onkey(check_pos,'space')
    screen.onkey(remove_pos,'d')
    screen.onkey(goal_pos,'g')
    screen.onkey(start_pos,'s')
    screen.onkey(check_pos,'b')

t.goto(-240,240)
t.penup()
screen.onclick(callDrawOnClick)
screen.onkey(mainn,'w')
screen.onkey(depth,'t')
screen.onkey(answer_pos,'l')
screen.listen()
screen.mainloop()

