import pygame
import sys
import time
from random import choice
import numpy as np

# Leeres Spielfeld
board = [ 9 for i in range(42)]


moves= 0 #?
won = False
countermin = 0
countermax = 0


# Variablen für pygame-Teil
x, y = 1024, 768
grey = 180,180,180
black = 0, 0, 0
blue = 0, 0, 180
dblue = 0, 0, 120
yellow = 180, 180, 0
dyellow = 150, 150, 0
red = 180, 0, 0
dred = 150, 0, 0

pygame.init()
screen = pygame.display.set_mode([x, y])
screen.fill(grey)

# Spielfeld zeichnen
pygame.draw.rect(screen, (blue), (144,132,740,636))
pygame.draw.rect(screen, (dblue), (144,132,740,636),10)

for xpos in range(212, 813, 100):
    for ypos in range (200, 701, 100):
        pygame.draw.circle(screen, (grey), (xpos,ypos), 45)
        pygame.draw.circle(screen, (dblue), (xpos,ypos), 50, 5)
        pygame.display.flip()
        
 

def chipnew():
    pygame.draw.circle(screen, (color), (xpos, 65), 40, 0)
    pygame.draw.circle(screen, (dcolor), (xpos, 65), 50, 10)
    pygame.display.flip()
    
def chipmove(x):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > 212:
                    pygame.draw.circle(screen, (grey), (x,65), 51, 0)
                    pygame.display.flip()
                    x -= 100
                    pygame.draw.circle(screen, (color), (x,65), 40, 0)
                    pygame.draw.circle(screen, (dcolor), (x,65), 50, 10)
                    pygame.display.flip()
                elif event.key == pygame.K_RIGHT and x < 812:
                    pygame.draw.circle(screen, (grey), (x,65), 51, 0)
                    pygame.display.flip()
                    x += 100
                    pygame.draw.circle(screen, (color), (x,65), 40, 0)
                    pygame.draw.circle(screen, (dcolor), (x,65), 50, 10)
                    pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    if board[int((x - 212) / 100)] == 9: # Zug gültig oder Spalte bereits komplett belegt
                        return x
                
def chipdrop(x, ye):
    pygame.draw.circle(screen, (grey), (x, 65), 51, 0)
    pygame.display.flip()
    for ypos in range (200, ye +  1, 100):
        pygame.draw.circle(screen, (color), (x, ypos), 40, 0)
        pygame.draw.circle(screen, (dcolor), (x, ypos), 45, 5)
        pygame.display.flip()
        if ypos != ye:
            pygame.time.wait(30)
            pygame.draw.circle(screen, (grey), (x, ypos), 45)
            pygame.display.flip()
            
            
# Zufälliger Computerzug
def randturn():
    available = []
    for i in range (7):
        if board[i] == 9:
            available.append(i)
    return choice(available)


