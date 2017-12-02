import numpy as np

def found_up(chess_matrix, pao_position):
    start = pao_position[1] - 1
    s = 0
    while start >= 0 and s < 2:
        if chess_matrix[pao_position[0], start] == 1:
            s += 1
        if s< 2:
            start -= 1
    if s==2:
        return True, [pao_position[0], start]
    else:
        return False, []
    
def found_down(chess_matrix, pao_position):
    CHESS_SIZE = chess_matrix.shape[0]
    start = pao_position[1] + 1
    s = 0
    while start < CHESS_SIZE and s < 2:
        if chess_matrix[pao_position[0], start] == 1:
            s += 1
        if s< 2:
            start += 1
    if s==2:
        return True, [pao_position[0], start]
    else:
        return False, []

def found_left(chess_matrix, pao_position):
    start = pao_position[0] - 1
    s = 0
    while start >= 0 and s < 2:
        if chess_matrix[start, pao_position[1]] == 1:
            s += 1
        if s< 2:
            start -= 1
    if s==2:
        return True, [start, pao_position[1]]
    else:
        return False, []
    
def found_right(chess_matrix, pao_position):
    CHESS_SIZE = chess_matrix.shape[0]
    start = pao_position[0] + 1
    s = 0
    while start < CHESS_SIZE and s < 2:
        if chess_matrix[start, pao_position[1]] == 1:
            s += 1
        if s< 2:
            start += 1
    if s==2:
        return True, [start, pao_position[1]]
    else:
        return False, []
    
if __name__ == "__main__":
    chess_matrix = np.ones([4,4])
    pao_position = (0,2)
    is_found, start  = found_up(chess_matrix, pao_position)
    print is_found, start