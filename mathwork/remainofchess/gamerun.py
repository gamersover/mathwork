import numpy as np
import pygame
from pygame import *
import sys
from check_function import found_up, found_down, found_left, found_right

def draw_chess(chess_matrix):
    for i in range(CHESS_SIZE):
        for j in range(CHESS_SIZE):
            if chess_matrix[i][j] == 2:
                pygame.draw.circle(screen, BLACK, [RADIUS + i*2*RADIUS, RADIUS + j*2*RADIUS] , RADIUS/2, 0)
            elif chess_matrix[i][j] == 1:
                pygame.draw.circle(screen, BLACK, [RADIUS + i*2*RADIUS, RADIUS + j*2*RADIUS] , RADIUS/2, 2)

def update_matrix(chess_matrix, pao_place, new_place, FLAG):
    chess_matrix[tuple(pao_place)]  = 0
    pao_place = new_place
    chess_matrix[tuple(pao_place)] = 2
    FLAG = [0, 0, 0, 0]
    return chess_matrix, pao_place, FLAG

pygame.init()
WHITE = [255,255,255]
BLACK = [    0,    0,    0]
CHESS_SIZE = 4
SCREEN_SIZE = [300, 300]
RADIUS = SCREEN_SIZE[0]/(CHESS_SIZE*2)

FLAG = [0, 0, 0, 0]  #up, down, left, right 
screen  = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

chess_matrix = np.ones([CHESS_SIZE, CHESS_SIZE])

pygame.display.set_caption("chess play")
screen.fill(WHITE)

draw_chess(chess_matrix)
pygame.display.update()
y,x = map(int, raw_input("please select your start position:").split())
# x,y = 1,2
print "game start"
pao_place = [x,y]
chess_matrix[tuple(pao_place)] = 2

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #pao_place[1] ,0   if the second is 1 then found  if cant found the second 1  then not found
            if event.key  == K_UP:
                FLAG[0] = 1 
                is_found, new_place = found_up(chess_matrix, pao_place)
                if is_found:
                    chess_matrix, pao_place, FLAG = update_matrix(chess_matrix, pao_place, new_place, FLAG)
                else:
                    print "warning: up is not permission!"
    
            elif event.key  == K_DOWN:
                FLAG[1] = 1
                is_found, new_place = found_down(chess_matrix, pao_place)
                if is_found:
                    chess_matrix, pao_place, FLAG = update_matrix(chess_matrix, pao_place, new_place, FLAG)
                else:
                    print "warning: down is not permission!"                
                
            elif event.key == K_LEFT:
                FLAG[2] = 1
                is_found, new_place = found_left(chess_matrix, pao_place)
                if is_found:
                    chess_matrix, pao_place, FLAG = update_matrix(chess_matrix, pao_place, new_place, FLAG)
                else:
                    print "warning: left is not permission!"

            elif event.key == K_RIGHT:
                FLAG[3] = 1
                is_found, new_place = found_right(chess_matrix, pao_place)
                if is_found:
                    chess_matrix, pao_place, FLAG = update_matrix(chess_matrix, pao_place, new_place, FLAG)
                else:
                    print "warning: right is not permission!"
                
        if all(FLAG):
            left = np.sum(chess_matrix) - 1
            score = CHESS_SIZE**2 - left
            print "game is over!"
            print "you score is {}".format(int(score))
            sys.exit()           
        
        if event.type == QUIT:
            sys.exit()
    screen.fill(WHITE)
    draw_chess(chess_matrix)
    pygame.display.update()