#Funktion zum Prüfen ob es einen Sieger gibt   'O' Computer 
def Winmax():
    global countermax
    countermax += 1
    
   # Waagerecht alternativ
    for c in range(38, 2, -7):
        if board[c] == 0:
            if board[(c-3):c] == [0, 0, 0] or board[(c-2)] == board[(c-1)] == board[(c+1)] == 0 or board[(c-1)] == board[(c+1)] == board[(c+2)] == 0 or board[(c+1):(c+4)] == [0, 0, 0]:
                return 'O' 

    

    '''#waagerecht Reihe 6
    if board[38] == 1:
        if board[35:38] == [1,1,1] or board[36] == 1 and board[37]== 1  and board[39] == 1 or board[37]== 1  and board[39]== 1  and board[40] == 1 or board[39:42] == [1,1,1]:
            return 'X'
    if board[38] == 0:
        if board[35:38] == [0,0,0] or board[36] == 0 and board[37]== 0  and board[39] == 0 or board[37]== 0  and board[39]== 0  and board[40] == 0 or board[39:42] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 5
    if board[31] == 1:
        if board[28:31] == [1,1,1] or board[29] == 1 and board[30]== 1  and board[32] == 1 or board[30]== 1  and board[32]== 1  and board[33] == 1 or board[32:35] == [1,1,1]:
            return 'X'
    if board[31] == 0:
        if board[28:31] == [0,0,0] or board[29] == 0 and board[30]== 0  and board[32] == 0 or board[30]== 0  and board[32]== 0  and board[33] == 0 or board[32:35] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 4
    if board[24] == 1:
        if board[21:24] == [1,1,1] or board[22] == 1 and board[23]== 1  and board[25] == 1 or board[23]== 1  and board[25]== 1  and board[26] == 1 or board[25:28] == [1,1,1]:
            return 'X'
    if board[24] == 0:
        if board[21:24] == [0,0,0] or board[22] == 0 and board[23]== 0  and board[25] == 0 or board[23]== 0  and board[25]== 0  and board[26] == 0 or board[25:28] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 3
    if board[17] == 1:
        if board[14:17] == [1,1,1] or board[15] == 1 and board[16]== 1  and board[18] == 1 or board[16]== 1  and board[18]== 1  and board[19] == 1 or board[18:21] == [1,1,1]:
            return 'X'
    if board[17] == 0:
        if board[14:17] == [0,0,0] or board[15] == 0 and board[16]== 0  and board[18] == 0 or board[16]== 0  and board[18]== 0  and board[19] == 0 or board[18:21] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 2
    if board[10] == 1:
        if board[7:10] == [1,1,1] or board[8] == 1 and board[9]== 1  and board[11] == 1 or board[9]== 1  and board[11]== 1  and board[12] == 1 or board[11:14] == [1,1,1]:
            return 'X'
    if board[10] == 0:
        if board[7:10] == [0,0,0] or board[8] == 0 and board[9]== 0  and board[11] == 0 or board[9]== 0  and board[11]== 0  and board[12] == 0 or board[11:14] == [0,0,0]:
            return 'O'
  
    #waagerecht Reihe 1
    if board[3] == 1:
        if board[0:3] == [1,1,1] or board[1] == 1 and board[2] == 1 and board[4] == 1 or board[2] == 1 and board[4] == 1 and board[5] == 1 or board[4:7] == [1,1,1]:
            return 'X'
    if board[3] == 0:
        if board[0:3] == [0,0,0] or board[1] == 0 and board[2] == 0 and board[4] == 0 or board[2] == 0 and board[4] == 0 and board[5] == 0 or board[4:7] == [0,0,0]:
            return 'O'''
        


    
        
