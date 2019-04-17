import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

def drawGender(screen, bg):
    screen.blit(bg, (0, 0))
    pygame.display.update()

def gender(screen):
    bg = pygame.image.load('../assets/gender_girl.png')
    bg = pygame.transform.scale(bg, (1920, 1080))

    # Gender Screen Loop
    genderContinue = True
    currentGender = 'female'

    while genderContinue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if currentGender == 'female' and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                currentGender = 'male'
                bg = pygame.image.load('../assets/gender_boy.png')
                bg = pygame.transform.scale(bg, (1920, 1080))
            elif currentGender == 'male' and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                currentGender = 'female'
                bg = pygame.image.load('../assets/gender_girl.png')
                bg = pygame.transform.scale(bg, (1920, 1080))
            elif keys[pygame.K_SPACE] and currentGender == 'female':
                genderContinue = False
            elif keys[pygame.K_SPACE] and currentGender == 'male':
                genderContinue = False
            drawGender(screen, bg)

    return currentGender