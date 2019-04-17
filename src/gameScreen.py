from inventoryScreen import inventory
from inventoryScreen import determineInventory
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawGame(screen, bg):
    screen.blit(bg, (0, 0))
    pygame.display.update()

class Sprite:
    def __init__(self, x, y, gender):
        self.x = x
        self.y = y
        self.width = 700
        self.height = 500
        self.gender = gender
        self.hellbender = pygame.image.load("../assets/Hellbender.png")
        self.bubble = pygame.image.load("../assets/Bubbles.png")
        self.diverFemale = pygame.image.load("../assets/Diver_Female.png")
        self.diverMale = pygame.image.load("../assets/Diver_Male.png")
        self.background = pygame.image.load("../assets/gamescreen.png")
        self.gameover = pygame.image.load("../assets/game_over.png")

    def render(self, air, screen):
        # screen.blit(pygame.transform.scale(self.hellbender, (426, 90)), (100, -2400))

        if self.gender == 0:  # Female Diver
            image = self.diverFemale
        else:  # Male Diver
            image = self.diverMale

        if (air > 4000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1800, 900))
        elif (air > 3000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1700, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1800, 900))
        elif (air > 2000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1600, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1700, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1800, 900))
        elif (air > 1000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1600, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1700, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1800, 900))
        else:
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1600, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1700, 900))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1800, 900))

def game(screen, playerGender):
    inventoryItems = [0, 0, 0, 0, 0, 0, 0]
    clock = pygame.time.Clock()
    playerX, playerY = 0, 0
    player = Sprite(-800, -300, playerGender)
    gameContinue = True
    air = 0

    while gameContinue:
        for event in pygame.event.get():
            print('-------------------------------')
            print('PlayerX:', player.x)
            print('PlayerY:', player.y)

            keys = pygame.key.get_pressed()

            if event.type == pygame.QUIT or keys[pygame.K_SPACE]:
                gameLoop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.x < -200:
                    playerX += 25
                if event.key == pygame.K_RIGHT and player.x > -5900:
                    playerX += -25
                if event.key == pygame.K_UP and player.y < -100:
                    playerY += 25
                if event.key == pygame.K_DOWN and player.y > -3930:
                    playerY += -25
                if event.key == pygame.K_i:
                    inventory(screen, inventoryItems)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerX = 0
                if event.key == pygame.K_RIGHT:
                    playerX = 0
                if event.key == pygame.K_UP:
                    playerY = 0
                if event.key == pygame.K_DOWN:
                    playerY = 0

            if (player.y > -300):
                air = 0
            else:
                air += 20

        player.x += playerX
        player.y += playerY
        determineInventory(player.x, player.y, inventoryItems)
        player.render(air, screen)
        if(air > 5000):
            return

        clock.tick(60)
        pygame.display.flip()