# SENKRECHT



    #senrecht alternativ
    for c in range(14, 21):
        
        if board[c] == 0 and board[c+7] == 0:
            if board[c-14] == 0 and board[c-7] == 0 or board[c-7] == 0 and board[c+14] == 0 or board[c+14] == 0 and board[c+21] == 0:
                return 'O'
        
    '''#senrecht Reihe 1
    if board[14] == 1 and board[21] == 1:
        if board[28] == 1:
            if board[35] == 1 or board[7] == 1:
                return 'X'
        if board[0] == 1 and board[7] == 1:
            return 'X'
        
    if board[14] == 0 and board[21] == 0:
        if board[28] == 0:
            if board[35] == 0 or board[7] == 0:
                return 'O'
        if board[0] == 0 and board[7] == 0:
            return 'O'
        
    #senrecht Reihe 2
    if board[15] == 1 and board[22] == 1:
        if board[29] == 1:
            if board[36] == 1 or board[8] == 1:
                return 'X'
        if board[1] == 1 and board[8] == 1:
            return 'X'
    if board[15] == 0 and board[22] == 0:
        if board[29] == 0:
            if board[36] == 0 or board[8] == 0:
                return 'O'
        if board[1] == 0 and board[8] == 0:
            return 'O'
        
    #senrecht Reihe 3
    if board[16] == 1 and board[23] == 1:
        if board[30] == 1:
            if board[37] == 1 or board[9] == 1:
                return 'X'
        if board[2] == 1 and board[9] == 1:
            return 'X'
    if board[16] == 0 and board[23] == 0:
        if board[30] == 0:
            if board[37] == 0 or board[9] == 0:
                return 'O'
        if board[2] == 0 and board[9] == 0:
            return 'O'
        
    # Senkrecht Reihe 4
    if board[17] == 1 and board[24] == 1:
        if board[31] == 1:
            if board[38] == 1 or board[10] == 1:
                return 'X'
        if board[3] == 1 and board[10] == 1:
            return 'X'
    if board[17] == 0 and board[24] == 0:
        if board[31] == 0:
            if board[38] == 0 or board[10] == 0:
                return 'O'
        if board[3] == 0 and board[10] == 0:
            return 'O'
        
    # Senkrecht Reihe 5
    if board[18] == 1 and board[25] == 1:
        if board[32] == 1:
            if board[39] == 1 or board[11] == 1:
                return 'X'
        if board[4] == 1 and board[11] == 1:
            return 'X'
    if board[18] == 0 and board[25] == 0:
        if board[32] == 0:
            if board[39] == 0 or board[11] == 0:
                return 'O'
        if board[4] == 0 and board[11] == 0:
            return 'O'
        
    # Senkrecht Reihe 6
    if board[19] == 1 and board[26] == 1:
        if board[33] == 1:
            if board[40] == 1 or board[12] == 1:
                return 'X'
        if board[5] == 1 and board[12] == 1:
            return 'X'
    if board[19] == 0 and board[26] == 0:
        if board[33] == 0:
            if board[40] == 0 or board[12] == 0:
                return 'O'
        if board[5] == 0 and board[12] == 0:
            return 'O'
        
    # Senkrecht Reihe 7
    if board[20] == 1 and board[27] == 1:
        if board[34] == 1:
            if board[41] == 1 or board[13] == 1:
                return 'X'
        if board[6] == 1 and board[13] == 1:
            return 'X'
    if board[20] == 0 and board[27] == 0:
        if board[34] == 0:
            if board[41] == 0 or board[13] == 0:
                return 'O'
        if board[6] == 0 and board[13] == 0:
            return 'O'''
        
#Diagonal
        
    #von links oben nach rechts unten
    
    
    if 0 == board[3] == board[11] == board[19] == board[27]:
        return 'O'
    
    
    if board[14] == 0 and board[22] == 0 and board[30] == 0 and board[38] == 0:
        return 'O'
    
    
    if board[10] == 0 and board[18] == 0 and board[26] == 0:
        if board[2] == 0 or board[34] == 0:
            return 'O'
        
    
    if board[15] == 0 and board[23] == 0 and board[31] == 0:
        if board[7] == 0 or board[39] == 0:
            return 'O'
        
    
    if board[17] == 0 and board[25] == 0:
        if board[9] == 0:
            if board[1] == 0 or board[33] == 0:
                return 'O'
        if board[33] == 0 and board[41] == 0:
            return 'O'
        
    
    if board[16] == 0 and board[24] == 0:
        if board[8] == 0:
            if board[0] == 0 or board[32] == 0:
                return 'O'
        if board[32] == 0 and board[40] == 0:
            return 'O'
        
    #von rechts oben nach links unten
        
    
    if board[3] == 0 and board[9] == 0 and board[15] == 0 and board[21] == 0:
        return 'O'
    
    
    if board[20] == 0 and board[26] == 0 and board[32] == 0 and board[38] == 0:
        return 'O'
    
    
    if board[10] == 0 and board[16] == 0 and board[22] == 0:
        if board[4] == 0 or board[28] == 0:
            return 'O'
        
    
    if board[19] == 0 and board[25] == 0 and board[31] == 0:
        if board[13] == 0 or board[37] == 0:
            return 'O'
        
    
    if board[17] == 0 and board[23] == 0:
        if board[11] == 0:
            if board[5] == 0 or board[29] == 0:
                return 'O'
        if board[29] == 0 and board[35] == 0:
            return 'O'
        
    
    if board[18] == 0 and board[24] == 0:
        if board[12] == 0:
            if board[6] == 0 or board[30] == 0:
                return 'O'
        if board[30] == 0 and board[36] == 0:
            return 'O'
    
    
    
    
    
    
    
    
    #Bonuszüge    
    '''if B1 == True:
        if board[31] == 9:
            if board[38] == 0:
                #B1 = False
                return 'OB'
            if board[38] == 1:
                #B1 = False
                return 'XB'
        
    if board[36] != 9 and board[22] == 9:
        if board[29] == 0:
            return 'OB'
        if board[29] == 1:
            return 'XB'''
    

    
            
    if 9 not in board:
        return 'U'
        
    return 'K'

#Funktion zum Prüfen ob es einen Sieger gibt  'X' Mensch  
def Winmin():
    global countermin
    countermin += 1
    
   # Waagerecht alternativ
    for c in range(38, 2, -7):
      
        if board[c] == 1:
            if board[(c-3):c] == [1, 1, 1] or board[(c-2)] == board[(c-1)] == board[(c+1)] == 1 or board[(c-1)] == board[(c+1)] == board[(c+2)] == 1 or board[(c+1):(c+4)] == [1, 1, 1]:
                return 'X'
    
           

    '''#waagerecht Reihe 6
    if board[38] == 1:
        if board[35:38] == [1,1,1] or board[36] == 1 and board[37]== 1  and board[39] == 1 or board[37]== 1  and board[39]== 1  and board[40] == 1 or board[39:42] == [1,1,1]:
            return 'X'
    if board[38] == 0:
        if board[35:38] == [0,0,0] or board[36] == 0 and board[37]== 0  and board[39] == 0 or board[37]== 0  and board[39]== 0  and board[40] == 0 or board[39:42] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 5
    if board[31] == 1:
        if board[28:31] == [1,1,1] or board[29] == 1 and board[30]== 1  and board[32] == 1 or board[30]== 1  and board[32]== 1  and board[33] == 1 or board[32:35] == [1,1,1]:
            return 'X'
    if board[31] == 0:
        if board[28:31] == [0,0,0] or board[29] == 0 and board[30]== 0  and board[32] == 0 or board[30]== 0  and board[32]== 0  and board[33] == 0 or board[32:35] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 4
    if board[24] == 1:
        if board[21:24] == [1,1,1] or board[22] == 1 and board[23]== 1  and board[25] == 1 or board[23]== 1  and board[25]== 1  and board[26] == 1 or board[25:28] == [1,1,1]:
            return 'X'
    if board[24] == 0:
        if board[21:24] == [0,0,0] or board[22] == 0 and board[23]== 0  and board[25] == 0 or board[23]== 0  and board[25]== 0  and board[26] == 0 or board[25:28] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 3
    if board[17] == 1:
        if board[14:17] == [1,1,1] or board[15] == 1 and board[16]== 1  and board[18] == 1 or board[16]== 1  and board[18]== 1  and board[19] == 1 or board[18:21] == [1,1,1]:
            return 'X'
    if board[17] == 0:
        if board[14:17] == [0,0,0] or board[15] == 0 and board[16]== 0  and board[18] == 0 or board[16]== 0  and board[18]== 0  and board[19] == 0 or board[18:21] == [0,0,0]:
            return 'O'
        
    #waagerecht Reihe 2
    if board[10] == 1:
        if board[7:10] == [1,1,1] or board[8] == 1 and board[9]== 1  and board[11] == 1 or board[9]== 1  and board[11]== 1  and board[12] == 1 or board[11:14] == [1,1,1]:
            return 'X'
    if board[10] == 0:
        if board[7:10] == [0,0,0] or board[8] == 0 and board[9]== 0  and board[11] == 0 or board[9]== 0  and board[11]== 0  and board[12] == 0 or board[11:14] == [0,0,0]:
            return 'O'
  
    #waagerecht Reihe 1
    if board[3] == 1:
        if board[0:3] == [1,1,1] or board[1] == 1 and board[2] == 1 and board[4] == 1 or board[2] == 1 and board[4] == 1 and board[5] == 1 or board[4:7] == [1,1,1]:
            return 'X'
    if board[3] == 0:
        if board[0:3] == [0,0,0] or board[1] == 0 and board[2] == 0 and board[4] == 0 or board[2] == 0 and board[4] == 0 and board[5] == 0 or board[4:7] == [0,0,0]:
            return 'O'''
        


    
        
