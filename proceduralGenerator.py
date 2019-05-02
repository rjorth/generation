import random
from turtle import *



#establish turtles 
sky = Turtle()
sky.color('#e5e5ff')
sky.pensize(100)
sky.speed(0)

water = Turtle() 
mountains = Turtle() 
clouds = Turtle() 
sun = Turtle()
sun.speed('fastest')
cut = Turtle() 

turtles = [sky, water, mountains, clouds, sun]

#built ins

def penup():
    for i in turtles:
        i.penup()
def pendown():
    for i in turtles:
        i.pendown()
def speed():
    for i in turtles:
        i.speed(0)
        i.hideturtle()


penup()
sky.goto(-240,-300)
pendown()

get_sky = random.randint(0,3)

if get_sky == 0: #daytime
	skycol = ['#85C1E9','#85C1E9','#85C1E9','#85C1E9', '#85C1E9','#85C1E9','#85C1E9','#85C1E9','#AED6F1','#AED6F1','#AED6F1','#AED6F1','#AED6F1','#AED6F1','#AED6F1']
elif get_sky == 1: #sunset
	skycol = ['#add8e6','#add8e6','#b5d8e5','#bdd8e4','#c5d8e3','#cdd8e3','#d6d8e2','#ded8e1','#e6d8e1','#eed8e0','#f6d8df','#ffd9df','#ffd9df','#ffd9df','#ffd9df']
elif get_sky == 2: 
	skycol = ['#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#D6EAF8','#FDF2E9','#FDF2E9','#FDF2E9','#FDF2E9','#FAE5D3','#FAE5D3','#FAE5D3','#FAE5D3']

else: #nighttime 
	skycol = ['black', 'black','black','black','black','black','black','black','black','black','black','black','black','black','black']

def drawsky():
    for i in skycol:
        sky.color(i)
        sky.forward(500)
        sky.left(90)
        sky.forward(20)
        sky.left(90)

        sky.color(i)
        sky.forward(500)
        sky.right(90)
        sky.forward(20)
        sky.right(90)




def drawmountainss():
    penup()
    mountains.goto(-300,-100)
    pendown()
    mountains.speed('fastest')
    mountains.begin_fill()

    #first layer 
    for i in range(15):
        cross_screen = random.randint(10,250) #20/200
        
        make_peak = random.randint(50,90) #45/80
        
        mountains.left(make_peak)
        mountains.forward(cross_screen)
        mountains.right(2*make_peak)
        mountains.forward(cross_screen)
        mountains.setheading(0)
        
    mountains.goto(300,-400)
    mountains.goto(-300,-400)
    mountains.end_fill()

    second_color = ['#7e8b99','#F2F3F4','#56606b','#a7b1bc']

    mountains.color(second_color[random.randint(0,len(second_color)-1)])
    penup()
    mountains.goto(-300,-150)
    pendown()
    mountains.begin_fill()

    #second layer
    for i in range(15):
        cross_screen = random.randint(20,200)
        
        make_peak = random.randint(30,50)
        
        mountains.left(make_peak)
        mountains.forward(cross_screen)
        mountains.right(2*make_peak)
        mountains.forward(cross_screen)
        mountains.setheading(0)
        
    mountains.goto(300,-400)
    mountains.goto(-300,-400)
    mountains.end_fill()

    third_color = ['#145A32','#1f603b','#427235','#67a855']

    mountains.color(third_color[random.randint(0,len(third_color)-1)]) 
    penup()
    mountains.goto(-300,-165)
    pendown()
    mountains.begin_fill()
    
    #third layer 
    for i in range(15):
        cross_screen = random.randint(20,200)
        
        make_peak = random.randint(10,30)
        
        mountains.left(make_peak)
        mountains.forward(cross_screen)
        mountains.right(2*make_peak)
        mountains.forward(cross_screen)
        mountains.setheading(0)
        
    mountains.goto(300,-400)
    mountains.goto(-300,-400)
    mountains.end_fill()


