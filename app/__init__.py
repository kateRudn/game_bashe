import pygame
from unipath import Path
import os

M = 3
N = 15

WIDTH = 800
HEIGHT = 650

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (200, 162, 200)
RED = (255, 41, 77)
GREEN = (1, 50, 32)

successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
pygame.display.set_caption('Игра Баше')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_font = pygame.font.SysFont('Comic Sans MS', 30)