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
    


# In[ ]:


screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
while True:
    pygame.event.pump()
    count = 0
    for i in range(nRows):
        for j in range(nCols):
            if matrix.item((i,j))==1:
                pygame.draw.rect(screen, liveCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)))
                count=1
            else:
                pygame.draw.rect(screen, deadCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)),  0)
    for i in range(nRows):
        for j in range(nCols):
            pygame.draw.rect(screen, liveCellColor, pygame.Rect(heightPerRow*i, widthPerCol*j, heightPerRow*(i+1), widthPerCol*(j+1)),1)
    pygame.display.flip()
    newBoard = matrix.copy()
    for i in range(nRows):
        for j in range(nCols):
            if (vecinos(i,j,newBoard)<2 or vecinos(i,j,newBoard)>3) and newBoard.item((i,j))==1:
                matrix[i][j]=0
            if (vecinos(i,j,newBoard)==3) and newBoard.item((i,j))==0:
                matrix[i][j]=1
    if count==0:
        break
    time.sleep(0.05)
time.sleep(1)
pygame.quit()


# In[3]:


vecinos(1,1,matrix)


# In[ ]:




