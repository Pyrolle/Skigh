import pygame, random
pygame.init()
#VARIABLES
done = False
speed = 1
spinCD = 0
cFrameCD = 0
pFrameCD = 0
nextFrame = 0
spined = False
#CONSTANTS
Dir = 'D:\Program Data\OneDrive\Programs\Games\Skigh'
##TEXTURES
bg = pygame.image.load(Dir + r'\bg.jpg')
playerWinged1 = pygame.image.load(Dir + r'\wing (1).png')
playerWinged2 = pygame.image.load(Dir + r'\wing (2).png')
playerWinged3 = pygame.image.load(Dir + r'\wing (3).png')
playerWinged4 = pygame.image.load(Dir + r'\wing (4).png')
playerWinged5 = pygame.image.load(Dir + r'\wing (5).png')
playerWinged6 = pygame.image.load(Dir + r'\wing (6).png')
playerWinged7 = pygame.image.load(Dir + r'\wing (7).png')
playerWinged8 = pygame.image.load(Dir + r'\wing (8).png')
playerWinged9 = pygame.image.load(Dir + r'\wing (9).png')
playerWinged10 = pygame.image.load(Dir + r'\wing (10).png')
playerSpin = pygame.image.load(Dir + r'\Spined.png')
playerSpin = pygame.transform.scale(playerSpin,(68,100))

playerL = [pygame.transform.scale(playerWinged1,(223,150)),pygame.transform.scale(playerWinged2,(223,150)),pygame.transform.scale(playerWinged3,(223,150)),pygame.transform.scale(playerWinged4,(223,150)),pygame.transform.scale(playerWinged5,(223,150)),pygame.transform.scale(playerWinged6,(223,150)),pygame.transform.scale(playerWinged7,(223,150)),pygame.transform.scale(playerWinged8,(223,150)),pygame.transform.scale(playerWinged9,(223,150)),pygame.transform.scale(playerWinged10,(223,150))]

cometS1 = pygame.image.load(Dir + r'\comet1.png')
cometS2 = pygame.image.load(Dir + r'\comet2.png')
cometS3 = pygame.image.load(Dir + r'\comet3.png')
cometS4 = pygame.image.load(Dir + r'\comet4.png')
#CLASSES
class Comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteL = [pygame.transform.scale(cometS1,(100,250)),pygame.transform.scale(cometS2,(100,250)),pygame.transform.scale(cometS3,(100,250)),pygame.transform.scale(cometS4,(100,250))]
        self.frameRand = random.randint(1,4)
        self.frame = self.frameRand
        self.image = self.spriteL[self.frameRand-1]
        self.rect = self.image.get_rect()
        self.speed = random.randint(2,3)
        self.FrameCD = 100

    def update(self):
        self.rect.y += 2*speed*self.speed
        if self.rect.y > 800:
            self.rect.y = -(random.randint(100,1000))
            self.rect.x = random.randint(0,700)
            self.speed = random.randint(2,4)
        if self.FrameCD < pygame.time.get_ticks():
            self.frame += 1
            if self.frame > 4:
                self.frame -= 4
                print(self, 'changed')
            self.image = self.spriteL[self.frame-1]
            self.FrameCD = pygame.time.get_ticks() + 100
cometsList = pygame.sprite.Group()

comet1 = Comet()
comet1.rect.y = -random.randrange(1000, 10000)
comet1.rect.x = random.randint(0,700)
cometsList.add(comet1)

comet2 = Comet()
comet2.rect.y = -random.randrange(1000, 10000)
comet2.rect.x = random.randint(0,700)
cometsList.add(comet2)

comet3 = Comet()
comet3.rect.y = -random.randrange(1000, 10000)
comet3.rect.x = random.randint(0,700)
cometsList.add(comet3)

comet = Comet()
comet.rect.y = -500
comet.rect.x = random.randint(0,700)
cometsList.add(comet)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spriteL = playerL
        self.image = self.spriteL[0]
        self.rect = self.image.get_rect()
        self.frame = 1
    def update(self):
        global pFrameCD, spined
        if pFrameCD < pygame.time.get_ticks():
            self.frame += 1
            if self.frame > 10:
                self.frame -= 10
            if spined == False:
                self.image = self.spriteL[self.frame-1]
            pFrameCD = pygame.time.get_ticks() + 100
PlayerList = pygame.sprite.Group()
player = Player()
player.rect.y = 650
PlayerList.add(player)
#FUNCTIONS
def spin():
    global speed, spinCD, spined
    player.image = playerSpin
    x = player.rect.x
    player.rect = player.image.get_rect()
    player.rect.x = x+68
    player.rect.y = 650
    speed *= 2
    spinCD = pygame.time.get_ticks()+ 1000
    spined = True
def unspin():
    global speed, spinCD, spined
    player.image = player.spriteL[0]
    x = player.rect.x
    player.rect = player.image.get_rect()
    player.rect.x = x-68
    player.rect.y = 650
    speed /= 2
    spined = False

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
        player.rect.x -= 8
        while player.rect.x < 0:
            player.rect.x += 1
    if keys[pygame.K_d]:
        player.rect.x += 8
        while player.rect.x > 596:
            player.rect.x -= 1
    if keys[pygame.K_SPACE] and spinCD < pygame.time.get_ticks():
        spin()
    if spinCD -500 < pygame.time.get_ticks() and spined == True:
        unspin()
    if pygame.sprite.spritecollideany(player, cometsList) != None:
        print("game over")
        done = True

    screen.blit(bg,(-100+ player.rect.x/6.5,-100))



    cometsList.draw(screen)
    PlayerList.draw(screen)
    comet.update()
    comet1.update()
    comet2.update()
    comet3.update()
    player.update()
    print(comet.frame)
    print(cFrameCD, pygame.time.get_ticks())
    pygame.display.flip()