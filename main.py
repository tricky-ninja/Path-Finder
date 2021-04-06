import math
import random
import turtle


    
# stores the list of towns and the list of visited towns
town = []  
done = []

#function for calculating the distance
def dist(cp,dp): 
    num = (dp[0]*dp[0] - cp[0]*cp[0]) + (dp[1]*dp[1] - cp[1]*cp[1])
    dist = math.sqrt(abs(num))
    return dist


# function for generating a random set of towns based on a seed
def town_place(seed, n):
    random.seed(seed)
    for l in range(n):  # generates `n` number of towns
        
        x = math.ceil(random.random()*300) -150  # x coordinate
        y = math.ceil(random.random()*300) -150  # y coordinate
        ar = [x,y]  # list that stores both x and y coordinates 

        # calculates the distance from current town to all town and space them if the distance is less than 20
        for xx in town: 
            if dist(ar,xx) < 20:
                x = x + 20 - abs(xx[0] - ar[0])
                y = y + 20 - abs(xx[1] - ar[1])
                ar = [x,y]
        town.append(ar) # adds current town to the list of towns
        
        #draw the towns
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot(5)

# function to place an ant in a random town
def ant_place():
    t.penup()
    ch = random.randint(0,len(town) - 1)
    
    pa = town[ch]
    
    t.goto(pa[0], pa[1])
    t.pendown()
    return pa

# function to return the towns sorted according to their distance from the current position
def short(r):
    distance = []
    near_town = []
    for point in town:
        distance.append(dist(r,point))
    temp = distance
    temp.sort()
    for i in range(len(temp)):
        #if i == len(temp) - 1: break
        #i = i + 1 
        index = distance.index(temp[i])
        near_town.append(town[i])
    
    return near_town

# function to move to the nearest town
def move(r):
    cord = r
    done.append(r)
    for i in range(len(town) - 1):
        l = 0
        
        near_town = short(cord)
        
        while (near_town[l] in done):
            if l == len(near_town): break
            l = l + 1

        next_town = near_town[l]
        t.pendown()
        t.pencolor("#faaf9b")
        t.speed(5)
        xloc = next_town[0]
        yloc = next_town[1]
        t.goto(xloc, yloc)
        cord = [xloc, yloc]
        done.append(cord)
    t.speed(10)
    t.penup()
    t.pencolor("#d6d6d4")
        


seed = input("Enter a seed: ")
num = input("Enter number of towns: ")
s = turtle.getscreen()
t = turtle.Turtle()
t.pencolor("#d6d6d4")
t.speed(10)
turtle.title("Ant colony optimization demo")
turtle.screensize(canvwidth=400*(num/(num/5)), canvheight=300*(num/(num/5)),
                  bg="#1c1b1b")
t.hideturtle() 
town_place(seed, num)
r = ant_place()
move(r)



turtle.done()