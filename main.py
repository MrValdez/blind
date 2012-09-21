import pygame
import random
import math

pygame.init()
pygame.display.set_caption ("Blind Girl prototype")
pygame.mouse.set_visible(True)

resolution = [800,540]

screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

GameRunning = True

mouse_pressed = pygame.mouse.get_pressed()    

#background = pygame.image.load("background.png")

class CirclePing:
    def __init__(self, pos):
        self.pos = pos
        self.radius = 0
        self.inner_radius = 0

        self.max_radius = 300

    def isAlive(self):
        if self.radius >= self.max_radius and self.inner_radius >= self.max_radius:
            return False
        return True

    def update(self):
        if self.radius < self.max_radius:
            self.radius += 10

        if self.radius >= self.max_radius * .75:
            self.inner_radius += 11
        
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(128, 128, 128), self.pos, self.radius)
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), self.pos, self.inner_radius)

class Items:
    def __init__(self, min_pos, max_pos):        
        self.pos = [random.randint(min_pos[0], max_pos[0]),
                        random.randint(min_pos[1], max_pos[1])]

        images = ["Bee_Spring_2010", "Daisy_colored_01", "Daisy_colored_02"]
        self.image = pygame.image.load(random.choice(images) + ".png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.15)
        
    def draw(self, screen):
        screen.blit(self.image, self.pos)

CirclePingCollection = []
ItemCollection = []

def SpawnItem():
    newItem = Items([0,0], resolution)
    ItemCollection.append(newItem)

for i in range(12):
    SpawnItem()

while GameRunning:
    screen.fill(pygame.Color(0,0,0))
    #screen.blit(background, [0,0])
    
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
        #text = font.render("test", False, pygame.Color(255, 255, 255))
        #screen.blit(text, [0,0])
        CirclePingCollection.append(CirclePing(mouse_pos))

    for Circle in CirclePingCollection:
        Circle.update()
        Circle.draw(screen)

    for Item in ItemCollection:
        for Circle in CirclePingCollection:
            def IsInside(Circle, Item):
                origin = [Circle.pos[0] - Item.pos[0], Circle.pos[1] - Item.pos[1]]
                distance = origin[0] * origin[0] + origin[1] * origin[1]                
                distance = math.sqrt(distance)

                if distance <= Circle.radius and distance >= Circle.inner_radius:
                    return True
                
                return False
                
            if IsInside(Circle, Item):
                Item.draw(screen)

    for Circle in CirclePingCollection:
        if not Circle.isAlive():
            CirclePingCollection.remove(Circle)

    pygame.display.update()
    clock.tick(60)
