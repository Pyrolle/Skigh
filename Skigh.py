import pygame, random
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
#VARIABLES
done = False
speed = 2
cFrameCD = 0
pFrameCD = 0
nextFrame = 0
bgPos = 0
bgPos2 = -1000

#CONSTANTS
Dir = 'D:\Program Data\OneDrive\Programs\Games\Skigh'
SIZE = 9001
while SIZE > 800:
    SIZE = int(input('What size?    (max and recomended = 800)'))
sizeMultiplier = SIZE / 800
BG_SCROLL = 7
print(sizeMultiplier)
##TEXTURES
bg = pygame.image.load(Dir + r'\bg.jpg')
playerWinged1 = pygame.image.load(Dir + r'\wing\wing (1).png')
playerWinged2 = pygame.image.load(Dir + r'\wing\wing (2).png')
playerWinged3 = playerWinged1
playerWinged4 = pygame.image.load(Dir + r'\wing\wing (4).png')
playerWinged5 = pygame.image.load(Dir + r'\wing\wing (5).png')
playerWinged6 = pygame.image.load(Dir + r'\wing\wing (6).png')
playerWinged7 = pygame.image.load(Dir + r'\wing\wing (7).png')
playerWinged8 = playerWinged6
playerWinged9 = playerWinged5
playerWinged10 = playerWinged4

playerL = [pygame.transform.scale(playerWinged1,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged2,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged3,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged4,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged5,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged6,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged7,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged8,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged9,(int(223*sizeMultiplier),int(150*sizeMultiplier))),
           pygame.transform.scale(playerWinged10,(int(223*sizeMultiplier),int(150*sizeMultiplier)))]

cometS1 = pygame.image.load(Dir + r'\comet\comet1.png')
cometS2 = pygame.image.load(Dir + r'\comet\comet2.png')
cometS3 = pygame.image.load(Dir + r'\comet\comet3.png')
cometS4 = pygame.image.load(Dir + r'\comet\comet4.png')
#CLASSES
class Comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteL = [pygame.transform.scale(cometS1,(int(75*sizeMultiplier),int(188*sizeMultiplier))),
                        pygame.transform.scale(cometS2,(int(75*sizeMultiplier),int(188*sizeMultiplier))),
                        pygame.transform.scale(cometS3,(int(75*sizeMultiplier),int(188*sizeMultiplier))),
                        pygame.transform.scale(cometS4,(int(75*sizeMultiplier),int(188*sizeMultiplier)))]
        self.frameRand = random.randint(1,4)
        self.frame = self.frameRand
        self.image = self.spriteL[self.frameRand-1]
        self.rect = self.image.get_rect()
        self.speed = random.randint(2,3)
        self.FrameCD = 100
        self.boomCD = 0
    def update(self):
        self.rect.y += 2*speed*self.speed*sizeMultiplier
        if self.rect.y > 800:
            self.rect.y = -(random.randint(100,1000))
            self.rect.x = random.randint(0,SIZE - (SIZE/5))
            self.speed = random.randint(2,4)
        if self.FrameCD < pygame.time.get_ticks():
            self.frame += 1
            if self.frame > 4:
                self.frame = 1
            self.image = self.spriteL[self.frame-1]
            self.FrameCD = pygame.time.get_ticks() + 100
cometsList = pygame.sprite.Group()

comet1 = Comet()
comet1.rect.y = -random.randrange(1000, 10000)
comet1.rect.x = random.randint(0,SIZE - (SIZE/5))
cometsList.add(comet1)

comet2 = Comet()
comet2.rect.y = -random.randrange(10000, 20000)
comet2.rect.x = random.randint(0,SIZE - (SIZE/5))
cometsList.add(comet2)

comet3 = Comet()
comet3.rect.y = -random.randrange(50000, 100000)
comet3.rect.x = random.randint(0,SIZE - (SIZE/5))
cometsList.add(comet3)

comet = Comet()
comet.rect.y = -2000
comet.rect.x = random.randint(0,SIZE - (SIZE/5))
cometsList.add(comet)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteL = playerL
        self.image = self.spriteL[0]
        self.rect = self.image.get_rect()
        self.frame = 1
    def update(self):
        global pFrameCD
        if pFrameCD < pygame.time.get_ticks():
            self.frame += 1
            if self.frame > 10:
                self.frame -= 10
            self.image = self.spriteL[self.frame-1]
            pFrameCD = pygame.time.get_ticks() + 100
PlayerList = pygame.sprite.Group()
player = Player()
player.rect.y = SIZE - (SIZE/5)
PlayerList.add(player)
#FUNCTIONS


#SCREEN
size = [SIZE, SIZE]
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
        player.rect.x -= 8*sizeMultiplier*speed
        while player.rect.x < 0:
            player.rect.x += 1
    if keys[pygame.K_d]:
        player.rect.x += 8*sizeMultiplier*speed
        while player.rect.x > SIZE - 233*sizeMultiplier:
            player.rect.x -= 1
    if pygame.sprite.spritecollideany(player, cometsList) != None:
        print("game over")
        done = True

    screen.blit(bg,(-100+ player.rect.x/6.5,bgPos2))
    screen.blit(bg,(-100+ player.rect.x/6.5,bgPos))
    bgPos += BG_SCROLL
    bgPos2 += BG_SCROLL
    if bgPos > 900:
        bgPos = -1000
    if bgPos2 > 900:
        bgPos2 = -1000

    comet.update()
    comet1.update()
    comet2.update()
    comet3.update()
    player.update()
    cometsList.draw(screen)
    PlayerList.draw(screen)
    pygame.display.flip()