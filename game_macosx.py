import turtle
import os
import math
import random
global ending
ending = "playing"
nofenm = int(input("select how many rows of enemies you want to have: ")) * 10
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
wn.tracer(0)
bp = turtle.Turtle()
bp.speed(0)
bp.color("white")
bp.penup()
bp.setposition(-300,-300)
bp.pendown()	
bp.pensize(3)
for side in range(4):
	bp.fd(600)
	bp.lt(90)
bp.hideturtle()
scr = 0
sp = turtle.Turtle()
sp.speed(0)
sp.color("white")
sp.penup()
sp.setposition(-290, 280)
scstr = "Score %s" %scr
sp.write(scstr, False, align="left", font=("Arial", 14, "normal"))
sp.hideturtle()
plr = turtle.Turtle()
plr.color("blue")
plr.shape("player.gif")
plr.penup()
plr.speed(0)
plr.setposition(0,-256)
plr.setheading(90)
plrspd = 10
enemies = []
enstx = -225
ensty = 250
ennum = 0
for i in range(nofenm):
	enemies.append(turtle.Turtle())
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = enstx + (50 * ennum)
	y = ensty
	enemy.setposition(x,y)
	ennum += 1
	if ennum == 10:
		ensty -= 50
		ennum = 0
enemyspeed = 0.10
blt = turtle.Turtle()
blt.color("yellow")
blt.shape("triangle")
blt.penup()
blt.speed(0)
blt.setheading(90)
blt.shapesize(0.5,0.5)
blt.hideturtle()
bltspd = 5
bltstt = "ready"
def fb():
	global bltstt
	if bltstt == "ready":
		os.system("afplay {}&".format(laser.wav))
		bltstt = "fire"
		x = plr.xcor()
		y = plr.ycor() + 10
		blt.setposition(x,y)
		blt.showturtle()
def move_left():
	x = plr.xcor()
	x -= plrspd
	if x < -280:
		x = - 280
	plr.setx(x)
def move_right():
	x = plr.xcor()
	x += plrspd
	if x > 280:
		x = 280
	plr.setx(x)
def ic(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fb, "space")
while True:
	wn.update()
	for enemy in enemies:
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		if enemy.xcor() > 280:
				for e in enemies:
					y = e.ycor()
					y -= 40
					e.sety(y)
				enemyspeed *= -1
		if enemy.xcor() < -280:
				for e in enemies:
					y = e.ycor()
					y -= 40
					e.sety(y)
				enemyspeed *= -1
		if ic(blt, enemy):
			os.system("afplay {}&".format(explosion.wav))
			blt.hideturtle()
			bltstt = "ready"
			blt.setposition(0, -400)
			enemy.setposition(0,10000)
			scr += 1
			scstr = "Score %s" %scr
			sp.clear()
			sp.write(scstr, False, align="left", font=("Arial", 14, "normal"))
		if ic(plr, enemy):
			os.system("afplay {}&".format(explosion.wav))
			plr.hideturtle()
			enemy.hideturtle()
			ending = "abc"
	if bltstt == "fire":
		y = blt.ycor()	
		y += bltspd
		blt.sety(y)
	if blt.ycor() > 275:
		blt.hideturtle()
		bltstt = "ready"
	if ending == "abc":
		end = input("game over, press enter to exit")
		break
	if scr == nofenm:
		end = input("You Won!!!, press enter to exit")
		break