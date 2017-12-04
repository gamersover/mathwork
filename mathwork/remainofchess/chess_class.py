"""
a implementation of chess class
"""
import numpy as np
import pygame
from Founder import Founder
import sys

BLACK = [    0,    0,    0]
WHITE = [255,255,255]
fpsclock = pygame.time.Clock()

class Chess:
    
    def __init__(self, chess_size, screen=None, print_info=True, FPS=60):
        """
        chess_size:  the size of chess
        screen: if it has screen then display screen, else just dont display screen
        print_info: print the warning info or not
        FPS: the fps of the game
        """
        self.print_info = print_info
        self.FPS = FPS
        self.chess_size_y = chess_size[0]
        self.chess_size_x = chess_size[1]
        self.chess_matrix = np.ones([self.chess_size_x, self.chess_size_y])
        self.screen = screen
        if self.screen:
            screen_size = self.screen.get_size()
            self.radius_y = screen_size[0]/chess_size[0]
            self.radius_x = screen_size[1]/chess_size[1]
            self.radius = min(self.radius_x, self.radius_y)/4

        self.founder = Founder()
   
    def draw_chess(self):
        
        self.screen.fill(WHITE)
        for i in range(self.chess_size_x):
            for j in range(self.chess_size_y):
                if self.chess_matrix[i][j] == 1:
                    pygame.draw.circle(self.screen, BLACK, [self.radius_x/2 + i*self.radius_x, self.radius_y/2 + j*self.radius_y], self.radius, 2)
                elif self.chess_matrix[i][j] == 2:
                    pygame.draw.circle(self.screen, BLACK, [self.radius_x/2 + i*self.radius_x, self.radius_y/2 + j*self.radius_y], self.radius, 0)
        pygame.display.update()
        fpsclock.tick(self.FPS)
    
    def game_start(self, start_position=None):
        
        if start_position:
            self.start_position = [start_position[1]-1, start_position[0]-1]
            self.chess_matrix[tuple(self.start_position)] = 2
        else:
            while True:
                start_y, start_x = map(int, raw_input("please input your start position like 1 2:").split())
                if 1 <= start_x <= self.chess_size_x and 1 <= start_y <= self.chess_size_y: 
                    self.start_position = [start_x-1, start_y-1]
                    break
                else:
                    print "your input position is meaningless!"
            self.chess_matrix[tuple(self.start_position)] = 2
            print "game start"
            self.draw_chess()
            
    def game_over(self):
        
        score = self.get_score()
        if self.screen:
            print "game over and your final score is %d" %(score) 
            sys.exit()
    
    def step(self, action):
        
        self.check_terminal()
        if not any(self.is_found):
            self.game_over()
        else:
            if action == "up":
                if self.is_found[0]:
                    self.update_matrix(self.new_position[0])
                else:
                    if self.print_info:
                        print "warning:up is not permission!"
                    
            elif action == "down":
                if self.is_found[1]:
                    self.update_matrix(self.new_position[1])
                else:
                    if self.print_info:
                        print "warning:down is not permission!"
                
            elif action == "left":
                if self.is_found[2]:
                    self.update_matrix(self.new_position[2])
                else:
                    if self.print_info:
                        print "warning:left is not permission!"
                
            elif action == 'right':
                if self.is_found[3]:
                    self.update_matrix(self.new_position[3])
                else:
                    if self.print_info:
                        print "warning:right is not permission!"
    
    def update_matrix(self, new_position):
        self.chess_matrix[tuple(self.start_position)] = 0
        self.start_position = new_position
        self.chess_matrix[tuple(self.start_position)] = 2 
    
    def get_score(self):
        remain = np.sum(self.chess_matrix) - 1
        score = self.chess_size_x*self.chess_size_y - remain
        return score
    
    def check_terminal(self):
        self.is_found, self.new_position = self.founder.found(self.chess_matrix, self.start_position)
    