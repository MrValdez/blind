import pygame

pygame.init()
pygame.display.set_caption ("Blind Girl prototype")
pygame.mouse.set_visible(True)

screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

GameRunning = True

mouse_pressed = pygame.mouse.get_pressed()    

while GameRunning:
    screen.fill(pygame.Color(0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            GameRunning = False
            
        if event.type == pygame.KEYDOWN and    \
            event.key == pygame.K_ESCAPE:
            pygame.quit()
            GameRunning = False

    prev_mouse_pressed = mouse_pressed
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0] and not prev_mouse_pressed[0]:
        text = font.render("test", False, pygame.Color(255, 255, 255))
        screen.blit(text, [0,0])

    pygame.display.update()
    clock.tick(60)
