# Simple Pong in Python 3 incorporates winsound to
# play wav files on a windows machine.
# By @Mitchell_Mears
import turtle
import winsound

# wn = window
wn = turtle.Screen()
wn.title("Pong by @MitchellMears")
# background color
wn.bgcolor("black")
# dimensions
wn.setup(width=800, height=600)
# stop window from updating to speed up games, we have to manually update
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# animation speed 0 is max
paddle_a.speed(0)
# by default 20 pixel by 20 pixel
paddle_a.shape("square")
paddle_a.color("white")
# stretches width by 5x and length by 1x
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
# turn off animation/go max speed.
paddle_b.speed(0)
# by default 20 pixel by 20 pixel
paddle_b.shape("square")
paddle_b.color("white")
# multiples width by 5 and length by 1.
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# ball movement - moves 2 pixels x and y
ball.dx = .2
ball.dy = .2

# pen - writes text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))


# functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding, from turtle
wn.listen()
# moves paddle_a
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# moves paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top and bottom border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("reload.WAV", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("reload.WAV", winsound.SND_ASYNC)

    # ball goes off-screen right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # increments score
        score_a += 1
        # clears the text of pen
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # ball goes off-screen left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # paddle and ball collision
        # paddle_b collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 45 > ball.ycor() > paddle_b.ycor() - 45):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("gunshot.WAV", winsound.SND_ASYNC)

        # paddle_a collision
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 45 > ball.ycor() > paddle_a.ycor() - 45):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("gunshot.WAV", winsound.SND_ASYNC)
