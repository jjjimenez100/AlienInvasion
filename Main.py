import pygame
from Agent import Agent
from Alien import Alien
from Label import Label

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
FPS = 50

backgroundImage = pygame.transform.scale(pygame.image.load("resources/images/bg.gif"), (500,400))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Punch it out!")
screen.blit(backgroundImage, (0,0))

gameLoop = False
timer = pygame.time.Clock()
agentSprite = Agent(SCREEN_WIDTH, SCREEN_HEIGHT)

iteration = 0
aliens = []
score = 0

instructions = Label("PUNCH AS MANY AS YOU CAN!", 40, SCREEN_WIDTH, SCREEN_HEIGHT, 40)
key = Label("press spacebar to punch", 30, SCREEN_WIDTH, SCREEN_HEIGHT, 70)
scoreLabel = Label("Score: " + (str(score)), 25, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT-50)
sprites = pygame.sprite.Group(agentSprite, instructions, key, scoreLabel)
punchingSound = pygame.mixer.Sound("resources/music/punch.wav")
bgMusic = pygame.mixer.Sound("resources/music/bgmusic.ogg")
bgMusic.play(-1)

while not gameLoop:
    timer.tick(FPS)
    for alien in aliens:
        if (agentSprite.rect.colliderect(alien.rect)):
            if(agentSprite.punching):
                punchingSound.play()
                score += 1
                sprites.remove(alien)
                aliens.remove(alien)
                scoreLabel.text = "Score: " + (str(score))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            gameLoop = True

    if(iteration % 70 == 0):
        newAlien = Alien(SCREEN_WIDTH, SCREEN_HEIGHT)
        aliens.append(newAlien)
        sprites.add(newAlien)
    sprites.clear(screen, backgroundImage)
    sprites.update()
    sprites.draw(screen)
    iteration += 1
    pygame.display.update()
