from scripts.InterfaceElements import get_key
import pygame
bindedButtons = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d
        }

print(get_key(pygame.K_w, bindedButtons))