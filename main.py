
#slither game final version
#John M. Valadez-Rodriguez
#Done early enough
import pygame
import random
import math
pygame.init()
pygame.display.set_caption("slither")
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
doExit = False
#P variables
xPos = 150
yPos = 150
Vx = 1
Vy = 1
#P2 variables
xPos2 = 300
yPos2 = 300

#start class pellet
class pellet:
    def __init__(self, xpos, ypos, red, green, blue, radius):
        self.xpos = xpos
        self.ypos = ypos
        self.red = red
        self.green = green
        self.blue = blue
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen, (self.red, self.green, self.blue), (self.xpos, self.ypos), self.radius)
    def collide(self,x,y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) < self.radius + 6:
            self.xpos = random.randrange(0,400)
            self.ypos = random.randrange(0,400)
            self.red = random.randrange(0,255)
            self.blue = random.randrange(0,255)
            self.green = random.randrange(0,255)
            self.radius = random.randrange(0,30)
            return True

pelletBag = list()#creates a list data strructure
tail = list()
for i in range (100):
    pelletBag.append(pellet(random.randrange(0,370),random.randrange(0,370),random.randrange(0,255),random.randrange(0,255),random.randrange(0,255),random.randrange(0,30)))   
#end class pellet
    #class tailsag
class TailSag:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    def update(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen,(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (self.xpos, self.ypos), 12) 
    def collide(self,x,y):
        if math.sqrt((x-self.xpos)*(x-self.xpos)+(y-self.ypos)*(y-self.ypos)) <6:
            return True
tail2 = list()
               
oldX=200
oldY=200
oldX2=200
oldY2=200
counter = 0
#gameloop
while not doExit:
#event/input
    
    #clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
        else:
            doExit = False
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        if mousePos[0]>xPos:
            Vx = 1
        else:
            Vx = -1
        if mousePos[1]>yPos:
            Vy = 1
        else:
            Vy = -1
    #player 2 keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        xPos2-=1
    if keys[pygame.K_RIGHT]:
        xPos2+=1
    if keys[pygame.K_UP]:
        yPos2-=1
    if keys [pygame.K_DOWN]:
        yPos2+=1

            
    counter += 1 #update counter
    if counter == 20: #create a delay so the segments follow behind
        counter = 0 #reset counter every 20 ticks
        oldX = xPos #hold onto old players position from 20 ticks ago
        oldY = yPos
        oldX2 = xPos2 #hold onto old players position from 20 ticks ago
        oldY2 = yPos2
        if (len(tail)>2): # don't push numbers if they are no nodes yet
            for i in range(len(tail)):#loop for each slot in list
            #start in LAST position, push the *second to last* into it, repeat till at beginning
                tail[len(tail)-i-1].xpos = tail[len(tail)-i-2].xpos
                tail[len(tail)-i-1].ypos = tail[len(tail)-i-2].ypos
        if (len(tail2)>2): # don't push numbers if they are no nodes yet
            for i in range(len(tail2)):#loop for each slot in list
            #start in LAST position, push the *second to last* into it, repeat till at beginning
                tail2[len(tail2)-i-1].xpos = tail2[len(tail2)-i-2].xpos
                tail2[len(tail2)-i-1].ypos = tail2[len(tail2)-i-2].ypos
        if(len(tail)>0): #If you have at least one segment; push old head position into that
            tail[0].update(oldX,oldY) #push head position into first position of list
        if(len(tail2)>0): #If you have at least one segment; push old head position into that
            tail2[0].update(oldX2,oldY2) #push head position into first position of list
    
    print("p1 is mouse motion, player 2 is arrow keys. Touch your enemies tail to die.")

#physics

#check for p1 collision with p2 tail
    for i in range(len(tail2)):
        if tail2[i].collide(xPos, yPos) ==True:
            print("p1 hits p2's tail and loses!")
            doExit = True
#check for p2 collision with p1's tail
    for i in range(len(tail)):
        if tail[i].collide(xPos2, yPos2) ==True:
            print("p2 hits p1, p2 loses!")
            doExit = True        
#update circle position
    xPos += Vx
    yPos += Vy

#render to screen
    screen.fill((255,255,255))
    for i in range (10):
        if pelletBag[i].collide(xPos, yPos) == True:
           tail.append(TailSag(oldX,oldY))
        if pelletBag[i].collide(xPos2, yPos2) == True:
           tail2.append(TailSag(oldX2,oldY2))   
    for i in range(len(tail)):
        tail[i].draw()

    for i in range(len(tail2)):
        tail2[i].draw()

    for i in range (10):
        pelletBag[i].draw()
    pygame.draw.circle(screen, (200,0,200), (xPos, yPos),12)
    #p2 snek draw
    pygame.draw.circle(screen, (200,0,0), (xPos2, yPos2),12)

    pygame.display.flip()
#endgameloop
pygame.quit()#this is the end of my code to fully inspect it I reccommend moving your mouse around the screen 
