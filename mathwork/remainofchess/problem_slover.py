'''
for each different size of chess, which start position and which method based on the position can get maximum score or minimum remain of chess!
problem_solver file is to solve that problem
'''

import pygame
from chess_class import Chess


def search_up(chess, display):
    while chess.is_found[0]:
        chess.step("up")
        if display:
            chess.draw_chess()

def search_down(chess, display):
    while chess.is_found[1]:
        chess.step("down")
        if display:
            chess.draw_chess()

def search_left(chess, display):
    while chess.is_found[2]:
        chess.step("left")
        if display:
            chess.draw_chess()

def search_right(chess, display):
    while chess.is_found[3]:
        chess.step("right")
        if display:
            chess.draw_chess()

def get_game_score(chess, start_position, display=False):
    """
    display: display the screen or not
    """
    chess.game_start(start_position)
    chess.step("none")
    while True:
        search_right(chess, display)
        search_left(chess, display)
        search_down(chess, display)
        search_up(chess, display)
        if not any(chess.is_found):
            break
    score = chess.get_score()
    return score

def search_max_score(chess_size):
    """
    search all start position and get the max_score
    """
    max_score = 0
    for i in range(1,chess_size[0]+1):
        for j in range(1,chess_size[1]+1):
            chess = Chess(chess_size, print_info=False)
            score = get_game_score(chess, [i,j])
            if score > max_score:
                max_score = score
                start_position = [i,j]
    remain = chess_size[0]*chess_size[1] - max_score
    return start_position, remain

def display_result(chess_size, start_position):
    """
    after get the maximun score, display the process
    """
    pygame.init()
    screen_size = [300, 300]
    screen = pygame.display.set_mode(screen_size, 0, 32)
    chess = Chess(chess_size, screen, FPS=3)
    get_game_score(chess, start_position, display=True)
    
if __name__ == "__main__":
    
    chess_size = [5,5]
    start_position, remain = search_max_score(chess_size)   
    print "the remain of chess is %d" %(remain)
    display_result(chess_size, start_position)