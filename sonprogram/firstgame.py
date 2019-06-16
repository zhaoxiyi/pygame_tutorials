import pygame
import random

#define screen size
WIDTH = 360
HEIGHT = 480
FPS = 30

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

pygame.quit()
