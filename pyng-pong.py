"""
Simple pong clone

To Do:
	-randomize ball speed at match start
	-Count down/pause for start of match or new point
	-Winner Screen/Procedure
	-Reset board procedure
"""

import pygame #used for drawing and window management
import sys #used for window management

#theme settings
maincolor = (255,255,255)
backgroundcolor = (0,0,0)




pygame.init() #start pygame
window = pygame.display.set_mode((1200,800))
pygame.draw.rect(window,backgroundcolor,((0,0),(1200,800)),0)
#Set up the game
def drawcenterline():
	pygame.draw.line(window,maincolor,(600,0),(600,800),4) #draw white center line 
															   #change to dashed??

def winner(playernum):
	pass
	#Draw winning playernum in middle of screen (large)
	#Pause Game
	#call reset of board/scores/ball
def drawnum (num,size,posx,posy):
	if num == 0:
		pygame.draw.rect(window,maincolor,((posx,posy),(size,int(size*1.5))),8)
	elif num == 1:
		pygame.draw.line(window,maincolor,(posx+int(size/2),posy),(posx+int(size/2),posy+int(size*1.5)),8)
		pygame.draw.line(window,maincolor,(posx+int(size/2)+4,posy),(posx+int(size/4),posy+int(size/4)),8)
		pygame.draw.line(window,maincolor,(posx+int(size/5),posy+int(size*1.5)),(posx+int(4*size/5),posy+int(size*1.5)),8)
	elif num == 2:
		pygame.draw.line(window,maincolor,(posx,posy),(posx+size,posy),8)
		pygame.draw.line(window,maincolor,(posx+size,posy),(posx+size,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*0.75)),(posx+size+2,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*0.75)),(posx,posy+int(size*1.5)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*1.5)),(posx+size+2,posy+int(size*1.5)),8)
	elif num == 3:
		pygame.draw.line(window,maincolor,(posx,posy),(posx+size,posy),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*0.75)),(posx+size,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*1.5)),(posx+size,posy+int(size*1.5)),8)
		pygame.draw.line(window,maincolor,(posx+size,posy),(posx+size,posy+int(size*1.5)),8)
	elif num == 4:
		pygame.draw.line(window,maincolor,(posx,posy),(posx,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx+int(2*size/3),posy),(posx+int(2*size/3),posy+int(size*1.5)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*0.75)),(posx+size,posy+int(size*0.75)),8)
	elif num == 5:
		pygame.draw.line(window,maincolor,(posx,posy),(posx+size,posy),8)#top
		pygame.draw.line(window,maincolor,(posx+size,posy+int(size*0.75)),(posx+size,posy+int(size*1.5)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*0.75)),(posx+size+2,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx,posy),(posx,posy+int(size*0.75)),8)
		pygame.draw.line(window,maincolor,(posx,posy+int(size*1.5)),(posx+size+2,posy+int(size*1.5)),8)
def erasenum (size,posx,posy):
	pygame.draw.rect(window,backgroundcolor,((posx,posy),(size,int(size*1.5))),0)
def drawscore():
	global p1score
	global p2score
	drawnum(p1score,75,300,80)
	drawnum(p2score,75,825,80)
	#draw the score
#procedure wrappers for drawing
def drawplayer(playernum,y):
	x=(playernum-1)*1160 + 20
	pygame.draw.line(window,maincolor,(x,y-50),(x,y+50),5)#draw paddle
def eraseplayer(playernum,y):
	x=(playernum-1)*1160 + 20
	pygame.draw.line(window,backgroundcolor,(x,y-50),(x,y+50),5)#draw paddle
def eraseboard():
	global ballx
	global bally
	pygame.draw.rect(window,backgroundcolor,((ballx-5,bally-5),(10,10)),0)#erase ball
	eraseplayer(1,y1)
	eraseplayer(2,y2)
def drawboard():
	global ballx
	global bally
	pygame.draw.rect(window,maincolor,((int(ballx)-5,int(bally)-5),(10,10)),0)#draw ball
	drawplayer(1,y1)
	drawplayer(2,y2)
	drawscore()
	drawcenterline()
def checkboard():
	global ballvy
	global bally
	global ballx
	global ballvx
	global p2score
	global p1score
	#scoring
	if ballvx < 0 and ballx <= 20:
		#if paddle is not within y range:
		if bally <= y1+50 and bally >= y1-50:
			#bounce ball, increase speed
			ballvx *= -1.25
			ballx = 20 #correct ball going past paddle
		else:
			p2score += 1 #player2 scores
			
			erasenum(96,815,75)
			if p2score > 4:
				print "Player 2 Wins!"
				#winner procedure
			#reset ball position			
			ballx = 600
			bally = 400
			ballvx = -1.3 #randomize~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
			ballvy = 2.0
	elif ballvx > 0 and ballx >= 1180:
		#if paddle is not within y range:
		if bally <= y2+50 and bally >= y2-50:
			#bounce ball, increase speed
			ballvx *= -1.25
			ballx = 1180 #correct ball going past paddle
		else:
			p1score += 1 #player1 scores
			erasenum(96,290,75)
			if p1score > 4:
				print "Player 1 Wins!"
				#winner procedure
			#reset ball position			
			ballx = 600
			bally = 400
			ballvx = 1.3 #randomize~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
			ballvy = 2.0
	#hit sides
	if bally >= 800 or bally <= 0: 
		ballvy *= -1 


def checkplayers():
	global y1
	global y2
	if y1 < 50:
		y1 = 50
	elif y1 > 750: 
		y1 = 750
	if y2 < 50:
		y2 = 50
	elif y2 > 750:
		y2 = 750
def moveball():
	global ballx
	global bally
	ballx += ballvx
	bally += ballvy
#game variables
y2      = 400 #start players in middle
y1      = 400
ballx   = 600 #start ball in middle
bally   = 400
ballvx  = -1.3 #randomize
ballvy  = 2.0 #randomize
p1score = 0 #player scores
p2score = 0

upheld = False #used for detecting keyboard holds
downheld = False

while True: #main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif event.type == pygame.KEYDOWN: #Change it to check for holding
			if event.key == pygame.K_UP: #Up arrow
				upheld = True
				y1 += -10
			elif event.key == pygame.K_DOWN: #down arrow
				downheld = True
				y1 += 10
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				upheld = False
			elif event.key == pygame.K_DOWN:
				downheld = False
	p2pos = pygame.mouse.get_pos()
	y2 = p2pos [1] #p2pos = tuple (x,y)
	if upheld:
		y1 += -10
	elif downheld:
		y1 += 10
	moveball()
	checkplayers()
	checkboard()
	drawboard()
	pygame.display.flip()
	pygame.time.wait(10)
	eraseboard()