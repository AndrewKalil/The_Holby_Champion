#!/usr/bin/python3

import sys, pygame
from pygame.locals import *
if __name__== '__main__':
    pygame.init()

ventana = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Kamikase")

guerrero = pygame.image.load("images/guerrero.py")
posX, posY = 130, 70

ventana.blit(guerrero, (posX, posY))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()