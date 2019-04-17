import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

class duck(object):
    def __init__(self, img, x, y, width, height, start, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.start = start
        self.end = end
        self.path = [self.x, self.end]
        self.vel = 10
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

def drawTitle(screen, signLocation, bg, sign, mallard_1, mallard_2, mallard_3, diver, promptFont):
    screen.blit(bg, (0, 0))
    screen.blit(sign, (1205, 97))
    mallard_1.draw(screen)
    mallard_2.draw(screen)
    mallard_3.draw(screen)
    screen.blit(diver, (0, 0))
    screen.blit(promptFont, (850, signLocation))
    pygame.display.update()

def title(screen):
    # Title Screen---------------------------------------------------------------------------------------------------------
    pygame.display.set_caption("Cheat Lake Dive Club")
    clock = pygame.time.Clock()

    # Rockwell Nova MS
    myfont = pygame.font.Font('../assets/fredoka.ttf', 130)
    # myfont = pygame.font.SysFont('Rockwell Nova MS', 150)
    promptFont = myfont.render('Press A to Begin', True, (255, 255, 255))

    # Load Background + Scale
    bg = pygame.image.load('../assets/background.png')
    bg = pygame.transform.scale(bg, (1920, 1080))

    # Play Background Sounds
    pygame.mixer.music.load("../assets/Lake_Sounds.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.3)

    # Load Assets + Scale
    sign = pygame.image.load('../assets/CheatLakeSign.png')
    sign = pygame.transform.scale(sign, (662, 435))
    diver = pygame.image.load('../assets/diver.png')
    diver = pygame.transform.scale(diver, (1920, 1080))
    mallard_1 = duck('../assets/Mallard.png', -300, 500, 97, 50, -300, 2300)
    mallard_2 = duck('../assets/Mallard.png', -150, 505, 117, 60, -150, 2450)
    mallard_3 = duck('../assets/Mallard.png', -255, 550, 136, 70, -255, 2345)

    # Title Screen Loop
    introContinue = True
    signLocation = 750
    down = 1

    while introContinue:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            introContinue = False

        if (signLocation <= 800 and down == 1):
            signLocation += 2
        if (signLocation == 800 and down == 1):
            down = 0
        if (down == 0):
            signLocation -= 2
        if (signLocation == 700 and down == 0):
            down = 1

        drawTitle(screen, signLocation, bg, sign, mallard_1, mallard_2, mallard_3, diver, promptFont)
