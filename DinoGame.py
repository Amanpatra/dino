import pygame
import random

pygame.init()

run= True
run2= True
vel=10
isJump=False
jump=9
clld=False

black=(0,0,0)
white=(250,250,250)
red=(255,0,0)
    
height=350
width=900
x=100
y=200
score=0
    
screen=pygame.display.set_mode((width,height))
d=[]
for i in range(5):
    new=pygame.image.load('D:\\Python programs\\Dinoimg\\d00{}.png'.format(i))
    d.append(new)

c=[]
for i in range(4):
    new=pygame.image.load('D:\\Python programs\\Dinoimg\\tile00{}.png'.format(i))
    c.append(new)

bg=pygame.image.load('D:\\Python programs\\Dinoimg\\front.png')
Font=pygame.font.SysFont('times new roman',20,True,True)
Font2=pygame.font.SysFont('Ariel',60,False,True)

class dino:
    def __init__(self):
        self.walkcount=1
    def change(self):
        self.walkcount+=1
        if self.walkcount==9:
            self.walkcount=3
    def disp(self):
        dino.change(self)
        if clld:
            screen.blit(d[4],(x,y))
            global run2
            run2=False
        else:
            if isJump:
                screen.blit(d[0],(x,y))
            else:
                screen.blit(d[self.walkcount//3],(x,y))       
Dobj=dino()

class obs:
    def __init__(self):
        self.xpos=[900,1700,1300]
        self.y1=200
        self.x1=random.choice(self.xpos)
        self.s=random.randint(0,3)
        self.check=False
    def change(self):
        self.x1-=vel
        if self.x1<-100:
            self.x1=random.choice(self.xpos)
    def display(self):
        screen.blit(c[self.s],(self.x1,self.y1))
    def checkcollide(self):
        global clld
        if x+84>=self.x1+2 and x+84<self.x1+12 and y+26>=self.y1+14:
            clld=True
        elif x+44>=self.x1+2 and x+44<=self.x1+12 and y+90>=self.y1+14:
            clld=True
        elif x+44>=self.x1+18 and x+44<=self.x1+32 and y+90>=self.y1+2:
            clld=True
        elif x+52>=self.x1+18 and x+52<=self.x1+32 and y+90>=self.y1+2:
            clld=True
        elif x+32>=self.x1+18 and x+32<=self.x1+32 and y+90>=self.y1+2:
            clld=True
        elif x+24>=self.x1+18 and x+24<=self.x1+32 and y+90>=self.y1+2:
            clld=True
        elif x+24>=self.x1+38 and x+24<=self.x1+48 and y+90>=self.y1+24:
            clld=True
        elif x+4>=self.x1+18 and x+4<=self.x1+32 and y+58>=self.y1+2:
            clld=True
        elif x+4>=self.x1+38 and x+4<=self.x1+48 and y+58>=self.y1+24:
            clld=True        
    def call(self):
        obs.change(self)
        obs.checkcollide(self)
        obs.display(self)
    
ob1=obs()
ob2=obs()
ob3=obs()

while run:    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    k=pygame.key.get_pressed()
    if k[pygame.K_SPACE]:
        run=False
    screen.blit(bg,(0,0))
    pygame.display.update()

while run2:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.time.delay(40)
    screen.fill(white)
    
    Dobj.disp()    
    ob1.call()
    ob2.call()
    ob3.call()
    
    keys=pygame.key.get_pressed()
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump=True
    
    else:
        if jump>=-9:
            neg=-1
            if jump>0:
                neg=1
            y=y-(jump*jump*0.5*neg)
            jump-=1
        else:
            jump=9
            isJump=False
    
    pygame.draw.rect(screen,(black),(0,296,900,1))
    
    score+=1
    text=Font.render("Score " + str(score),True,black)
    screen.blit(text,(800,2))
    if score%1000==0:
        vel+=1
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            
    text=Font2.render("Game Over",True,red)
    screen.blit(text,(300,150))
    pygame.display.update()