# SENKRECHT



    #senrecht alternativ
    for c in range(14, 21):
        if board[c] == 1 and board[c+7] == 1:
            if board[c-14] == 1 and board[c-7] == 1 or board[c-7] == 1 and board[c+14] == 1 or board[c+14] == 1 and board[c+21] == 1:
                return 'X'
        
                
    '''#senrecht Reihe 1
    if board[14] == 1 and board[21] == 1:
        if board[28] == 1:
            if board[35] == 1 or board[7] == 1:
                return 'X'
        if board[0] == 1 and board[7] == 1:
            return 'X'
        
    if board[14] == 0 and board[21] == 0:
        if board[28] == 0:
            if board[35] == 0 or board[7] == 0:
                return 'O'
        if board[0] == 0 and board[7] == 0:
            return 'O'
        
    #senrecht Reihe 2
    if board[15] == 1 and board[22] == 1:
        if board[29] == 1:
            if board[36] == 1 or board[8] == 1:
                return 'X'
        if board[1] == 1 and board[8] == 1:
            return 'X'
    if board[15] == 0 and board[22] == 0:
        if board[29] == 0:
            if board[36] == 0 or board[8] == 0:
                return 'O'
        if board[1] == 0 and board[8] == 0:
            return 'O'
        
    #senrecht Reihe 3
    if board[16] == 1 and board[23] == 1:
        if board[30] == 1:
            if board[37] == 1 or board[9] == 1:
                return 'X'
        if board[2] == 1 and board[9] == 1:
            return 'X'
    if board[16] == 0 and board[23] == 0:
        if board[30] == 0:
            if board[37] == 0 or board[9] == 0:
                return 'O'
        if board[2] == 0 and board[9] == 0:
            return 'O'
        
    # Senkrecht Reihe 4
    if board[17] == 1 and board[24] == 1:
        if board[31] == 1:
            if board[38] == 1 or board[10] == 1:
                return 'X'
        if board[3] == 1 and board[10] == 1:
            return 'X'
    if board[17] == 0 and board[24] == 0:
        if board[31] == 0:
            if board[38] == 0 or board[10] == 0:
                return 'O'
        if board[3] == 0 and board[10] == 0:
            return 'O'
        
    # Senkrecht Reihe 5
    if board[18] == 1 and board[25] == 1:
        if board[32] == 1:
            if board[39] == 1 or board[11] == 1:
                return 'X'
        if board[4] == 1 and board[11] == 1:
            return 'X'
    if board[18] == 0 and board[25] == 0:
        if board[32] == 0:
            if board[39] == 0 or board[11] == 0:
                return 'O'
        if board[4] == 0 and board[11] == 0:
            return 'O'
        
    # Senkrecht Reihe 6
    if board[19] == 1 and board[26] == 1:
        if board[33] == 1:
            if board[40] == 1 or board[12] == 1:
                return 'X'
        if board[5] == 1 and board[12] == 1:
            return 'X'
    if board[19] == 0 and board[26] == 0:
        if board[33] == 0:
            if board[40] == 0 or board[12] == 0:
                return 'O'
        if board[5] == 0 and board[12] == 0:
            return 'O'
        
    # Senkrecht Reihe 7
    if board[20] == 1 and board[27] == 1:
        if board[34] == 1:
            if board[41] == 1 or board[13] == 1:
                return 'X'
        if board[6] == 1 and board[13] == 1:
            return 'X'
    if board[20] == 0 and board[27] == 0:
        if board[34] == 0:
            if board[41] == 0 or board[13] == 0:
                return 'O'
        if board[6] == 0 and board[13] == 0:
            return 'O'''
        
