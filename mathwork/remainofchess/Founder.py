"""
a definition of founder
it found four direction <up, down , left, right> of a chess, then return is founded and the new position 
"""
class Founder:
    
    def __init__(self):
        
        self.is_found  = []
        self.new_position = []
        
    def found(self, matrix, position):
        
        self.__init__()
        self.found_up(matrix, position)
        self.found_down(matrix, position)
        self.found_left(matrix, position)
        self.found_right(matrix, position)
        return self.is_found, self.new_position
    
    def found_up(self, matrix, position):
        start = position[1] - 1
        s = 0
        while start >= 0 and s < 2:
            if matrix[position[0], start] == 1:
                s += 1
            if s< 2:
                start -= 1
        if s==2:
            found, n_position = True, [position[0], start]
        else:
            found, n_position = False, []
        self.is_found.append(found)
        self.new_position.append(n_position)
        
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
            found, n_position = True, [position[0], start]
        else:
            found, n_position = False, []
        self.is_found.append(found)
        self.new_position.append(n_position)
        
    def found_left(self, matrix, position):
        start = position[0] - 1
        s = 0
        while start >= 0 and s < 2:
            if matrix[start, position[1]] == 1:
                s += 1
            if s< 2:
                start -= 1
        if s==2:
            found, n_position = True, [start, position[1]]
        else:
            found, n_position = False, []
        self.is_found.append(found)
        self.new_position.append(n_position)
        
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
            found, n_position = True, [start, position[1]]
        else:
            found, n_position = False, []
        self.is_found.append(found)
        self.new_position.append(n_position)
    