def drawwater():

    b,b2 = random.randint(0,6),random.randint(0,6)

    xloc, yloc = random.randint(200,300), random.randint(200,300)

    blues = ['blue','lightblue','darkblue','gray','brown','tan','lightgreen']

    penup()
    water.goto(-xloc,-yloc) #-200,-200 good, -300,-300 ok, -250,-250 good 
    water.color(blues[b], blues[b2])
    water.shape('circle')
    water.begin_fill()
    water.shapesize(4,10,1)
    water.end_fill()


def drawclouds():

    clouds.color('white')
    clouds.speed('fastest')

    def brush_random(randloc,stroke):
        penup()
        clouds.goto(randloc)
        pendown()
        clouds.pensize(random.randint(3,5))
        clouds.forward(stroke)
        
    def get_cloud():

        stroke = 30
        xloc, yloc = random.randint(0,350), random.randint(-200,270) #0,350 #0,270 good 
            
        for i in range(random.randint(15,30)): #20
            temp = (yloc, xloc)
            brush_random(temp,stroke)
            xloc += 1
            yloc += random.randint(-10,10)
            stroke += random.randint(-40,40)

    for i in range(3):    
        get_cloud()


def drawsun():

	#sun.speed('fastest')

    if get_sky == 0:
    	sun.speed('fastest')
    	sun.color('pink', 'gold')
        sun.begin_fill()
        #make small
        cstar = random.randint(150,250)
        #make pos
        dstar = random.randint(50,150)

        #forward positive, left negative for upper right corner 
        while True:
            sun.forward(380) #380
            sun.left(-250) #-250
            if abs(sun.pos()) < 1:
                break
        sun.end_fill()

    elif get_sky == 1 or get_sky == 2:
    	sun.color('white', 'white')
      	sun.penup()
      	sun.goto(250,250)
      	sun.pendown()
      	sun.begin_fill()
      	colors = ["red", "orange", "yellow", "lightblue", "gold", "purple","pink"]
        sun.color(colors[random.randint(0,5)])

        for x in range (0, 360):
          	sun.forward(100)
          	sun.left(180)
          	sun.forward(100)
          	sun.right(1)

        sun.penup()
        sun.forward(50)
        sun.right(90)
        sun.forward(50)
        sun.pendown()
        sun.color(colors[random.randint(0,5)])
          
        for i in range (0, 360):
	      	sun.forward(100)
	      	sun.left(180)
	      	sun.forward(100)
	      	sun.right(1)


    else:
    	sun.color('white', 'white')
      	sun.penup()
      	sun.goto(250,250)
      	sun.pendown()
      	sun.begin_fill()
        sun.color('white')

        for x in range (0, 360):
          	sun.forward(100)
          	sun.left(180)
          	sun.forward(100)
          	sun.right(1)

        sun.penup()
        sun.forward(50)
        sun.right(90)
        sun.forward(50)
        sun.pendown()
        sun.color("black")
          
        for i in range (0, 360):
	      	sun.forward(100)
	      	sun.left(180)
	      	sun.forward(100)
	      	sun.right(1)



    




def cutdraw():

    screen = Screen()

    cut.penup()

    cut.color('black')
    cut.pensize(40)
    cut.goto(-350,350)
    cut.pendown()
    cut.goto(350,350)
    cut.goto(350,-350)
    cut.goto(-350,-350)
    cut.goto(-350,350)

    penup()
    cut.speed(9)
    cut.color('white')
    cut.pensize(100)
    cut.goto(-345,345)
    cut.pendown()
    cut.goto(345,345)
    cut.goto(345,-345)
    cut.goto(-345,-345)
    cut.goto(-345,345)
    screen.exitonclick()



drawsky()
drawmountainss()
drawclouds()
drawwater()
drawsun()
cutdraw()
