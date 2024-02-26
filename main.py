import pygame
import random

# Initialize the game

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ship.png')
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Checking for player boundary
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > pygame.display.get_window_size()[0] - playerImg.get_width():
        playerX = pygame.display.get_window_size()[0] - playerImg.get_width()

    playerY += playerY_change
    if playerY < 0:
        playerY = 0
    elif playerY > pygame.display.get_window_size()[1] - playerImg.get_height():
        playerY = pygame.display.get_window_size()[1] - playerImg.get_height()

    # Checking for enemy boundary
    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX > pygame.display.get_window_size()[0] - enemyImg.get_width():
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
