import math
import random
import turtle



s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("#1c1b1b")
t.pencolor("#d6d6d4")
t.speed(10)
turtle.title("Ant colony optimization demo")
t.hideturtle() 
arr = []
def shopPlace(seed, n):
    random.seed(seed)
    for l in range(n):
        check = 0
        x = math.ceil(random.random()*300) -150
        y = math.ceil(random.random()*300) -150
        ar = [x,y]
        for xx in arr:
            
            num = (xx[0]*xx[0] - ar[0]*ar[0]) + (xx[1]*xx[1] - ar[1]*ar[1])
            print(num)
            dist = math.sqrt(abs(num))
            print(dist)
            
            if dist < 50:
                x = x + 50 - abs(xx[0] - ar[0])
                y = y + 50 - abs(xx[1] - ar[1])
        arr.append(ar)
        
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot(15)
def antPlace():
    t.penup()
    ch = random.randrange(0,len(arr))
    print(ch)
    pa = arr[ch]
    print(pa)
    t.goto(pa[0],pa[1])
    t.pendown()
seedd = input("Enter a seed: ")
shopPlace(seedd, 10)
antPlace()
input("Enter any random string to exit: ")
turtle.done()