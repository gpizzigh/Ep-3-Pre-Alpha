import pygame as pyg
from pygame.locals import *
import time
import math
import os
from classes import *
#-------------------Class-------------------------------------------------------


#-------------------------------------------------------------------------------
pyg.init()


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"resourses\imagens")

screen = pyg.display.set_mode((500,500))

#background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"track final.png"))
faixa = pyg.image.load(os.path.join(img_folder,"faixa.png"))
carro = pyg.image.load(os.path.join(img_folder,"carro vermelho Demo.png"))#.convert_alpha()
#carro_mask = pyg.mask.from_surface((os.path.join(img_folder,"carro vermelho mask.png")))
#carro_mask = carro_mask(15,24)
#pista_mask = pista_mask(1383,1448.4)
#bg_mask = bg_mask(1500,1500)
#pista_mask = pyg.image.load(os.path.join(img_folder,"track final pista mask black.png")).convert_alpha()
bg_mask = pyg.image.load(os.path.join(img_folder,"track final mask white.png"))
#carro_mask = pyg.image.load(os.path.join(img_folder,"carro vermelho mask.png"))
pistax= 0
pistay= -1000
xpos = 275
ypos = 350
keys=[False,False,False,False]
direction = 0
forward = 0
WHITE = (255, 255, 255, 255)
RED = (255,0,0)
black =(0,0,0)
BLACK = (255, 255, 255, 0)
#BLACK =()
FPS = 120
YEllOW = (246,255,0,255)
LAPS=0
smallfont = pyg.font.SysFont("comicsansms",20)
def score(score):

	text = smallfont.render("Laps: "+str(score),True, BLACK)
	#if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:
		#score += 1

	screen.blit(text, [0,0])
def tempo(Tempo):
    text1 = smallfont.render("Tempo total: "+str(timer),True,BLACK)
    text2 = smallfont.render("Tempo da volta: "+str(Tempo),True, BLACK)
    screen.blit(text1,[250,0])
    screen.blit(text2,[250,24])

clock = pyg.time.Clock()

dt = 0
TEMPO = 0
timer2 =0
y = 0

#lista de sprites:
#all_sprites_carros = pyg.sprite.Group()#sprites de carros
#all_sprites_extra = pyg.sprite.Group()#sprites da pista e BG
#adiciona ao grupo de sprites:
#all_sprites_carros.add(carro_mask)
#all_sprites_extra.add(pista_mask)
#all_sprites_extra.add(bg_mask)

running = True
while running:
<<<<<<< HEAD:teste_main.py
	pyg.display.set_caption('Random Race')
	screen.fill(0)
	clock.tick(FPS)
	timer = pyg.time.get_ticks()/1000

 	#Verifica se o carro bateu na pista.

	#print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
	#print(pistax,pistay)
	if pistax >= 270:
    	pistax = pistax -5
    	forward = 0.01
	if pistax <= -1200:
    	pistax = pistax + 5
    	forward = 0.01
	if pistay >= 350:
    	pistay= pistay - 5
    	forward = 0.01
	if pistay <= -1125:
    	pistay = pistay + 5
    	forward = 0.01

	if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
        forward -= 0.1
=======
    pyg.display.set_caption('Random Race')
    screen.fill(0)
    clock.tick(FPS)
    timer = pyg.time.get_ticks()/1000

    # Verifica se o carro bateu na pista.

#    print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
    #print(pistax,pistay)
    if pistax >= 270:
        pistax = pistax -5
        forward = 0.01

    if pistax <= -1200:
        pistax = pistax + 5
        forward = 0.01
    if pistay >= 350:
        pistay= pistay - 5
        forward = 0.01
    if pistay <= -1125:
        pistay = pistay + 5
        forward = 0.01

    if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == WHITE:
#        if forward >2:
#            forward = 2
>>>>>>> 374d414b592c37610ae939db149d5a67adb0705b:Main_Alpha.py
        if keys[2]==True:
            forward = 0
            forward = -2
		if keys[3]==True:
            forward = 0
            forward = 2


