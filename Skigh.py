import pygame, random
pygame.init()
#VARIABLES
done = False
speed = 1
spinCD = 0
frame = 0
nextFrame = 0
#CONSTANTS
Dir = 'D:\Program Data\OneDrive\Programs\Games\Skigh'
##TEXTURES
bg = pygame.image.load(Dir + r'\bg.jpg')
player = pygame.image.load(Dir + r'\Winged.png')
player = pygame.transform.scale(player,(204,100))
playerSpin = pygame.image.load(Dir + r'\Winged.png')
playerL = [player]
comet1 = pygame.image.load(Dir + r'\comet1.png')
comet1 = pygame.transform.scale(comet1,(100,250))
comet2 = pygame.image.load(Dir + r'\comet2.png')
comet2 = pygame.transform.scale(comet2,(100,250))
comet3 = pygame.image.load(Dir + r'\comet3.png')
comet3 = pygame.transform.scale(comet3,(100,250))
comet4 = pygame.image.load(Dir + r'\comet4.png')
comet4 = pygame.transform.scale(comet4,(100,250))
cometL = [comet1,comet2,comet3,comet4]
#CLASSES
class Comet():
    def __init__(self):
        self.spriteL = cometL
        self.frameRand = random.randint(1,4)
        self.frame = self.frameRand
        self.image = self.spriteL[self.frameRand]
        self.rect = self.image.get_rect()
        self.speed = random.randint(0,3)
    def update(self):
        self.rect.y -= speed*self.speed
class Player():
    def __init__(self):
        self.spriteL = playerL
        self.image = self.spriteL[0]
        self.rect = self.image.get_rect()
#SCREEN
size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Skigh")
icon = pygame.image.load(Dir + '\icon.png')
pygame.display.set_icon(icon)
#LOOP
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.rect.x -= 5+2*speed
        while player.rect.x < 0:
            player.rect.x += 1
    if keys[pygame.K_d]:
        player.rect.x += 5+2*speed
        while player.rect.x > 596:
            player.rect.x -= 1
    if keys[pygame.K_SPACE]:
        spin()

    pygame.display.flip()