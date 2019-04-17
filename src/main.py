from loadingScreen import title
from genderScreen import gender
from gameScreen import game
from finalScreen import gameOver

import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def main():
    screen = pygame.display.set_mode((1920, 1080))

    while(True):
        title(screen)
        playerGender = gender(screen)

        keepPlaying = 1
        while(keepPlaying == 1):
            game(screen, playerGender)
            choice = gameOver(screen)

            if choice == 1:
                keepPlaying = 0
            if choice == 3:
                pygame.quit()

main()