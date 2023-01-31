import pygame
import random
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

#Creating a 128x128 grid
def drawGrid():
    for x in range(0, 128*5, 5):
        for y in range(0, 128*5, 5):
            rectangle = pygame.Rect(x, y, 5, 5)
            pygame.draw.rect(SCREEN, (0, 0, 0), rectangle, 1) 

#Obstacle covering 5 grid cells
def shape_1():
    b = random.randint(0, 122)
    a = random.randint(0, 127)
    for i in range (5):
        shape1_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape1_, 0)
        b+=1

#Obstacle covering 5 grid cells
def shape_1_inv():
    b = random.randint(0, 127)
    a = random.randint(0, 122)
    for i in range (5):
        shape1_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape1_, 0)
        a+=1
#Obstacle covering 9 grid cells
def shape_2():
    b = random.randint(0, 119)
    a = random.randint(0, 125)
    for i in range (3):
        for j in range(3):
            shape2_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
            pygame.draw.rect(SCREEN, (0, 0, 255), shape2_, 0)
            b+=1
        a+=1

#Obstacle covering 9 grid cells
def shape_2_inv():
    b = random.randint(0, 125)
    a = random.randint(0, 119)
    for i in range (3):
        for j in range(3):
            shape2_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
            pygame.draw.rect(SCREEN, (0, 0, 255), shape2_, 0)
            a+=1
        b+=1

#Obstacle covering 8 grid cells
def shape_3():
    b = random.randint(0, 121)
    a = random.randint(0, 126)
    for i in range (4):
        for j in range(2):
            shape2_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
            pygame.draw.rect(SCREEN, (0, 0, 255), shape2_, 0)
            b+=1
        a+=1

#Obstacle covering 4 grid cells
def shape_4():
    b = random.randint(0, 126)
    a = random.randint(1, 126)
    for i in range (2):
        shape4_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        shape4_ = pygame.Rect((a-i)*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        shape4_ = pygame.Rect((a+i)*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        b+=1

#Obstacle covering 10 grid cells
def shape_5():
    b = random.randint(0, 124)
    a = random.randint(3, 124)
    for i in range (4):
        shape4_ = pygame.Rect(a*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        shape4_ = pygame.Rect((a-i)*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        shape4_ = pygame.Rect((a+i)*5 +1, b*5 +1, 3, 3)
        pygame.draw.rect(SCREEN, (0, 0, 255), shape4_, 0)
        b+=1


def generate_shape(coverage):
    #Creatinng 164 obstacles in frst go
    #Changing the number of loops depeding on coverage
    for i in range(coverage):
        for j in range(3):
            shape_1()
            shape_1_inv()
            shape_2()
            shape_2_inv()
            shape_3()
            shape_4()
            shape_5()
        shape_5()
        shape_4()

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((128*5, 128*5))
    SCREEN.fill((255, 255, 255))
    running = True
    coverage = int(input("Please enter the Coverage value in percent:\n"))   #Input the coverage from the command line instead of function.
    drawGrid()     
    generate_shape(coverage)
    while running:
        for event in pygame.event.get():  #Only to kill the screen by pressing escape key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pygame.display.update()
if __name__ == "__main__":main()