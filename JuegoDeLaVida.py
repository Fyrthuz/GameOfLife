#!/usr/bin/env python
# coding: utf-8

# In[1]:


from turtle import width
import numpy as np
import pygame
import time

nCols, nRows = 50, 50
width, height = 800, 800

widthPerCol = width / nCols
heightPerRow = height / nRows

matrix = np.random.randint(2,size=(nRows,nCols))

liveCellColor = (255,255,255)
deadCellColor = (0,0,0)



print(matrix)


# In[2]:


def vecinos(i,j,matriz):
    count = 0
    
    neighbours = [
    ((i+1)%nRows,j%nCols),
    ((i+1)%nRows,(j+1)%nCols),
    ((i+1)%nRows,(j-1)%nCols),
    ((i-1)%nRows,j%nCols),
    ((i-1)%nRows,(j-1)%nCols),
    ((i-1)%nRows,(j+1)%nCols),
    ((i)%nRows,(j+1)%nCols),
    ((i)%nRows,(j-1)%nCols)]
    
    for neigh in neighbours:
        if matriz.item((neigh[0],neigh[1]))==1:
            count+=1
    return count
    

pygame.init()
# In[ ]:

play = True
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
while True:

    
    for event in pygame.event.get():
        #when the user clicks the close button
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        #iF THE SPCAE BAR IS PRESSED
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if play:
                    play = False
                else:
                    play = True
        if not play:
            click = pygame.mouse.get_pressed()
            if sum(click) > 0:
                pos = pygame.mouse.get_pos()
                i = pos[0] // heightPerRow
                j = pos[1] // widthPerCol
                i = int(i)
                j = int(j)
                if matrix.item((i,j)) == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1
                #time.sleep(0.1)


    for i in range(nRows):
        for j in range(nCols):
            if matrix.item((i,j))==1:
                pygame.draw.rect(screen, liveCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)))
            else:
                pygame.draw.rect(screen, deadCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)),  0)
    for i in range(nRows):
        for j in range(nCols):
            pygame.draw.rect(screen, liveCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)),1)

    pygame.display.flip()
    if play:
        newBoard = matrix.copy()
        for i in range(nRows):
            for j in range(nCols):
                if (vecinos(i,j,newBoard)<2 or vecinos(i,j,newBoard)>3) and newBoard.item((i,j))==1:
                    matrix[i][j]=0
                if (vecinos(i,j,newBoard)==3) and newBoard.item((i,j))==0:
                    matrix[i][j]=1
    time.sleep(0.05)
    #Empty the queue of events
    pygame.event.pump()
        
time.sleep(1)
pygame.quit()



