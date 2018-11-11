"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def slide(line):
    '''
    slides the given row to the front(front = left)
    '''
    temp = []
    for tile in range(len(line)):
        if line[tile] != 0:
            temp.append(line[tile])
    temp += ([0] * (len(line) - len(temp)))
    return temp
    
def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    temp = slide(line)    
    start = 0
    for tile in range(1, len(temp)):
        if temp[start] == temp[tile]:
            temp[start] *= 2
            temp[tile] = 0
        start = tile
    temp = slide(temp)
    return temp  

def reverse(listy):
    '''
    reverse a list
    '''
    listy.reverse()
    return listy

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = [0]
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [0] * (self._height * self._width)
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string = ''
        for row in range(self._height):
            string += str(self._grid[self._width*row:self._width*(row+1)])
            string += '\n'
        return string

    def tile(self, row, col):
        '''
        get the tile number for corrosponding row and col
        '''
        return (row * self._width) + col
       
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        temp_list = list(self._grid)
        if direction == LEFT:
            for row in range(self._height):
                temp_list[self._width*row:self._width*(row+1)] = merge(temp_list[self._width*row:self._width*(row+1)])
        elif direction == RIGHT:
            for row in range(self._height):
                temp_list[self._width*row:self._width*(row+1)] = reverse(temp_list[self._width*row:self._width*(row+1)])
                temp_list[self._width*row:self._width*(row+1)] = merge(temp_list[self._width*row:self._width*(row+1)])
                temp_list[self._width*row:self._width*(row+1)] = reverse(temp_list[self._width*row:self._width*(row+1)])       
        elif direction == UP:
            for col in range(self._width):
                temp2 = []
                for row in range(self._height):
                    temp2.append(temp_list[self.tile(row, col)])
                temp2 = merge(temp2)
                for row in range(self._height):
                    temp_list[self.tile(row, col)] = temp2[row]
        elif direction == DOWN:
            for col in range(self._width):
                temp2 = []
                for row in range(self._height - 1, -1, -1):
                    temp2.append(temp_list[self.tile(row, col)])
                temp2 = merge(temp2)
                temp2.reverse()
                for row in range(self._height):
                    temp_list[self.tile(row, col)] = temp2[row]
        
        changed = 1
        if self._grid == temp_list:
            changed = 0
        if changed:
            self._grid = temp_list
            self.new_tile()
           
    def get_empty_squares(self):
        '''
        returns a list of indices which have value = 0
        '''
        listy = []
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[self.tile(row, col)] == 0:
                    listy.append([row, col])
        return listy
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile = random.choice(self.get_empty_squares())
        self.set_tile(tile[0], tile[1], random.choice([2] * 9 + [4]))

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[self.tile(row, col)] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[self.tile(row, col)]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
