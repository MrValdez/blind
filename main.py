import pygame

pygame.init()
pygame.display.set_caption ("Blind Girl prototype")
pygame.mouse.set_visible(True)

screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()

GameRunning = True

while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GameRunning = False
            
        if event.type == pygame.KEYDOWN and    \
            event.key == pygame.K_ESCAPE:
            pygame.quit()
            GameRunning = False

    mouse_pos = pygame.mouse.get_pos()

    pygame.display.update()
    clock.tick(60)
