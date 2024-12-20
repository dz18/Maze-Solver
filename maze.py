'''
Index Number Representation Guide
------------------------
0 = blank space
1 = wall
2 = starting point
3 = goal
4 = your trail
'''

class Maze:
    '''
    Creates a Maze Board

    param p1: lalalaa
    '''
    def __init__(self, board_size_width = None, board_size_height = None):
        self.width = board_size_width
        self.height = board_size_height

        # Initialize board size
        if board_size_width is None or board_size_height is None:
            self.board = []
        else:
            board = []
            for i in range(0, board_size_height):
                board.append([])
                for _ in range(0, board_size_width):
                    board[i].append(0)
            self.board = board

        # Example: Start at (0,0) and the goal is at (10,10). 
        self.start = None
        self.goal = None
