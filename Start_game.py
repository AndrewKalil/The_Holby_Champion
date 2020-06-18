#!/usr/bin/python3

import sys, pygame
from time import sleep
from pygame.sprite import Sprite
from pygame.locals import *

"""Champions Class"""
from fighter import Fighter
from mage import Mage
from rogue import Rogue
from champ import Champ
from base import Base


class Game(Champ):

    def __init__(self, h_1, h_2):
        self.h_1 = h_1
        self.h_2 = h_2

    @property
    def h_1(self):
        return self.__h_1

    @h_1.setter
    def h_1(self, value):
        self.__h_1 = value

    @property
    def h_2(self):
        return self.__h_2

    @h_2.setter
    def h_2(self, value):
        self.__h_2 = value

        pygame.init()
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)

        self.bright_red = (255, 0, 0)
        self.bright_green = (0, 255, 0)

        self.width = 800
        self.height = 600
        self.display_surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Kamikase')
        self.clock = pygame.time.Clock()

        self.image1 = pygame.image.load("images/aspec_fighter.png")
        self.image2 = pygame.image.load("images/aspec_mago.png")
        self.guerrero = pygame.image.load("images/guerrero.png")
        self.mago = pygame.image.load("images/Mago.png")

    def message_display(self, text):
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((self.width/2), (self.height/2))
        self.display_surface.blit(TextSurf, TextRect)

        pygame.display.update()
        time.sleep(2)
        game_loop()

    def print_screen(self, msg, x, y):
        font = pygame.font.SysFont("comicsansms", 22)
        self.text = font.render(msg, True, self.black)
        self.display_surface.blit(self.text, (x, y))

    def text_screen(self, msg, value, x, y):
        font = pygame.font.SysFont("comicsansms", 22)
        self.text = font.render(msg+str(value), True, self.black)
        self.display_surface.blit(self.text, (x, y))

    def text_objects(self, text, font):
        self.textSurface = font.render(text, True, self.black)
        return self.textSurface, self.textSurface.get_rect()


    def button_function(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.display_surface, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                if action == "Start":
                    self.game_loop()
                elif action == "Exit":
                    pygame.quit()
                    quit()

        else:
            pygame.draw.rect(self.display_surface, ic,(x, y, w, h))

            smallText = pygame.font.SysFont("comicsansms", 20)
            TextSurf, TextRect = self.text_objects(msg, smallText)
            TextRect.center = ((x+(w/2)), (y+(h/2)))
            self.display_surface.blit(TextSurf, TextRect)

    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.display_surface.fill(self.white)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_objects("Kamikase", largeText)
            TextRect.center = ((self.width/2), (self.height/2))
            self.display_surface.blit(TextSurf, TextRect)

            self.button_function("Start", 150, 450, 100, 50, self.green, self.bright_green, "Start")
            self.button_function("Exit", 550, 450, 100, 50, self.red, self.bright_red, "Exit")

            pygame.display.update()
            self.clock.tick(15)

    def Champ_1(self):
        self.text_screen("Name :",self.h_1.name, 0, 105)
        self.text_screen("Class :",self.h_1.champ_class, 0, 125)
        self.text_screen("Health :",self.h_1.health, 0, 145)
        self.text_screen("Attack :",self.h_1.attack, 0, 165)
        self.text_screen("Defence :",self.h_1.defence, 0, 185)

    def Champ_2(self):
        self.text_screen("Name :",self.h_2.name, 700, 105)
        self.text_screen("Class :",self.h_2.champ_class, 700, 125)
        self.text_screen("Health :",self.h_2.health, 700, 145)
        self.text_screen("Attack :",self.h_2.attack, 700, 165)
        self.text_screen("Defence :",self.h_2.defence, 700, 185)

    def attack(self, count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, self.black)
        self.display_surface.blit(text,(0,0))

    def game_loop(self):
        while True:
            self.display_surface.fill(self.white)

            self.display_surface.blit(self.image1, (0, 0))
            self.display_surface.blit(self.image2, (700, 0))
            self.display_surface.blit(self.guerrero, (0, 400))
            self.display_surface.blit(self.mago, (600, 400))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            self.Champ_1()
            self.Champ_2()
            self.attack(self.h_2.display_battle_stats)

            if self.h_1.health <= 0 or self.h_2.health <= 0:
                if self.h_1.health > 0:
                    self.text_screen("Player 1 WINS!!", None, 250, 150)
                elif h_2.health > 0:
                    self.text_screen("Player 1 WINS!!", None, 300, 180)

            if self.h_1.health > 0:
                self.print_screen("Player 1 Attacking", 260, 200)
                sleep(2)
            if self.h_2.health > 0:
                self.print_screen("Player 2 Attacking", 280, 230)
                sleep(2)


            pygame.display.update()

p1 = Mage("Sasuke", 1, 1)
print(p1)
p2 = Fighter("Pekka", 1, 1)
print(p2)

h = Game(p1, p2)
h.game_intro()
game_loop()
pygame.quit()
quit()
