from inventoryScreen2 import inventory2
from inventoryScreen2 import determineInventory2
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

    def render(self, screen):
        global air

        if self.gender == 'female':  # Female Diver
            image = self.diverFemale
        else:  # Male Diver
            image = self.diverMale

        if (air > 4000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 3000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 2000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        elif (air > 1000):
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1200, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))
        else:
            screen.blit(self.background, (self.x, self.y))
            screen.blit(pygame.transform.scale(image, (self.width, self.height)), (600, 300))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1100, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1200, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1300, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1400, 800))
            screen.blit(pygame.transform.scale(self.bubble, (100, 100)), (1500, 800))

            # makes hellbender appear by the player's head when player is in these coordinated
            # below the the right hook of the starter boat near the top rocks
            # level with the center of the wheel / look for the bleh's
        if (self.x > -950 and self.x < -750 and self.y > -3825 and self.y < -3650):
            screen.blit(pygame.transform.scale(self.hellbender, (200, 100)), (1200, 300))

        # BEWARE THE HOOKS! THESE KILL THE PLAYER!!!!!!!!!!!!!!
        # (In order from left most hook to right most hook)
        if (self.x > -650 and self.x < -100 and self.y > -2220 and self.y < -1925):
            air = 5050
        if (self.x > -1200 and self.x < -525 and self.y > -3125 and self.y < -2850):
            air = 5050
        if (self.x > -4575 and self.x < -3900 and self.y > -2750 and self.y < -2475):
            air = 5050
        #This one has the door
        #if (self.x > -5200 and self.x < -4525 and self.y > -2200 and self.y < -1925):
        #    air = 5050

def game2(screen, playerGender):
    inventoryItems = [0, 0, 0, 0, 0, 0, 0]
    clock = pygame.time.Clock()
    playerX, playerY = 0, 0
    player = Sprite(-800, -300, playerGender)
    gameContinue = True
    global air
    air = 0

    while gameContinue:
        for event in pygame.event.get():
            print('-------------------------------')
            print('PlayerX:', player.x)
            print('PlayerY:', player.y)

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                pygame.quit()

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
                    inventory2(screen, inventoryItems)
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
        determineInventory2(player.x, player.y, inventoryItems)
        player.render(screen)

        if(air > 5000):
            return

        clock.tick(60)
        pygame.display.flip()