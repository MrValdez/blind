import pygame

pygame.init()
pygame.display.set_caption ("Blind Girl prototype")
pygame.mouse.set_visible(True)

screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

GameRunning = True

mouse_pressed = pygame.mouse.get_pressed()    

class CirclePing:
    def __init__(self, pos):
        self.pos = pos
        self.radius = 0

    def isAlive(self):
        if self.radius > 300:
            return False
        return True

    def update(self):
        self.radius += 1

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(128, 128, 128), self.pos, self.radius)

CirclePingCollection = []

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
        CirclePingCollection.append(CirclePing(mouse_pos))

    for Circle in CirclePingCollection:
        Circle.update()
        Circle.draw(screen)

    for Circle in CirclePingCollection:
        if not Circle.isAlive():
            CirclePingCollection.remove(Circle)

    pygame.display.update()
    clock.tick(60)
