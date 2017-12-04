"""
play game you should run this file
"""
import pygame
from chess_class import Chess

pygame.init()
screen_size = [300, 300]
screen = pygame.display.set_mode(screen_size, 0, 32)
Action = ["up", "down", "left", "right"]

def get_chess_size():
    while True:
        chess_x, chess_y = map(int, raw_input("please your chess size like 4 4:").split())
        if chess_x < 3 and chess_y < 3:
            print("your input chess size is meaningless!")
        else:
            return [chess_x, chess_y]

def run(chess):
    chess.draw_chess()
    chess.game_start()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    action = Action[0]
                elif event.key == pygame.K_DOWN:
                    action = Action[1]
                elif event.key == pygame.K_LEFT:
                    action = Action[2]
                elif event.key == pygame.K_RIGHT:
                    action = Action[3]
                chess.step(action)
            
            if event.type == pygame.QUIT:
                chess.game_over()
                        
        chess.draw_chess()

if __name__ == "__main__":
    
    chess_size = get_chess_size()
    chess = Chess(chess_size, screen)
    run(chess) 
        
    
    
    


