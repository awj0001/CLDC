import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()


class Sprite:
    def __init__(self, x, y, gender):
        self.x = x
        self.y = y
        self.width = 480
        self.height = 270
        self.gender = gender
        self.diverFemale = pygame.image.load("Diver Female.png")
        self.diverMale = pygame.image.load("Diver Male.png")
        self.background = pygame.image.load("gamescreen.png")

    def update(self):
        self.render()

    def render(self):
        if self.gender == 0:  # Female Diver
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(self.diverFemale, (self.width, self.height)), (500, 500))

        else:  # Male Diver
            # screen.blit(pygame.transform.scale(self.hellbender, (426, 90)), (600, 150))
            # screen.blit(pygame.transform.scale(self.hellbender, (426, 90)), (750, 700))
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(self.diverMale, (self.width, self.height)), (500, 500))


class duck(object):
    def __init__(self, img, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 5
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (width, height))

    def draw(self, screen):
        self.move('right')
        screen.blit(self.img, (self.x, self.y))

    def move(self, direction):
        if direction == 'right':
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.x = self.start


def redrawWindow(state):
    if (state == 1):
        screen.blit(bg, (0, 0))
        screen.blit(sign, (1205, 97))
        mallard_1.draw(screen)
        mallard_2.draw(screen)
        mallard_3.draw(screen)
        screen.blit(diver, (0, 0))
        screen.blit(promptFont, (825, 850))

    if (state == 2):
        screen.blit(bg, (0, 0))

    pygame.display.update()


screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Cheat Lake Dive Club")
clock = pygame.time.Clock()

# Title Screen Font
myfont = pygame.font.SysFont('Rockwell Nova MS', 150)
promptFont = myfont.render('PRESS A TO BEGIN', True, (255, 255, 255))

# Load Background + Scale
bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (1920, 1080))

# Play Background Sounds
pygame.mixer.music.load("Lake_Sounds.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.3)

# Load Assets + Scale
sign = pygame.image.load('CheatLakeSign.png')
sign = pygame.transform.scale(sign, (662, 435))
diver = pygame.image.load('diver.png')
diver = pygame.transform.scale(diver, (1920, 1080))
mallard_1 = duck('Mallard.png', -300, 500, 97, 50, -300, 2300)
mallard_2 = duck('Mallard.png', -150, 505, 117, 60, -150, 2450)
mallard_3 = duck('Mallard.png', -255, 550, 136, 70, -255, 2345)

# Title Screen Loop
introContinue = True

while introContinue:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        introContinue = False

    redrawWindow(1)

# Load Background
bg = pygame.image.load('gender_girl.png')
bg = pygame.transform.scale(bg, (1920, 1080))

# Gender Screen Loop
genderContinue = True
currentGender = 'female'

while genderContinue:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if currentGender == 'female' and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        currentGender = 'male'
        bg = pygame.image.load('gender_boy.png')
        bg = pygame.transform.scale(bg, (1920, 1080))
    elif currentGender == 'male' and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        currentGender = 'female'
        bg = pygame.image.load('gender_girl.png')
        bg = pygame.transform.scale(bg, (1920, 1080))
    elif keys[pygame.K_SPACE] and currentGender == 'female':
        genderContinue = False
    elif keys[pygame.K_SPACE] and currentGender == 'male':
        genderContinue = False
    redrawWindow(2)

# Game Screen Loop
moveX, moveY = 0, 0
if (currentGender == 'female'):
    player = Sprite(100, 150, 0)
else:
    player = Sprite(100, 150, 1)
gameContinue = True

while gameContinue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = 25
            if event.key == pygame.K_RIGHT:
                moveX = -25
            if event.key == pygame.K_UP:
                moveY = 25
            if event.key == pygame.K_DOWN:
                moveY = -25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
            if event.key == pygame.K_RIGHT:
                moveX = 0
            if event.key == pygame.K_UP:
                moveY = 0
            if event.key == pygame.K_DOWN:
                moveY = 0

    player.x += moveX
    player.y += moveY
    player.update()

    clock.tick(60)

    pygame.display.flip()

pygame.quit()