#Diagonal
        
    #von links oben nach rechts unten
    
    if 1 == board[3] == board[11] == board[19] == board[27]:
        return 'X'
    
    
    if board[14] == 1 and board[22] == 1 and board[30] == 1 and board[38] == 1:
        return 'X'
    
    
    if board[10] == 1 and board[18] == 1 and board[26] == 1:
        if board[2] == 1 or board[34] == 1:
            return 'X'
    
        
    if board[15] == 1 and board[23] == 1 and board[31] == 1:
        if board[7] == 1 or board[39] == 1:
            return 'X'
    
        
    if board[17] == 1 and board[25] == 1:
        if board[9] == 1:
            if board[1] == 1 or board[33] == 1:
                return 'X'
        if board[33] == 1 and board[41] == 1:
            return 'X'
    
        
    if board[16] == 1 and board[24] == 1:
        if board[8] == 1:
            if board[0] == 1 or board[32] == 1:
                return 'X'
        if board[32] == 1 and board[40] == 1:
            return 'X'
    
        
    #von rechts oben nach links unten
        
    if board[3] == 1 and board[9] == 1 and board[15] == 1 and board[21] == 1:
        return 'X'
    
    
    if board[20] == 1 and board[26] == 1 and board[32] == 1 and board[38] == 1:
        return 'X'
    
    
    if board[10] == 1 and board[16] == 1 and board[22] == 1:
        if board[4] == 1 or board[28] == 1:
            return 'X'
    
        
    if board[19] == 1 and board[25] == 1 and board[31] == 1:
        if board[13] == 1 or board[37] == 1:
            return 'X'
    
        
    if board[17] == 1 and board[23] == 1:
        if board[11] == 1:
            if board[5] == 1 or board[29] == 1:
                return 'X'
        if board[29] == 1 and board[35] == 1:
            return 'X'
    
        
    if board[18] == 1 and board[24] == 1:
        if board[12] == 1:
            if board[6] == 1 or board[30] == 1:
                return 'X'
        if board[30] == 1 and board[36] == 1:
            return 'X'
    
    
    
    
    
    
    
    
    
    #Bonuszüge    
    '''if B1 == True:
        if board[31] == 9:
            if board[38] == 0:
                #B1 = False
                return 'OB'
            if board[38] == 1:
                #B1 = False
                return 'XB'
        
    if board[36] != 9 and board[22] == 9:
        if board[29] == 0:
            return 'OB'
        if board[29] == 1:
            return 'XB'''
    

    
            
    if 9 not in board:
        return 'U'
        
    return 'K'



#Funktion für besten Computerzug
def bestTurn():
    bestScore = -10
    for i in order:
        if board[i] == 9:
            for j in range (35,-1,-7):
                if board[j+i] == 9:
                    board[j+i] = 0
                    break
            score = minimax(board,tiefe,False)
            board[j+i] = 9
            if score > bestScore:
                bestScore = score
                bestMove = i
                    
    return bestMove
    
scores = {'O' : 2, 'X' : -2, 'OB' : 1, 'XB' : -1, 'U' : 0}

def minimax(board,depth,maxi):
    if maxi:
        winner = Winmax()
    else:
        winner = Winmin()
        
    if winner != 'K':
        return scores[winner]
    #print (depth)
    if depth <=0:
        return 0
    
    if maxi:
        bestScore = -10
        for i in order:
            if board[i] == 9:
                for j in range (35,-1,-7):
                    if board[j+i] == 9:
                        board[j+i] = 0
                        break
                score = minimax(board,depth-1,False)
                board[j+i] = 9
                bestScore = max (score, bestScore)
                
        return bestScore
    else:
        bestScore = 10
        for i in order:
            if board[i] == 9:
                for j in range (35,-1,-7):
                    if board[j+i] == 9:
                        board[j+i] = 1
                        break
                score = minimax(board,depth-1,True)
                board[j+i] = 9
                bestScore = min(score, bestScore);
         
        return bestScore
    

 

