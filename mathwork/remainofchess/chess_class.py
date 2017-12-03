import numpy as np
import pygame
from Founder import Founder
import sys
BLACK = [    0,    0,    0]
WHITE = [255,255,255]


class Chess:
    
    def __init__(self, chess_size, screen):
        
        self.chess_size_y = chess_size[0]
        self.chess_size_x = chess_size[1]
        self.chess_matrix = np.ones([self.chess_size_x, self.chess_size_y])
        self.screen = screen
        
        screen_size = self.screen.get_size()
        self.radius_y = screen_size[0]/chess_size[0]
        self.radius_x = screen_size[1]/chess_size[1]
        self.radius = min(self.radius_x, self.radius_y)/4
        
        self.flag = [0 ,0 ,0 ,0]
        self.founder = Founder()   #new a Founder obj
   
    def draw_chess(self):
        
        self.screen.fill(WHITE)
        for i in range(self.chess_size_x):
            for j in range(self.chess_size_y):
                if self.chess_matrix[i][j] == 1:
                    pygame.draw.circle(self.screen, BLACK, [self.radius_x/2 + i*self.radius_x, self.radius_y/2 + j*self.radius_y], self.radius, 2)
                elif self.chess_matrix[i][j] == 2:
                    pygame.draw.circle(self.screen, BLACK, [self.radius_x/2 + i*self.radius_x, self.radius_y/2 + j*self.radius_y], self.radius, 0)
        pygame.display.update()
    
    def game_start(self):
        
        self.start_y, self.start_x = map(int, raw_input("please input your start position like 1 2:").split())
        self.start_position = [self.start_x-1, self.start_y-1]
        self.chess_matrix[tuple(self.start_position)] = 2
        print "game start"
        self.draw_chess()
    
    def step(self, action):
        
        #jugement flag is all 1 then game is over
        if all(self.flag):
            score = self.get_score()
            print "game over and your final score is %d" %(score) 
            sys.exit()
        else:
            if action == "up":
                self.flag[0] = 1
                is_found, new_position = self.founder.found_up(self.chess_matrix, self.start_position)
                if is_found:
                    self.update_matrix(new_position)
                else:
                    print "warning:up is not permission!"
                    
            elif action == "down":
                self.flag[1] = 1
                is_found, new_position = self.founder.found_down(self.chess_matrix, self.start_position)
                if is_found:
                    self.update_matrix(new_position)
                else:
                    print "warning:down is not permission!"
                
            elif action == "left":
                self.flag[2] = 1
                is_found, new_position = self.founder.found_left(self.chess_matrix, self.start_position)
                if is_found:
                    self.update_matrix(new_position)
                else:
                    print "warning:left is not permission!"
                
            elif action == 'right':
                self.flag[3] = 1
                is_found, new_position = self.founder.found_right(self.chess_matrix, self.start_position)
                if is_found:
                    self.update_matrix(new_position)
                else:
                    print "warning:right is not permission!"
    
    def update_matrix(self, new_position):
        self.chess_matrix[tuple(self.start_position)] = 0
        self.start_position = new_position
        self.chess_matrix[tuple(self.start_position)] = 2
        self.flag = [0, 0, 0, 0]    
    
    def get_score(self):
        remain = np.sum(self.chess_matrix) - 1
        score = self.chess_size_x*self.chess_size_y - remain
        return score