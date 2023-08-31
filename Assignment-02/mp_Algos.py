import pygame
import random
import numpy as np
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)
from collections import deque as queue

vis = [[False for i in range(128)]for i in range (128)]
vis_dfs = [[False for i in range(128)]for j in range (128)]
vis_dj = [[False for i in range(128)]for j in range (128)]

dRow = [ -5, 0, 5, 0]
dCol = [ 0, 5, 0, -5]

#Creating a 128x128 grid
def drawGrid():
    for x in range(0, 128*5, 5):
        for y in range(0, 128*5, 5):
            rectangle = pygame.Rect(x, y, 5, 5)
            pygame.draw.rect(SCREEN, (0, 0, 0), rectangle, 1) 
    # print(SCREEN.get_at((639,1)))

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

def isValid(vis, row, col):
    if (row<1 or col<1 or row>636 or col>636):
        return False
    if (vis[int((row-1)/5)][int((col-1)/5)]):
        return False
    if (SCREEN.get_at((row,col)) == (0, 0, 255, 255)):
        return False
    return True

def isValid_dfs(vis_dfs, row, col):
    if (row<1 or col<1 or row>636 or col>636):
        return False
    if (vis_dfs[int((row-1)/5)][int((col-1)/5)]):
        return False
    if (SCREEN.get_at((row,col)) == (0, 0, 255, 255)):
        return False
    return True

def isValid_dj(vis_dj, row, col):
    if (row<1 or col<1 or row>636 or col>636):
        return False
    if (vis_dj[int((row-1)/5)][int((col-1)/5)]):
        return False
    if (SCREEN.get_at((row,col)) == (0, 0, 255, 255)):
        return False
    return True

def bfs(grid, row, col, dest_row, dest_col):
    value = np.empty((), dtype=object)
    value[()] = (0, 0)
    parents = np.full((128, 128), value, dtype=object)
    q = queue()
    q.append((row, col))
    vis[int((row-1)/5)][int((col-1)/5)] = True
    
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        if ((x,y) != (dest_row, dest_col)):
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if isValid(vis, adjx, adjy):
                    parents[int((adjx-1)/5)][int((adjy-1)/5)] = (x, y)
                    q.append((adjx, adjy))
                    vis[int((adjx-1)/5)][int((adjy-1)/5)] = True
        else:
            break
    shortest_path = []
    current_node = (dest_row, dest_col)
    destination_node = (row, col)
    while (current_node >= destination_node):
        shortest_path.append(current_node)
        shapej_ = pygame.Rect((current_node[0], current_node[1], 3, 3))
        pygame.draw.rect(grid, (255, 0, 0), shapej_, 0)
        current_node = parents[int((current_node[0]-1)/5)][int((current_node[1]-1)/5)]
    print("Total iterations = {}".format(len(shortest_path)))        

def dfs(grid, row, col, dest_row, dest_col):
    st = []
    st.append([row, col])
    value = np.empty((), dtype=object)
    value[()] = (0, 0)
    parents_dfs = np.full((128, 128), value, dtype=object)
    while(len(st)>0):
        curr = st.pop()
        x = curr[0]
        y = curr[1]
        if ((x,y) != (dest_row, dest_col)):
            vis_dfs[int((x-1)/5)][int((y-1)/5)] = True

            for i in range(4):
                adjr = x + dRow[i]
                adjc = y + dCol[i]
                if isValid_dfs(vis_dfs, adjr, adjc): 
                    parents_dfs[int((adjr-1)/5)][int((adjc-1)/5)] = (x, y)   
                    st.append([adjr, adjc])
        else:
            break

    path_dfs = []
    current_node = (dest_row, dest_col)
    destination_node = (row, col)
    shapej_ = pygame.Rect((1, 1, 3, 3))
    pygame.draw.rect(grid, (0, 255, 0), shapej_, 0)
    while (current_node != destination_node):
        path_dfs.append(current_node)
        shapej_ = pygame.Rect((current_node[0], current_node[1], 3, 3))
        pygame.draw.rect(grid, (255, 0, 255), shapej_, 0)
        current_node = parents_dfs[int((current_node[0]-1)/5)][int((current_node[1]-1)/5)]
    print("Total iterations = {}".format(len(path_dfs)+1))  

def dijkstar(grid, row, col, dest_row, dest_col):
    pr_q = []
    dist = [[float("inf") for j in range(128)] for i in range(128)]
    val = np.empty((), dtype=object)
    val[()] = (row, col)
    previous = np.full((128, 128), val, dtype=object)
    dist[int((row-1)/5)][int((col-1)/5)] = 0
    previous[int((row-1)/5)][int((col-1)/5)] = (row,col)
    pr_q.append((row, col, 0))
    while (len(pr_q) != 0):
        pr_q = sorted(pr_q, key=lambda x: x[2])
        current = pr_q.pop(0)
        if ((current[0] != dest_row) or (current[1] != dest_col)):
            vis_dj[int((current[0]-1)/5)][int((current[1]-1)/5)] = True
            for i in range(4):
                x = current[0] + dRow[i]
                y = current[1] + dCol[i]
                if isValid_dj(vis_dj, x, y):
                    if dist[int((x-1)/5)][int((y-1)/5)] > (dist[int((current[0]-1)/5)][int((current[1]-1)/5)] +5):
                        dist[int((x-1)/5)][int((y-1)/5)] = (dist[int((current[0]-1)/5)][int((current[1]-1)/5)] +5)
                        pr_q.append((x, y, dist[int((x-1)/5)][int((y-1)/5)]))
                    previous[int((x-1)/5)][int((y-1)/5)] = (current[0], current[1])
                    vis_dj[int((x-1)/5)][int((y-1)/5)] = True                
        else:
            break
    path = []
    curr = (dest_row, dest_col)
    while (curr[0] != row or curr[1] != col):
        path.append(curr)
        curr = previous[int((curr[0]-1)/5)][int((curr[1]-1)/5)]
    path.append((row, col))
    path.reverse()
    print("Total iterations = {}".format(len(path)))
    for node in path:
        shapep_ = pygame.Rect((node[0], node[1], 3, 3))
        pygame.draw.rect(grid, (0, 255, 0), shapep_, 0)

def random_search(grid, row, col, dest_row, dest_col):
    path = []
    count = 0
    while (count<50000 and ((row, col)!=(dest_row, dest_col))):
        path.append([row, col])
        i = np.random.randint(4)
        x = row + dRow[i]
        y = col + dCol[i] 
        if isValid(vis, x, y):
            row = x
            col = y 
            # print(row, col)
        count+=1
        print(count)

    for p in path:
        shaper_ = pygame.Rect((p[0], p[1], 3, 3))
        pygame.draw.rect(grid, (0, 255, 0), shaper_, 0)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((128*5, 128*5))
    SCREEN.fill((255, 255, 255))
    running = True
    coverage = int(input("Please enter the Coverage value in percent:\n"))   #Input the coverage from the command line instead of function.
    drawGrid()     
    generate_shape(coverage)
    # bfs(SCREEN, 1, 1, 636, 636)
    # dfs(SCREEN, 1, 1, 636, 636)
    random_search(SCREEN, 1, 1, 636, 636)    
        
    # dijkstar(SCREEN, 1, 1, 636, 636)
    
    while running:     
        for event in pygame.event.get():  #Only to kill the screen by pressing escape key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        pygame.display.update()
if __name__ == "__main__":main()