while True:
    #Zug Mensch
    color = yellow
    dcolor = dyellow
    xpos = 512
    chipnew()
    xpos = chipmove(xpos)
        
    turnhuman = int((xpos-212)/100) # Wert für den Zug aus xpos errechnen : 0 - 6
    # Falltiefe des Chips
    end = 6
    for i in range (35,-1,-7):
        end -= 1
        if board[i+turnhuman] == 9:
            board[i+turnhuman] = 1
            yend = 100 * end +200
            move = 'c'
            moves +=1
            break
        
    chipdrop(xpos, yend)
    
    if Winmin() == 'X':
        fontObj = pygame.font.Font('freesansbold.ttf', 48)
        text = fontObj.render('Gelb gewinnt', True, (black))
        print ('Gelb gewinnt')
        break
    
    
    #Computerzug
    if moves < 15:
        tiefe = 7
    elif moves < 17:
        tiefe = 8
    elif moves < 19:
        tiefe = 9
    elif moves < 21:
        tiefe = 10
    elif moves < 23:
        tiefe = 11
    else:
        tiefe = 12
    
    fontObj = pygame.font.Font('freesansbold.ttf', 48)
    text = fontObj.render('calculating', True, (black))
    rect = text.get_rect()
    rect.center = (512, 66)
    screen.blit(text, rect)
    pygame.display.flip()
    
    color = red
    dcolor = dred
    
    # Reihenfolge der Suche
    order = [3,choice((2, 4))]
    order += [6 - order[1], choice((1, 5))]
    order += [6 - order[3], choice((0, 6))]
    order += [6 - order[5]]
    
    print(order)
    
    
    
    # Niederlage in einem Zug vermeiden? Erkennt die AI eine sichere Niederlage, macht sie den erstbesten Zug,
    # anstatt eine Niederlage in einem Zug zu vermeiden.
    #funktioniert nicht :(
    '''for i in order:
        if board[i] == 9:
            for j in range (35,-1,-7):
                if board[j+i] == 9:
                    board[j+i] = 1
                    break
            if Winmin() == 'X':    
                print('X')
                board[j+i] = 9
                turncomp = i
                won = True                
                break
            board[j+i] = 9'''
            
    #print (board)
    
    
    # Gewinn in einem Zug? Ansonsten macht die AI den erstbesten Zug der zum sicheren
    # Sieg führt, auch wenn dieser Sieg mehrere Züge in der Tiefe liegt.
    for i in order:
        if board[i] == 9:
            for j in range (35,-1,-7):
                if board[j+i] == 9:
                    board[j+i] = 0
                    break
            if Winmax() == 'O':
                print('O')
                board[j+i] = 9
                turncomp = i
                won = True                
                break
            board[j+i] = 9
            
            
    

    
    
    
    if won == False:
        t = time.time()
          
        turncomp = bestTurn()
        #turncomp = randturn()
        
        
        print (moves, tiefe, round(time.time() - t, 3), 'Sekunden')
        
        print (countermin)
        print (countermax)
        
        
    xpos = turncomp * 100 + 212
    
    pygame.draw.rect(screen, (grey), (300,40,424,50))
    pygame.display.flip()
    
    chipnew()
    pygame.time.delay(1000)
    
    
         
    # Chip einwerfen
    end = 6
    for i in range (35,-1,-7):
        end -= 1
        if board[i+turncomp] == 9:
            board[i+turncomp] = 0
            yend = 100 * end + 200
            break
    move = 'h'
    moves +=1  

          
    
        
    chipdrop(xpos, yend)
    
    if Winmax() == 'O':
        fontObj = pygame.font.Font('freesansbold.ttf', 48)
        text = fontObj.render('Rot gewinnt', True, (black))
        print ('Rot gewinnt')
        break
    
    if Winmax() == 'U':
        fontObj = pygame.font.Font('freesansbold.ttf', 48)
        text = fontObj.render('Unentschieden', True, (black))
        print ('Unentschieden')
        break
    
while True:
    rect = text.get_rect()
    rect.center = (512, 66)
    screen.blit(text, rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    

            
        
        
        
        
        
        
        
        
   