class Founder:
    
    def __init__(self):
        pass
    
    def found(self, matrix, position):
        
        up_is_found, up_new_position = self.found_up(matrix, position)
        down_is_found, down_new_position = self.found_down(matrix, position)
        left_is_found, left_new_position = self.found_left(matrix, position)
        right_is_found, right_new_position = self.found_right(matrix, position)
        
        is_found = [up_is_found, down_is_found, left_is_found, right_is_found]
        new_position = [up_new_position, down_new_position, left_new_position, right_new_position]
        return is_found, new_position
        
    def found_up(self, matrix, position):
        start = position[1] - 1
        s = 0
        while start >= 0 and s < 2:
            if matrix[position[0], start] == 1:
                s += 1
            if s< 2:
                start -= 1
        if s==2:
            return True, [position[0], start]
        else:
            return False, []
        
    def found_down(self, matrix, position):
        chess_size = matrix.shape[1]
        start = position[1] + 1
        s = 0
        while start < chess_size and s < 2:
            if matrix[position[0], start] == 1:
                s += 1
            if s< 2:
                start += 1
        if s==2:
            return True, [position[0], start]
        else:
            return False, []
    
    def found_left(self, matrix, position):
        start = position[0] - 1
        s = 0
        while start >= 0 and s < 2:
            if matrix[start, position[1]] == 1:
                s += 1
            if s< 2:
                start -= 1
        if s==2:
            return True, [start, position[1]]
        else:
            return False, []
        
    def found_right(self, matrix, position):
        chess_size = matrix.shape[0]
        start = position[0] + 1
        s = 0
        while start < chess_size and s < 2:
            if matrix[start, position[1]] == 1:
                s += 1
            if s< 2:
                start += 1
        if s==2:
            return True, [start, position[1]]
        else:
            return False, []
    