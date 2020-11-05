import turtle

t = turtle
health = 200
initial_heading = 90
heading = initial_heading
new_heading = 90
cannon_count = 30
max_cannon_capacity = 30


def left():
    global newheading
    newheading = heading - 5


def right():
    global newheading
    newheading = heading + 5


def refresh_heading():
    global heading
    heading = newheading


def Create_screen():
    t. Screen()
    t. screensize(1000, 500)
    t. bgcolor("#3895D3")
    t. hideturtle()
    t. speed(0)
    t. pensize(5)
    t. title("Battac!")


def draw_compass():
    t.color("#404040")
    t.penup()
    t.setx(200)
    t.sety(-200)
    t.pendown()
    t.circle(75)
    t.begin_fill()
    t.color("#808080")
    t.penup()
    t.sety(-199)
    t.begin_fill()
    t.circle(74)
    t.end_fill()
    t.penup()
    t.setposition(200, -125)
    t.color("#0000ff")
    t.setheading(heading + 180)
    t.pendown()
    t.fd(70)
    t. penup()
    t.setposition(200, -125)
    t.pendown()
    t.color("red")
    t.setheading(heading)
    t.fd(70)
    t. penup()
    t. fd(10)
    t. setposition(192, -45)
    t. color("black")
    t. write("N", font=("Arial", 24, "normal"))
    t. penup()


def Draw_player():
    t. penup()
    t. setx(15)
    t. sety(25)
    t. pendown()
    t. pensize(10)
    t. color("#ffffff")
    t. setx(-15)
    t. penup()
    t. setx(20)
    t. sety(10)
    t. pendown()
    t. setx(-20)
    t. penup()
    t. setx(0)
    t. sety(32)
    t. color("#653400")
    t. pensize(7)
    t. pendown()
    t. sety(-10)
    t. setx(20)
    t. sety(-10)
    t.begin_fill()
    t. pendown()
    t. sety(-30)
    t. setx(-20)
    t. sety(-10)
    t. setx(20)
    t. end_fill()
    t. penup()
    t. setx(-20)
    t. sety(-10)
    t. color("#996600")
    t. begin_fill()
    t. pendown()
    t. setx(20)
    t. sety(-20)
    t. setx(-20)
    t. sety(-10)
    t. end_fill()
    t. penup()


def draw_health():
    t. penup()
    t. pensize(10)
    t. sety(250)
    t. color("#ff0000")
    t. setx(-100)
    t. pendown()
    t. setx(100)
    t. penup()
    t. color("#00ff00")
    t. setx(-100)
    t. pendown()
    t. setheading(0)
    t. fd(health)
    t. penup()


def draw_CannonCount():
    t. penup()
    t. goto(200, 250)
    t. color("#000000")
    t. begin_fill()
    t. pendown()
    t. circle(10)
    t. end_fill()
    t. pensize(10)
    t. goto(200, 260)
    t. setheading(45)
    t. fd(20)
    t. penup()
    t. goto(180, 210)
    t. write(cannon_count, font= ("Arial", 24, "normal"))


def press_loop():
    t. onkey(left, "A")
    t. onkey(right, "D")
    t. listen()


t. done()
