from Sudoku import *
import pygame


# Initializing Pygame
pygame.init()

# Setting variables to colors:
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

# Setting screen size
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


cellSize = 20
board = Surface((cellSize * 8, cellSize * 8))
board.fill((255, 255, 255))
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(board, (0,0,0), (x*size, y*size, size, size))