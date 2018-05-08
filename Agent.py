from pygame.sprite import Sprite
import pygame
import random

class Agent(Sprite):
    # Screen width and height
    width: int
    height: int

    # Right facing sprite images
    movingAgentRight = []
    # Left facing sprite images
    movingAgentLeft = []

    # Current sprite list being used
    agentSprite = []

    # Total frames (image sprite count)
    totalAgentFrames : int

    # Keep track of the current agent sprite frame
    currentAgentFrame : int

    # Keep track of the current punching sprite frame
    currentPunchingFrame : int

    # Current agent sprite image being used
    currentAgentIndex : int

    # Current punching sprite image being used
    currentPunchingIndex: int

    # 0 - left, 1 - right, 2 - no movement
    direction : int

    # Uniform w x h size of each image to create a rect object
    imageSizes: (int, int)

    # Boolean flag to determine if sprite is moving
    moving : bool

    # Boolean flag to determine if sprite is punching
    punching : bool

    # Number of sprite frames used for punching
    punchingSpriteCount : int

    # Variable self.image is inherited from the parent class: pygame.sprite.Sprite

    def __init__(self, width, height):
        Sprite.__init__(self)
        self.width = width
        self.height = height

        # Init sprite images
        for index in range(1, 9):
            self.movingAgentRight.append(pygame.image.load("resources/images/agent" + (str(index)) + ".png"))
        self.movingAgentRight.append(pygame.image.load("resources/images/agentpunch1.png"))
        self.movingAgentRight.append(pygame.image.load("resources/images/agentpunch2.png"))
        for image in self.movingAgentRight:
            self.movingAgentLeft.append(pygame.transform.flip(image, True, False))

        self.totalAgentFrames = len(self.movingAgentRight)
        self.currentAgentFrame = 0
        self.currentPunchingFrame = 0
        self.currentAgentIndex = 0
        self.currentPunchingIndex = 0
        self.direction = 2  # Sprite has no direction

        self.imageSizes = self.movingAgentRight[0].get_size()
        self.rect = pygame.Rect((0,0), self.imageSizes)
        self.rect.centerx = width//2 # Placement of sprite on the background (center x)
        self.rect.centery = (height//2)+70 # center y

        # Default image shown is a right moving agent at index start of 0
        self.image = self.movingAgentRight[self.currentAgentIndex]
        # Set default sprite list to right facing sprites
        self.agentSprite = self.movingAgentRight
        # Is agent moving?
        self.moving = False
        # Is agent punching?
        self.punching = False
        self.punchingSpriteCount = 2

    def update(self):
        # Reset movement speed to 0
        self.dx = 0
        self.moving = False
        self.punching = False
        direction = pygame.key.get_pressed()
        if(direction[pygame.K_RIGHT]):
            self.direction = 1
            self.agentSprite = self.movingAgentRight
            self.dx = 5
            self.moving = True
            self.punching = False
        elif(direction[pygame.K_LEFT]):
            self.direction = 0
            self.agentSprite = self.movingAgentLeft
            self.dx = -5
            self.moving = True
            self.punching = False
        elif(direction[pygame.K_SPACE]):
            self.moving = False
            self.punching = True

        if(self.moving):
            self.currentAgentFrame += 1
            if(self.currentAgentFrame >= self.totalAgentFrames):
                self.currentAgentFrame = 0
                self.currentAgentIndex = (self.currentAgentIndex + 1) % (len(self.agentSprite) - self.punchingSpriteCount)
                self.image = self.agentSprite[self.currentAgentIndex]
            # Prevent sprite from moving out of bounds
            if(self.rect.right > self.width):
                self.rect.right = self.width
            elif(self.rect.left < 0):
                self.rect.left = 0
            else:
                self.rect.move_ip(self.dx, 0)
        if(self.punching):
            self.currentPunchingFrame += 1
            if(self.currentPunchingFrame >= self.punchingSpriteCount):
                self.currentPunchingFrame = 0
                self.currentPunchingIndex = (self.currentPunchingIndex + 1) % 2
                self.image = self.agentSprite[self.currentPunchingIndex + len(self.agentSprite)-2]
