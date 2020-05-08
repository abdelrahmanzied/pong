import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("#3498db")
player1.shapesize(stretch_wid=5,stretch_len=.5)
player1.penup()
player1.goto(-380, 0)

# Paddle B
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("#e74c3c")
player2.shapesize(stretch_wid=5,stretch_len=.5)
player2.penup()
player2.goto(370, 0)


# Score
score1 = 0
score2 = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#bdc3c7")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

# Pen
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("#3498db")
pen1.penup()
pen1.hideturtle()
pen1.goto(-120, 250)
pen1.write(f"Player 1: {score1}", align="center", font=("Courier", 24, "normal"))

pen = turtle.Turtle()
pen.speed(0)
pen.color("#27ae60")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("VS", align="center", font=("Courier", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("#e74c3c")
pen2.penup()
pen2.hideturtle()
pen2.goto(120, 250)
pen2.write(f"Player 2: {score2}", align="center", font=("Courier", 24, "normal"))


# Functions
def player1_up():
    y = player1.ycor()
    y += 30
    if y > 240:
        y = 240
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 30
    if y < -240:
        y = -240
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 30
    if y > 240:
        y = 240
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 30
    if y < -240:
        y = -240
    player2.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(player1_up, "w")
wn.onkeypress(player1_down, "s")
wn.onkeypress(player2_up, "Up")
wn.onkeypress(player2_down, "Down")


# Game Loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen1.clear()
        pen1.write(f"Player 1: {score1}", align="center", font=("Courier", 24, "normal"))

        

    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen2.clear()
        pen2.write(f"Player 2: {score2}", align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50:
        ball.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif ball.xcor() > 340 and ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
