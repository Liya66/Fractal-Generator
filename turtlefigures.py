from turtle import *
import math


# binary tree
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)

#end


# quadratic tree
def d(n,l,pen):
     # termination
     if n ==0 or l<2:
          return
     #endif
     pen.forward(l)
     pen.left(90)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.right(60)
     d(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)
#end d

def f(n,l,pen):
# termination
     if n ==0 or l<2:
          return
     #endif
     pen.forward(0.3*l)
     pen.right(45);f(n-1,l/2,pen);pen.left(45)
     pen.forward(0.7*l)
     pen.left(30);f(n-1,l/2,pen);pen.right(30)
     pen.forward(l)
     pen.right(10);f(n-1,0.8*l,pen);pen.left(10)
     pen.backward(2*l)

     #end
def koch(n,l,pen):
     if n ==0 or l<2:
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3,pen)
     pen.left(60);koch(n-1,l/3,pen)
     pen.right(120);koch(n-1,l/3,pen)
     pen.left(60);koch(n-1,l/3,pen)

#end k
def antiflake(n,l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.left(120)
     #endflake

#end k
def flake(n,l,pen):
     for i in range(3):
          koch(n,l,pen)
          pen.right(120)
     #endflake


#draw the gasket3
def gasket3(n,l,pen):
     #termination
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          #end for
          return
     #end if
     gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
     gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
     gasket3(n-1,l/2,pen);pen.forward(l);pen.left(120)
#end gasket3


def gasket4(n,l,pen):
    if n == 0 or l<2:
        for n in range(4):
            pen.forward(l)
            pen.left(90)
        return
    for i in range(4):
         gasket4(n-1,l/3,pen);pen.forward(l/3);
         gasket4(n-1,l/3,pen);pen.forward(l/3);
         gasket4(n-1,l/3,pen);pen.forward(l/3);
         pen.left(90)



def gasket6(n, l,pen):
    if n == 0 or l<2:
        for i in range(6):
            pen.forward(l)
            pen.left(60)
        return
    for i in range(6):
        gasket6(n-1,l/3,pen)
        pen.forward(2*l/3)
        gasket6(n-1,l/3,pen)
        pen.forward(l/3)
        pen.left(60)

def gasketC(n,radius,pen):
    if n == 0 or radius<2:
        for i in range(2):
            pen.circle(radius)
        return
    for i in range(2):
        gasketC(n-1, radius,pen)
        gasketC(n-1,radius/2,pen)
        pen.left(90)
        pen.penup()
        pen.forward(radius)
        pen.pendown()
        gasketC(n-1,radius/2,pen)
        pen.penup()
        pen.forward(radius)
        pen.pendown()
        pen.left(90)

def gasketc3(n, radius,pen):
    if n == 0 or radius < 2:
        for i in range(3):
            pen.circle(radius)
        return
    for i in range(3):
        gasketc3(n-1,radius,pen)
        gasketc3(n-1,3*radius/(3+2*math.sqrt(3)),pen)
        pen.left(90)
        pen.penup()
        pen.forward((1+math.sqrt(3))*3*radius/(3+2*math.sqrt(3)))
        pen.pendown()
        gasketc3(n-1,3*radius/(3+2*math.sqrt(3)),pen)
        pen.left(180)
        gasketc3(n-1,3*radius/(3+2*math.sqrt(3)),pen)
        pen.penup()
        pen.left(90)
        pen.forward(3*radius/(3+2*math.sqrt(3)))
        pen.left(30)
        pen.forward(3*radius/(3+2*math.sqrt(3)))
        pen.left(90)
        pen.pendown()
        
def gasketC2(n,radius,pen):
    if n == 0 or radius<2:
        for i in range(2):
            pen.circle(radius)
        return
    for i in range(2):
        #draw the big circle
        gasketC2(n-1, radius,pen)
        #draw the first small one with the same starting point
        gasketC2(n-1,radius/2,pen)
        #move the pen up to the center
        pen.left(90)
        pen.penup()
        pen.forward(2*radius)
        pen.pendown()
        #draw the second small circle
        pen.left(90)
        gasketC2(n-1,radius/2,pen)
        

def gasketC4(n,radius,pen):
    if n == 0 or radius<2:
        for i in range(4):
            pen.circle(radius)
        return
    for i in range(4):
        #draw the big and first small circle
        gasketC4(n-1, radius,pen)
        gasketC4(n-1, radius*(math.sqrt(2)-1),pen)
        #move the pen
        pen.penup()
        pen.left(135)
        pen.forward(radius*math.sqrt(2))
        pen.left(135)
        #draw the second small circle
        pen.pendown()
        gasketC4(n-1, radius*(math.sqrt(2)-1),pen)
        #move the pen
        pen.penup()
        pen.left(135)
        pen.forward(radius*math.sqrt(2))
        pen.left(135)
        pen.pendown()


def flower(n, l,pen):
    if n == 0 or l<2:
        for i in range(8):
            pen.forward(l)
            pen.left(135)
        return
    for i in range(8):
        flower(n-1,l/3,pen)
        pen.forward(2*l/3)
        flower(n-1,l/3,pen)
        pen.forward(l/3)
        pen.left(135)

def grid(n,l,pen):
     #termination
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #end for
          return
     #end if
     grid(n-1,l/2,pen);pen.forward(l);pen.left(90)
     grid(n-1,l/2,pen);pen.forward(l);pen.left(90)
     grid(n-1,l/2,pen);pen.forward(l);pen.left(90)
     grid(n-1,l/2,pen);pen.forward(l);pen.left(90)

def cross(n,l,pen):
     #termination
     if n==0 or l<2:
          for i in range(4):
               pen.forward(l)
               pen.left(90)
          #end for
          return
     #end if
     cross(n-1,l/3,pen);pen.forward(l);pen.left(90)
     cross(n-1,l/3,pen);pen.forward(l);pen.left(90)
     cross(n-1,l/3,pen);pen.forward(l);pen.left(90)
     cross(n-1,l/3,pen);pen.forward(l);pen.left(90)

#draw Penta doily    
def gasket5(n, l, pen):
    if n == 0 or l<2:
        for i in range(5):
            pen.forward(l)
            pen.left(72)
        return
    for i in range(5):
        gasket5(n-1,l/3,pen)
        pen.forward(2*l/3)
        gasket5(n-1,l/3,pen)
        pen.forward(l/3)
        pen.left(72)


