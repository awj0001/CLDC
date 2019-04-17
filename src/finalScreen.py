import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawFinal():
    print('Temp')

def gameOver(screen):
    mainMenu = pygame.image.load('../assets/gameMenu.png')
    restart = pygame.image.load('../assets/gameRestart.png')
    nextLevel = pygame.image.load('../assets/gameLevel.png')

    mainMenu = pygame.transform.scale(mainMenu, (1920, 1080))
    restart = pygame.transform.scale(restart, (1920, 1080))
    nextLevel = pygame.transform.scale(nextLevel, (1920, 1080))
    cont = 1

    screen.blit(mainMenu, (0, 0))
    pygame.display.update()
    print('Here!')
    while cont == 1:
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()

            if(y > 790 and y < 850):
                if(x > 180 and x < 560):
                    screen.blit(mainMenu, (0, 0))
                if(x > 810 and x < 1096):
                    screen.blit(restart, (0, 0))
                if(x > 1367 and x < 1750):
                    screen.blit(nextLevel, (0, 0))

            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if(y > 790 and y < 850 and pressed1 == 1):
                if(x > 180 and x < 560 and pressed1 == 1):
                    return 1
                if(x > 810 and x < 1096 and pressed1 == 1):
                    return 2
                if(x > 1367 and x < 1750 and pressed1 == 1):
                    return 3

            pygame.display.update()



