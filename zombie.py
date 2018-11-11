"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)] 
                       for dummy_row in range(self._grid_height)]
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
        return

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)  
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if not self.is_empty(row, col):
                    visited.set_full(row, col)
        
        distance_field = []
        
        boundary = poc_queue.Queue()        
        if entity_type == ZOMBIE:
            for zombie in self._zombie_list:
                boundary.enqueue(zombie)
                distance_field = [[self._grid_width * self._grid_height for col in range(self._grid_width)] 
                               for row in range(self._grid_height)]
        elif entity_type == HUMAN:
            for human in self._human_list:
                boundary.enqueue(human)
                distance_field = [[self._grid_width * self._grid_height for col in range(self._grid_width)] 
                               for row in range(self._grid_height)]
            
        for item in boundary:
            visited.set_full(item[0], item[1])
            distance_field[item[0]][item[1]] = 0
        
        while boundary:
            removed = boundary.dequeue()
            for neighbor in visited.four_neighbors(removed[0], removed[1]):
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue([neighbor[0], neighbor[1]])
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[removed[0]][removed[1]] + 1
                    
        return distance_field
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        new_human_list = []
        for human in self.humans():
            temp_list = [human]
            temp_list_value = []
            for neighbor in self.eight_neighbors(human[0], human[1]):
                temp_list.append(neighbor)
            for possible_moves in temp_list:
                if zombie_distance[possible_moves[0]][possible_moves[1]] != self._grid_width * self._grid_height:
                    temp_list_value.append(zombie_distance[possible_moves[0]][possible_moves[1]])
            maxy = max(temp_list_value)
            listy = []
            for move in temp_list:
                if zombie_distance[move[0]][move[1]] == maxy:
                    listy.append(move)
            new_human_list.append(listy[-1])
        self._human_list = new_human_list   
                                    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        new_zombie_list = []
        for zombie in self.zombies():
            temp_list = [zombie]
            temp_list_value = []
            for neighbor in self.four_neighbors(zombie[0], zombie[1]):
                temp_list.append(neighbor)
            for possible_moves in temp_list:
                temp_list_value.append(human_distance[possible_moves[0]][possible_moves[1]])
            miny = min(temp_list_value)
            listy = []
            for move in temp_list:
                if human_distance[move[0]][move[1]] == miny:
                    listy.append(move)
            new_zombie_list.append(listy[-1])
        self._zombie_list = new_zombie_list 
                    
poc_zombie_gui.run_gui(Zombie(20, 30))