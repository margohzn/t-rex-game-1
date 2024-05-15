import pygame
from pygame.locals import *
import random 

pygame.init()

#screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((173,216,230))

#additional
pygame.display.set_caption("T-rex game!")
FONT = pygame.font.SysFont("Times new roman", 50)


#variables for the game 
ground_scroll = 0 
scroll_speed = 5
score = 0 
moving = False
game_over = False
score = 0 
tree_gap = 200 
tree_frequency = 1500 #in millieseconds, time till a new tree is generated in the game diffrent to the gap 
jumped_tree = False
last_tree = pygame.time.get_ticks() - tree_frequency


# loading images for the ground (what will scroll while moving = True)
'''ground_img = pygame.image.load("")'''
clouds = pygame.image.load("cloud.png")


class Trex(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.timages = [] 
        self.index = 0 
        self.counter = 0 
        for i in range(1,4):
            timg = pygame.image.load(f"trex{i}.png")
            self.timages.append(timg)
        self.timage = self.timages[self.index]
        self.rect = self.timage.get_rect()
        self.rect.center = [x,y]
        self.vel = 0 
        self.clicked = False 


