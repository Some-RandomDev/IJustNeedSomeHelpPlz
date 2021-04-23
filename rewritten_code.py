#import random for random location
import turtle 
import random

#Idk why they exist but from the data from your code
health_float = float(200) # has to be float cant be health cuz used in class as variable
initial_heading= 90 #?
heading = initial_heading #?
new_heading = 90 #?
cannon_count = 30 #?
max_cannon_capacity = 30 #?
# Issues after test
# Ship won't move but a part that was lastly drawen does
# Looks empty no other func. if you gona add attack and stuff do them outside the class
# TO DO
# Edit it to make it visually appealling
# Make sort of camera that follows the player? or put collision soo it can't escape screen
# Edit the classes to change the drawing.
# https://github.com/sorutifokkusu
# Cya! Take Care!

#Create the window
win = turtle.Screen()
win.title("Battac!")
win.bgcolor("blue")
win.setup(width=1000,height=600)
win.tracer(0)

#the class Compass
class Compass:
    compas = turtle.Turtle()
    compas.color("red")
    compas.penup()
    compas.setx(200)
    compas.sety(-200)
    compas.pendown()
    compas.circle(75)
    compas.begin_fill()
    compas.color("#808080")
    compas.penup()
    compas.sety(-199)
    compas.begin_fill()
    compas.circle(74)
    compas.end_fill()
    compas.penup()
    compas.setposition(200, -125)
    compas.color("#0000ff")
    compas.setheading(heading + 180)
    compas.pendown()
    compas.fd(70)
    compas. penup()
    compas.setposition(200, -125)
    compas.pendown()
    compas.color("red")
    compas.setheading(heading)
    compas.fd(70)
    compas.penup()
    compas.fd(10)
    compas.setposition(192, -45)
    compas.color("black")
    compas.write("N", font=("Arial", 24, "normal"))
    compas.penup()

compas1 = Compass
compas = compas1.compas
# Use compas compas1=compas.compas all other class are the same

#Cannon
class CannonCount:
    cannon=turtle.Turtle()
    cannon. penup()
    cannon. goto(200, 250)
    cannon. color("#000000")
    cannon. begin_fill()
    cannon. pendown()
    cannon. circle(10)
    cannon. end_fill()
    cannon. pensize(10)
    cannon. goto(200, 260)
    cannon. setheading(45)
    cannon. fd(20)
    cannon. penup()
    cannon. goto(180, 210)
    cannon. write(cannon_count, font= ("Arial", 24, "normal"))
cannon1 = CannonCount
cannon1 = cannon1.cannon

#Health 
class Health:
    health= turtle.Turtle()
    health. penup()
    health. pensize(10)
    health. sety(250)
    health. color("#ff0000")
    health. setx(-100)
    health. pendown()
    health. setx(100)
    health. penup()
    health. color("#00ff00")
    health. setx(-100)
    health. pendown()
    health. setheading(0)
    health. fd(health_float)
    health. penup()
health1= Health
health = health1.health
#Player itself TO FIX= It's not a whole object but parts, you have to look up how to combine them
class Player:
    player = turtle.Turtle()
    player. penup()
    player. setx(15)
    player. sety(25)
    player. pendown()
    player. pensize(10)
    player. color("#ffffff")
    player. setx(-15)
    player. penup()
    player. setx(20)
    player. sety(10)
    player. pendown()
    player. setx(-20)
    player. penup()
    player. setx(0)
    player. sety(32)
    player. color("#653400")
    player. pensize(7)
    player. pendown()
    player. sety(-10)
    player. setx(20)
    player. sety(-10)
    player.begin_fill()
    player. pendown()
    player. sety(-30)
    player. setx(-20)
    player. sety(-10)
    player. setx(20)
    player. end_fill()
    player. penup()
    player. setx(-20)
    player. sety(-10)
    player. color("#996600")
    player. begin_fill()
    player. pendown()
    player. setx(20)
    player. sety(-20)
    player. setx(-20)
    player. sety(-10)
    player. end_fill()
    player. penup()
    player.speed(0)
    player.direction= "stop"

# calling the player
player1 = Player
# to make it shorter
player = player1.player


#Movement
def move():
    if player.direction == "left":
        x=player.xcor()
        player.setx(x-0.1)
                    #Change the ints for speed change
        
    if player.direction == "right" :
        x=player.xcor()
        player.setx(x+0.1)
    
    if player.direction == "up" :
        y=player.ycor()
        player.sety(y+0.1)
    
    if player.direction == "down" :
        y=player.ycor()
        player.sety(y-0.1)


#keypress func
def go_up():
    if player.direction != "up":
        player.direction = "up"
def go_down():
    if player.direction != "down":
        player.direction = "down"
def go_left():
    if player.direction != "left":
        player.direction = "left"

def go_right():
    if player.direction != "right":
        player.direction = "right"

#Get the keys and call func
win.listen()
win.onkey(go_right,"d")
win.onkey(go_left,"a")
win.onkey(go_up,"w")
win.onkey(go_down,"s")


#This is your game loop
while True:
    win.update()
    move()






