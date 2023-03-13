import pygame
from scripts.InterfaceElements import Button
import random
a = random.choices([2,4], [0.65, 0.35])
print(a)
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
fps = 30
button = Button(50, 50, (220, 200, 190), (255, 255, 255))
loop = True
def close():
    quit(666)

def drawmad():
    display = pygame.Surface((100, 100))
    display.fill((0, 0, 0))
    button.draw(0,0, display, action=close)
    pygame.draw.circle(display, (255, 255, 255), (100, 100), 80)
    display = pygame.transform.scale(display, (800, 600))
    return display

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(228)
    window.fill((255, 0, 0))
    
    
    window.blit(drawmad(), (10,0))
    pygame.display.flip()
    clock.tick(fps)