#print(bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))))
#print(faixa.get_at((int(xpos - pistax), int(ypos - pistay))))
	if faixa.get_at((int(xpos - pistax), int(ypos - pistay))) == YEllOW:

		if LAPS == 0 and TEMPO == 0:
            LAPS = 1
            TEMPO = timer - timer
            x = TEMPO
            y = timer

		elif LAPS ==1 and TEMPO>=0 and timer-y>15:
            LAPS =2
            TEMPO = timer
            y = timer
            x= TEMPO

		elif LAPS >1 and TEMPO >=0 and timer-y >15:
            LAPS += 1
            TEMPO = timer - y
            x = TEMPO
            y = timer

<<<<<<< HEAD:teste_main.py
	if keys[2]==True:
		forward-= 0.08
	if keys[3]==True and forward <= 0:
		forward+= 0.08
	if keys[0]==True:
		direction+= 2
	if keys[1]==True:
		direction-= 2
	movex=math.cos(direction/57.29)*forward
	movey=math.sin(direction/57.29)*forward
	pistax+=movex
	pistay-=movey


	carro_rot = pyg.transform.rotate(carro,direction)
=======


    if LAPS == 3:
    	print("finish")
    	pyg.quit()
    	exit(0)
    print(timer)


#     running = False
    #if bg_mask.get_at((int(xpos - pistax), int(ypos - pistay))) == NO_COLOR:
    if keys[2]==True:
        forward-= 0.08
    if keys[3]==True:
        forward+= 0.08
    if keys[0]==True:
        direction+= 2
    if keys[1]==True:
        direction-= 2
    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    pistax+=movex
    pistay-=movey


    carro_rot = pyg.transform.rotate(carro,direction)
>>>>>>> 374d414b592c37610ae939db149d5a67adb0705b:Main_Alpha.py
    #screen.blit(background,(0,0))

	screen.blit(pista, (pistax,pistay))

#    screen.blit(pista_mask, (pistax,pistay))

	screen.blit(faixa,(pistax,pistay))
	screen.blit(carro_rot, (xpos,ypos))

	score(LAPS)
	tempo(TEMPO)
	#print(timer)
	#print(timer2)
    #screen.blit(carro_mask, (xpos,ypos))
	pyg.display.flip()
	time.sleep(0.02)
	for event in pyg.event.get():
        #da update no grupo de sprites:
        # all_sprites_list.update()
    # checa se sai do jogo
		if event.type==pyg.QUIT:
            # SAida do jogo
<<<<<<< HEAD:teste_main.py
			pyg.quit()
			exit(0)

		if event.type == pyg.KEYDOWN:
			if event.key==K_LEFT:
				keys[0]=True
			elif event.key==K_RIGHT:
				keys[1]=True
			elif event.key==K_UP:
				keys[2]=True
			elif event.key==K_DOWN:
				keys[3]=True
			elif event.key == pyg.K_ESCAPE:
				pyg.quit()
				exit(0)


		if event.type == pyg.KEYUP:
			if event.key==pyg.K_LEFT:
				keys[0]=False
			elif event.key==pyg.K_RIGHT:
				keys[1]=False
			elif event.key==pyg.K_UP:
				forward -= 0.1
				keys[2]=False
			elif event.key==pyg.K_DOWN:
				keys[3]=False
=======
            pyg.quit()
            exit(0)

            

        if event.type == pyg.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
           
            elif event.key == pyg.K_ESCAPE:
                pyg.quit()
                exit(0)

        if event.type == pyg.KEYUP:
            if event.key==pyg.K_LEFT:
                keys[0]=False
            elif event.key==pyg.K_RIGHT:
                keys[1]=False
            elif event.key==pyg.K_UP:
                forward = -2
                keys[2]=False
            elif event.key==pyg.K_DOWN:
                keys[3]=False
>>>>>>> 374d414b592c37610ae939db149d5a67adb0705b:Main_Alpha.py
