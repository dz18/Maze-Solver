
class Maze:
    '''
    Index Number Representation Guide
    ------------------------
    : 0 = blank space
    : 1 = wall
    : 2 = starting point
    : 3 = goal
    : 4 = path taken trail
    : 5 = visited path
    '''
    def __init__(self, dimensions = None):
        """
        Initializes the maze game

        board_size_width: The width of the board size
        board_size_height: The height of the board size
        """

        if dimensions is None:
            self.board = []
            self.board_type = None
            self.width = None
            self.height = None
            self.board_type = None
        else:
            self.width = dimensions[0]
            self.height = dimensions[1]
            self.board = self.set_board_size(dimensions)
            self.board_type = 'custom'

        self.start = None
        self.goal = None

    def set_start(self, coord):
        ''' Change the start coordinates '''
        x, y = coord[0], coord[1]

        # Reset original start coordinates to blank
        if self.start:
            self.board[self.start[0]][self.start[1]] = 0
            
        # Change start Coodinates
        self.start = coord
        self.board[x][y] = 2

    def set_goal(self, coord):
        ''' Change the goal coordinates '''
        x, y = coord[0], coord[1]

        # Reset original goal coordinates to blank
        if self.goal:
            self.board[self.goal[0]][self.goal[1]] = 0
            
        # Change Goal Coodinates
        self.goal = coord
        self.board[x][y] = 3

    def set_size_small(self):
        ''' Set the board size to 32x15 '''
        dimension = (32, 15)
        self.set_board_size(dimension)
        self.board_type = 'small'

    def set_size_large(self):
        ''' Set the board size to 64x30 '''
        dimension = (64, 30)
        self.set_board_size(dimension)
        self.board_type = 'large'

    def set_board_size(self, dimensions):
        ''' Sets the board with a given set of dimensions'''

        board = []
        for row in range(0, dimensions[1]):
            board.append([])
            for _ in range(0, dimensions[0]):
                board[row].append(0)

        # Update Attributes
        self.board = board
        self.width = dimensions[0]
        self.height = dimensions[1]

        # Return new board        
        return board
    
    def remove_start(self):
        ''' Remove the start coordinates and set it to a blank '''
        x, y = self.start[0], self.start[1]
        self.board[x][y] = 0

    def remove_goal(self):
        ''' Remove the goal coordinates and set it to a blank '''
        x, y = self.goal[0], self.goal[1]
        self.board[x][y] = 0
            
    def use_default_maze(self, map):
        ''' Give the user an option to use 3 default maze maps
            based on the board type 
        '''

        if self.board_type == 'small':
            if map == 1:
                self.board = [[1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1]]
                self.start = (0, 1)
                self.end = (14, 30)
            if map == 2:
                pass
            if map == 3:
                pass

        if self.board == 'large':
            if map == 1:
                pass
            if map == 2:
                pass
            if map == 3:
                pass
            
    def reset_board(self):
        ''' Clear the board of all components. Board returns as all blank'''

        for row in range(0, self.height):
            for col in range(0, self.width):
                if self.board[row][col] != 0:
                    self.board[row][col] = 0

        self.start = None
        self.goal = None

    def show_board(self):
        ''' Print the board into the terminal '''

        print('=' * 100)
        for row in range(len(self.board)):
            print(self.board[row])