import turtle, winsound

wind = turtle.Screen()
wind.title('Pong by Amundeep Singh Dhaliwal')
wind.bgcolor('black')
wind.setup(width = 800, height=600)
wind.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5, stretch_len =1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5, stretch_len =1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2 # ball change in x direction
ball.dy = 0.2 # ball change in y direction


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0  Player B: 0 ', align ='center',font=('Courier',24,'normal'))

# move paddle a
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

# Keyboard binding
wind.listen()
wind.onkeypress(paddle_a_up, 'w')
wind.onkeypress(paddle_a_down, 's')
wind.onkeypress(paddle_b_up, 'Up')
wind.onkeypress(paddle_b_down, 'Down')

# main game loop
while True:
	wind.update()

	# move the ball
	ball.setx(ball.xcor() +ball.dx)
	ball.sety(ball.ycor() +ball.dy)
    # border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound(r"C:\Users\Amundeep\Music\Program sounds\4359__noisecollector__pongblipf4.wav", winsound.SND_ASYNC)
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound(r"C:\Users\Amundeep\Music\Program sounds\4359__noisecollector__pongblipf4.wav", winsound.SND_ASYNC)
	if ball.xcor() > 390:
		score_a += 1
		ball.goto(0,0)
		ball.dx *= -1
		pen.clear()
		pen.write(f'Player A: {score_a}  Player B: {score_b} ', align ='center',font=('Courier',24,'normal'))
	if ball.xcor() < -390:
		score_b+= 1
		ball.goto(0,0)
		ball.dx *= -1
		pen.clear()
		pen.write(f'Player A: {score_a}  Player B: {score_b} ', align ='center',font=('Courier',24,'normal'))
	
	# player checking
	if paddle_b.ycor() < -240:
		 paddle_b.sety(-240) 
	if paddle_b.ycor() > 250:
		 paddle_b.sety(250) 
	if paddle_a.ycor() < -240:
		 paddle_a.sety(-240) 
	if paddle_a.ycor() > 250:
		 paddle_a.sety(250) 	
	
	# Paddle and ball collisions
	if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() +40 and ball.ycor() >paddle_b.ycor()-40:
		ball.setx(340)
		winsound.PlaySound(r"C:\Users\Amundeep\Music\Program sounds\4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)
		ball.dx *= -1

	if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() +40 and ball.ycor() >paddle_a.ycor()-40:
		ball.setx(-340)
		winsound.PlaySound(r"C:\Users\Amundeep\Music\Program sounds\4388__noisecollector__pongblipe5.wav", winsound.SND_ASYNC)
		ball.dx *= -1

	
	