import pygame
import random
import math
from pygame import mixer
pygame.init()
clock = pygame.time.Clock()
background = pygame.image.load("background.jpg")
screen = pygame.display.set_mode((900, 600))
running = True
pygame.display.set_caption("Spacewarriors")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
#Player
playerX = 400
playerX_change = 0
playerY = 500
score = 0
playerImg = pygame.image.load("player.png")
score_font = pygame.font.Font("freesansbold.ttf", 45)
score_text = score_font.render("Score: "+str(score),True,"red")
# Meteorite
meteoriteImg = []
meteoriteX = []
meteoriteY = []
meteoriteX_change = []
meteoriteY_change = []
num_of_meteorites = 3

for i in range(num_of_meteorites):
    meteoriteImg.append(pygame.image.load("meteorite.png"))
    meteoriteX.append(random.randint(64,836))
    meteoriteY.append(random.randint(0,150))
    meteoriteX_change.append(0)
    meteoriteY_change.append(5)
ufoImg = pygame.image.load("ufo.png")
ufoX = random.randint(0,900)
ufoY = random.randint(0,150)
ufoX_change = 5
ufoY_change = 0

def ufo(x,y):
    screen.blit(ufoImg,(x,y))
coinImg = pygame.image.load("star.png")
coinX = random.randint(32,868)
coinY = 0
coinX_change = 0
coinY_change = 6
lazerImg = pygame.image.load("lazer.png")
lazerX = ufoX
lazerY = ufoY
lazerX_change = ufoX_change
lazerY_change = 5

def lazer(x,y):
    screen.blit(lazerImg,(x,y))

def coin(x,y):
    screen.blit(coinImg,(x,y))

def meteorite(x, y, i):
    screen.blit(meteoriteImg[i], (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def game_over_screen():
    over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))

def isCollision1(meteoriteX, meteoriteY, playerX, playerY):
    distance = math.sqrt((math.pow(meteoriteX - playerX, 2)) + (math.pow(meteoriteY - playerY, 2)))
    if distance < 60:
        return True
    else:
        return False
def isCollision2(coinX,coinY,playerX,playerY):
        distance = math.sqrt((math.pow(coinX - playerX, 2)) + (math.pow(coinY - playerY, 2)))
        if distance < 60:
            return True
        else:
            return False
def isCollision3(lazerX,lazerY,playerX,playerY):
    distance = math.sqrt((math.pow(lazerX - playerX, 2)) + (math.pow(lazerY - playerY, 2)))
    if distance < 60:
        return True
    else:
        return False
def isCollision4(bulletX,bulletY,playerX,playerY):
    distance = math.sqrt((math.pow(bulletX - playerX, 2)) + (math.pow(bulletY - playerY, 2)))
    if distance < 60:
        return True
    else:
        return False
font = pygame.font.Font("freesansbold.ttf", 64)
wel_font = pygame.font.Font("freesansbold.ttf", 32)
game_over = False
def welcome():
    global running
    global font
    global game_over
    screen.fill("black")
    while running:
        screen.fill("black")
        wel_text1 = wel_font.render("Welcome to Spacewarriors",True,"red")
        wel_text2= wel_font.render("Press Enter to Start",True,"red")
        screen.blit(wel_text1,(250,250))
        screen.blit(wel_text2,(300,300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
def gameloop():
    global running
    global game_over
    global playerX
    global playerX_change
    global coinY
    global coinX
    global score_text
    global score
    global lazerX
    global lazerY
    global ufoX 
    while running:
        screen.fill("black")
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -7
                    if event.key == pygame.K_RIGHT:
                        playerX_change = 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        playerX_change = 0

        if not game_over:
            playerX += playerX_change
            if playerX < 0:
                playerX = 0
            elif playerX > 836:
                playerX = 836

            for i in range(num_of_meteorites):
                meteoriteY[i] += meteoriteY_change[i]
                collision = isCollision1(meteoriteX[i], meteoriteY[i], playerX, playerY)

                if meteoriteY[i] >= 600:
                    meteoriteX[i] = random.randint(64, 836)
                    meteoriteY[i] = 0

                if collision:
                    game_over = True
                    break

                meteorite(meteoriteX[i], meteoriteY[i], i)
            coinY += coinY_change
            collision2 = isCollision2(coinX,coinY,playerX,playerY)
            if collision2:
                score += 1
                score_text = score_font.render("Score: "+str(score),True,"red")
                coinImg = pygame.image.load("star.png")
                coinX = random.randint(64,836)
                coinY = 0
            screen.blit(score_text,(0,0))
            if coinY > 600:
                coinImg = pygame.image.load("star.png")
                coinX = random.randint(64,836)
                coinY = 0
            
            if score >= 20:
                for i in range(num_of_meteorites):
                    meteoriteY_change[i] = 4
                    meteoriteY[i]+= meteoriteY_change[i]
                ufo(ufoX,ufoY)
                ufoX += ufoX_change
                lazer(lazerX,lazerY)
                lazerY +=lazerY_change
                if lazerY >= 600:
                    lazer(lazerX,lazerY)
                    lazerY = ufoY+32
                    lazerX = ufoX
                    lazerX += ufoX_change
                    if lazerX >= 900:
                        lazerX = ufoX
                if ufoX >= 900:
                    ufoX = 0
            coin(coinX,coinY)
            collision3 = isCollision3(lazerX,lazerY,playerX,playerY)
            if collision3:
                game_over = True
            player(playerX, playerY)
            clock.tick(60)
        else:
            game_over_screen()

        pygame.display.update()
welcome()
pygame.quit()