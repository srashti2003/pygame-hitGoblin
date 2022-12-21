import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()
score = 0
bulletSound = pygame.mixer.Sound('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/Game_bullet.mp3')
hitSound = pygame.mixer.Sound('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/Game_hit.mp3')
bg_music = pygame.mixer.music.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/music.mp3')
pygame.mixer.music.play(-1)
walkRight = [pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R1.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R2.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R3.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R4.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R5.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R6.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R7.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R8.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R9.png')]
walkLeft = [pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L1.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L2.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L3.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L4.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L5.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L6.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L7.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L8.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L9.png')]
bg = pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/bg.jpg')
char = pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/standing.png')

class Player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+17, self.y+11, 29,52)
    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3] , (self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount+=1
        else:
            if self.left:
                win.blit(walkLeft[0],(self.x,self.y))
            else:
                win.blit(walkRight[0],(self.x,self.y))
        self.hitbox = (self.x+17, self.y+11, 29,52)
        #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
    def both_hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 50
        self.y = 380
        self.walkCount = 0
        font1 = pygame.font.SysFont('Times New Roman', 100, True)
        text = font1.render('-5',1,(225,0,0))
        win.blit(text, (250 - text.get_width()/2,250))
        pygame.display.update()
        i = 0
        while i<300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

class Projectile():
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class Enemy():
    walkRight = [pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R1E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R2E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R3E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R4E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R5E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R6E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R7E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R8E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R9E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R10E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/R11E.png')]
    walkLeft = [pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L11E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L10E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L9E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L8E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L7E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L6E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L5E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L4E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L3E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L2E.png'), pygame.image.load('C:/Users/91623/Documents/Turtle Workspace/Python Turtle/L1E.png')]
    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x,self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y+2, 31, 57)
        self.health = 50
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (215,0,0), (self.hitbox[0], self.hitbox[1] - 10, 70, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 10, 70 - (70/50) * (50 - self.health), 10))
            self.hitbox = (self.x + 20, self.y, 28, 60)
            #pygame.draw.rect(win, (0,0,0), self.hitbox, 2)
                
    def move(self):
        if self.vel > 0:                            # adding up vel means going right
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:                                   # if it reached end point then we need to change the direction
                self.vel = self.vel * -1
                self.walkCount = 0
        else:                                       # going left
            if self.x - self.vel > self.path[0]:
                self.x += self.vel                  # already *-1 so no need to subtracting vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("HIT!")

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0), (223,246,232))
    win.blit(text, (350,10))
    goblin.draw(win)
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# mainloop
font = pygame.font.SysFont('Times New Roman', 30, True)
man = Player(150,380,64,64)
goblin = Enemy(0,380,64,64,300)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)      #frames per second

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] >  goblin.hitbox[1]:  #above the bottom AND below the top
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0]+goblin.hitbox[2]: #make sure x-axis of bullet > hitbox
                man.both_hit()
                score -= 5
    else:
        font2 = pygame.font.SysFont('Times New Roman', 30 , True, True)
        text = font2.render('Well Played! Your Score: '+str(score), 1, (0,0,0))
        win.blit(text, (250 - text.get_width()/2, 250))
        pygame.display.update()
        i = 0
        while i<300:
            pygame.time.delay(5)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius >  goblin.hitbox[1]:  #above the bottom AND below the top
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]: #make sure x-axis of bullet > hitbox
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 7:
            bullets.append(Projectile(round(man.x+man.width//2),round(man.y+man.height//2), 5, (0,0,0), facing))
        shootLoop = 1
            
    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount=0 
        
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount=0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount**2)*0.5*neg
            man.jumpCount -= 1
        else:
            man.jumpCount=10
            man.isJump = False
    redrawGameWindow()
pygame.quit()
