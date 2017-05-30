import math
import pygame as pyg
import os
#--------------------------------------------------Funçoes------------------------------------------------------------------------------------------
class carro:
    def __init__(self,carro,alt,vel):
        self.vel = vel
        self.carro = carro
        self.pos = carro.move(0, alt)
    def move(self):
        self.pos = self.pos.move(0, self.vel)
        if self.pos.right > 400:
            self.pos.left = 0
        elif self.pos.left > 400:
            self.pos.right = 0
        elif self.pos.up > 400:
            self.pos.down = 0
        elif self.pos.down > 400:
            self.pos.up = 0

#--------------------------------------------------Programa Principal-------------------------------------------------------------------------------
pyg.init()

white = (255,255,255)


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"arte_grafica")


#comprimeto Fundo--------------------
Display_largura = 400
Display_altura = 400
#----------------------------------
#comprimento Pista-------------
Display_pista_larg = 200
Display_pista_alt = 200
#----------------------------
#comprimeto Faixa ---------------
Display_faixa_larg =7
Display_faixa_alt = 9
screen = pyg.display.set_mode((Display_largura,Display_altura))
pyg.display.set_caption("Random Race")

background = pyg.image.load(os.path.join(img_folder,"FundoDemo.png")).convert()
pista = pyg.image.load(os.path.join(img_folder,"pista Demo.png")).convert_alpha()
faixa = pyg.image.load(os.path.join(img_folder,"faixa Demo.png")).convert_alpha()
carro  = pyg.image.load(os.path.join(img_folder,"carro vermelho Demo final.png")).convert_alpha()

clock = pyg.time.Clock()
keys = [False,False,False,False] #Efeito SUAVE
trcx = 0 # zoom da pista
trcy = -1000 # zoom da pista
lead_x = 275
lead_y = 350
#lead_x_change = 0
#lead_y_change = 0
global direction
direction = "right"
d_angle = 2
angle = 0
d_vel = 0.2
vel = 0
out = False
#global direction
if direction == "right":
    head = pyg.transform.rotate(carro,90)
if direction == "left":
    head = pyg.transform.rotate(carro,-90)
if direction == "up":
    head = pyg.transform.rotate(carro,0)
if direction == "down":
    head = pyg.transform.rotate(carro,180)

#-----------------------------Game LOOP------------------------------------------------------------
while out != True:

    if keys[0]==True: #Left
        angle -= d_angle
    if keys[1]==True: #Right
        angle += d_angle
    if keys[2] == True: #Up
        vel += d_vel
    if keys[3] == True and vel >=0: # Down
        vel -= d_vel

    lead_x_change = vel * math.sin(angle/57.29)
    lead_y_change = vel * math.cos(angle/57.29)
    trcx += lead_x_change
    trcy -= lead_y_change
    lead_x += lead_x_change
    lead_y -= lead_y_change



    for event in pyg.event.get():
        #global direction
        if event.type == pyg.QUIT:
            out = True
        if event.type == pyg.KEYDOWN:
#NAO MAEXER MAIS NESSE CODIGO---------------------------------------------------------------------
                if event.key == pyg.K_LEFT:
                    direction = "left"
                    keys[0] = True
                    #angle -= d_angle
                    #print("Left: {0}\n".format(angle))
                elif event.key == pyg.K_RIGHT:
                    direction = "right"
                    keys[1] = True
                    #angle += d_angle
                    #print("Right: {0}\n".format(angle))

                elif event.key == pyg.K_UP:
                    direction = "up"
                    keys[2] = True
                    #vel -= d_vel
                    #print("Up: {0}\n".format(vel))
                elif event.key == pyg.K_DOWN:
                    direction = "down"
                    keys[3] = True
                    #vel += d_vel
                    #print("Down: {0}\n".format(vel))
        if event.type == pyg.KEYUP:

            if event.key == pyg.K_LEFT:
                direction = "left"
                keys[0] = False
            elif event.key == pyg.K_RIGHT:
                direction = "right"
                keys[1] = False
            elif event.key == pyg.K_UP:
                direction = "up"
                keys[2] = False
            elif event.key == pyg.K_DOWN:
                direction = "down"
                keys[3] = False
#NAO MEXER MAIS NESSTE CODIGO --------------------------------------------------------------------------------
    #lead_x -= vel * math.sin(math.pi * angle / 180.0)
    #lead_y += vel * math.cos(math.pi * angle / 180.0)
    if lead_x >= Display_largura or lead_x < 0 or lead_y >= Display_altura or lead_y < 0:
        #Rebounce(lead_x,lead_y)
        pass
    if lead_x >= 400 or lead_x < 0 or lead_y >= 400 or lead_y < 0:
        lead_x += 5
        lead_y += 5
        #out = True
    rot_carro = pyg.transform.rotate(carro,angle)
    screen.blit(background, (0,0,trcx,trcy))
    screen.blit(pista, (trcx,trcy))
    screen.blit(faixa,(0,0,Display_faixa_alt,Display_faixa_larg))
    #screen.blit(pyg.transform.rotate(carro,angle),[lead_x, lead_y, 0, 0])
    screen.blit(rot_carro, (lead_x, lead_y))
    pyg.display.update()
    clock.tick(27)

pyg.quit()
