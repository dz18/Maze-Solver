import pygame as py
from modules.maze import Maze

WIDTH = 1280
HEIGHT = 720

# pygame setup
py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
running = True
font = py.font.SysFont('Comic Sans MS', 16)
middle_click = 'start'
py.display.set_caption("Maze Game AI Solver")

# Grid Colors: index corresponds with cell type
cell_colors = [
    (255, 255, 255), # WHITE: blank
    (0, 0, 0), # BLACK: wall
    (0, 0, 255), # BLUE: start
    (0, 255, 0), # GREEN: goal 
    (180, 255, 255), # LIGHT CYAN: Explored
    (255, 0, 0), # RED: Path to Goal
]
active_button_color = (100, 100, 100)

# Cell Sizes
SMALL_CELL = 40 # Board Size 32x15
LARGE_CELL = 20 # Board Size 64x30

# Initialize Maze
maze = Maze() # Default board size
maze.set_size_small()
cell_size = SMALL_CELL

def play(): # Play Screen
    ''''''
    # Draw Functions Bar
    py.draw.rect(screen, 'grey', py.Rect(0, 0, WIDTH, 120))

    def draw_legend():
        blank = py.draw.rect(screen, cell_colors[0], py.Rect(10, 10, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(10, 10, 30, 30), 2)
        text = font.render('0', True, 'black')
        text_rec = text.get_rect(center=blank.center)
        screen.blit(text, text_rec)
        text = font.render('Blank (Right Click)', True, 'black')
        text_x = blank.right + 5
        text_y = blank.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        wall = py.draw.rect(screen, cell_colors[1], py.Rect(10, 45, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(10, 45, 30, 30), 2)
        text = font.render('1', True, 'white')
        text_rec = text.get_rect(center=wall.center)
        screen.blit(text, text_rec)
        text = font.render('Wall (Left Click)', True, 'black')
        text_x = wall.right + 5
        text_y = wall.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        start = py.draw.rect(screen, cell_colors[2], py.Rect(10, 80, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(10, 80, 30, 30), 2)
        text = font.render('2', True, 'white')
        text_rec = text.get_rect(center=start.center)
        screen.blit(text, text_rec)
        text = font.render('Start (Middle Click)', True, 'black')
        text_x = start.right + 5
        text_y = start.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        x = text_rec.right + 20

        goal = py.draw.rect(screen, cell_colors[3], py.Rect(x, 10, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 10, 30, 30), 2)
        text = font.render('3', True, 'black')
        text_rec = text.get_rect(center=goal.center)
        screen.blit(text, text_rec)
        text = font.render('Goal (Middle Click)', True, 'black')
        text_x = goal.right + 5
        text_y = goal.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        return_x = text_rec.right

        goal = py.draw.rect(screen, cell_colors[4], py.Rect(x, 45, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 30, 30), 2)
        text = font.render('4', True, 'black')
        text_rec = text.get_rect(center=goal.center)
        screen.blit(text, text_rec)
        text = font.render('Explored', True, 'black')
        text_x = goal.right + 5
        text_y = goal.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        goal = py.draw.rect(screen, cell_colors[5], py.Rect(x, 80, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 80, 30, 30), 2)
        text = font.render('5', True, 'white')
        text_rec = text.get_rect(center=goal.center)
        screen.blit(text, text_rec)
        text = font.render('Path', True, 'black')
        text_x = goal.right + 5
        text_y = goal.centery
        text_rec = text.get_rect(left=text_x, centery=text_y)
        screen.blit(text, text_rec)

        return return_x

    def draw_divider(x):
        x += 20
        line = py.draw.line(screen, 'darkgrey', (x, 10), (x, 110), 2)
        return line.right
    
    def draw_AI_controls(x):
        x += 20

        solve_maze = py.draw.rect(screen, 'lightgrey', py.Rect(x, 10, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 10, 100, 30), 2)
        text = font.render('Solve Maze', True, 'black')
        text_rec = text.get_rect(center=solve_maze.center)
        screen.blit(text, text_rec)

        show_steps = py.draw.rect(screen, 'lightgrey', py.Rect(x, 45, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 100, 30), 2)
        text = font.render('Show Steps', True, 'black')
        text_rec = text.get_rect(center=show_steps.center)
        screen.blit(text, text_rec)
        
        previous_step = py.draw.rect(screen, 'lightgrey', py.Rect(x, 80, 48, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 80, 48, 30), 2)
        text = font.render('<-', True, 'black')
        text_rec = text.get_rect(center=previous_step.center)
        screen.blit(text, text_rec)

        next_step = py.draw.rect(screen, 'lightgrey', py.Rect(previous_step.right + 5, 80, 48, 30))
        py.draw.rect(screen, 'black', py.Rect(previous_step.right + 5, 80, 48, 30), 2)
        text = font.render('->', True, 'black')
        text_rec = text.get_rect(center=next_step.center)
        screen.blit(text, text_rec)

        x = next_step.right
        AI_controls = [solve_maze, show_steps, previous_step, next_step]

        return x, AI_controls
        
    def draw_settings(x, middle_click):
        x += 20

        color = 'lightgrey'
        if middle_click == 'start':
           color = active_button_color
        start = py.draw.rect(screen, color, py.Rect(x, 45, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 100, 30), 2)
        text = font.render('Middle Click:', True, 'black')
        text_rec = text.get_rect(left=start.left, bottom=start.top - 5)
        screen.blit(text, text_rec)
        text = font.render('Start', True, 'black')
        text_rec = text.get_rect(center=start.center)
        screen.blit(text, text_rec)

        color = 'lightgrey'
        if middle_click == 'goal':
            color = active_button_color
        goal = py.draw.rect(screen, color, py.Rect(x, 80, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 80, 100, 30), 2)
        text = font.render('Goal', True, 'black')
        text_rec = text.get_rect(center=goal.center)
        screen.blit(text, text_rec)

        x = goal.right + 20

        color = 'lightgrey'
        if maze.board_type == 'small':
            color = active_button_color
        small = py.draw.rect(screen, color, py.Rect(x, 45, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 100, 30), 2)
        text = font.render('Board Size:', True, 'black')
        text_rec = text.get_rect(left=small.left, bottom=small.top - 5)
        screen.blit(text, text_rec)
        text = font.render('Small', True, 'black')
        text_rec = text.get_rect(center=small.center)
        screen.blit(text, text_rec)

        color = 'lightgrey'
        if maze.board_type == 'large':
            color = active_button_color
        large = py.draw.rect(screen, color, py.Rect(x, 80, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 80, 100, 30), 2)
        text = font.render('Large', True, 'black')
        text_rec = text.get_rect(center=large.center)
        screen.blit(text, text_rec)

        x = large.right + 20

        default_board_1 = py.draw.rect(screen, 'lightgrey', py.Rect(x, 45, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 30, 30), 2)
        text = font.render('Default Boards:', True, 'black')
        text_rec = text.get_rect(left=default_board_1.left, bottom=default_board_1.top - 5)
        screen.blit(text, text_rec)
        text = font.render('1', True, 'black')
        text_rec = text.get_rect(center=default_board_1.center)
        screen.blit(text, text_rec)

        x = default_board_1.right + 10

        default_board_2 = py.draw.rect(screen, 'lightgrey', py.Rect(x, 45, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 30, 30), 2)
        text = font.render('2', True, 'black')
        text_rec = text.get_rect(center=default_board_2.center)
        screen.blit(text, text_rec)

        x = default_board_2.right + 10

        default_board_3 = py.draw.rect(screen, 'lightgrey', py.Rect(x, 45, 30, 30))
        py.draw.rect(screen, 'black', py.Rect(x, 45, 30, 30), 2)
        text = font.render('3', True, 'black')
        text_rec = text.get_rect(center=default_board_3.center)
        screen.blit(text, text_rec)

        settings = [
            start, 
            goal, 
            small, 
            large,
            default_board_1,
            default_board_2,
            default_board_3
        ]

        return settings

    def draw_manage_state():

        # State Management Buttons
        clear_maze = py.draw.rect(screen, 'lightgrey', py.Rect(WIDTH - 110, 10, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(WIDTH - 110, 10, 100, 30), 2)
        text = font.render('Clear Maze', True, 'black')
        text_rec = text.get_rect(center=clear_maze.center)
        screen.blit(text, text_rec)
        
        load_maze = py.draw.rect(screen, 'lightgrey', py.Rect(WIDTH - 110, 45, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(WIDTH - 110, 45, 100, 30), 2)
        text = font.render('Load Maze', True, 'black')
        text_rec = text.get_rect(center=load_maze.center)
        screen.blit(text, text_rec)

        save_maze = py.draw.rect(screen, 'lightgrey', py.Rect(WIDTH - 110, 80, 100, 30))
        py.draw.rect(screen, 'black', py.Rect(WIDTH - 110, 80, 100, 30), 2)
        text = font.render('Save Maze', True, 'black')
        text_rec = text.get_rect(center=save_maze.center)
        screen.blit(text, text_rec)

        x = save_maze.left - 20
        py.draw.line(screen, 'darkgrey', (x, 10), (x, 110), 2)

        return [
            clear_maze,
            load_maze,
            save_maze
        ]

    def draw_grid():
        for row in range(maze.height):
            for col in range(maze.width):
                cell_color = cell_colors[maze.board[row][col]]
                cell_rect = py.Rect(col * cell_size, 120 + row * cell_size, cell_size, cell_size)
                py.draw.rect(screen, cell_color, cell_rect)
                py.draw.rect(screen, 'black', cell_rect, 1)

    x = draw_legend()
    x = draw_divider(x)
    x, AI_controls = draw_AI_controls(x)
    x = draw_divider(x)
    settings = draw_settings(x, middle_click)
    manage_state = draw_manage_state()
    draw_grid()

    return AI_controls, settings, manage_state

def load_maze(): # Load Maze
    ''''''

while running:
    
    screen.fill("white")

    AI_controls, settings, manage_state = play()

    py.display.flip()

    clock.tick(60)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        if event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = py.mouse.get_pos()
            
            # Click is on The functions bar
            if mouse_y <= 120:

                if AI_controls[0].collidepoint(mouse_x, mouse_y): # Solve Maze
                    pass
                if AI_controls[1].collidepoint(mouse_x, mouse_y): # Show Steps
                    pass
                if AI_controls[2].collidepoint(mouse_x, mouse_y): # Previous Step
                    pass
                if AI_controls[3].collidepoint(mouse_x, mouse_y): # Next Step
                    pass

                if settings[0].collidepoint(mouse_x, mouse_y): # Middle Click ==> Start
                    middle_click = 'start'
                if settings[1].collidepoint(mouse_x, mouse_y): # Middle Click ==> goal
                    middle_click = 'goal'
                if settings[2].collidepoint(mouse_x, mouse_y): # Board Size ==> Small
                    board_size = 'small'
                    cell_size = SMALL_CELL
                    maze.set_size_small()
                if settings[3].collidepoint(mouse_x, mouse_y): # Board Size ==> Large
                    board_size = 'large'
                    cell_size = LARGE_CELL
                    maze.set_size_large()
                if settings[4].collidepoint(mouse_x, mouse_y): # Default Board ==> 1
                    
                    if maze.board_type == 'small':
                        maze.use_default_maze(1)
                    if maze.board_type == 'large':
                        maze.use_default_maze(1)
                if settings[5].collidepoint(mouse_x, mouse_y): # Default Board ==> 2
                    if maze.board_type == 'small':
                        maze.use_default_maze(2)
                    if maze.board_type == 'large':
                        maze.use_default_maze(2)
                if settings[6].collidepoint(mouse_x, mouse_y): # Default Board ==> 3
                    if maze.board_type == 'small':
                        maze.use_default_maze(3)
                    if maze.board_type == 'large':
                        maze.use_default_maze(3)

                if manage_state[0].collidepoint(mouse_x, mouse_y): # Clear Maze
                    maze.reset_board()
                elif manage_state[1].collidepoint(mouse_x, mouse_y): # Load Maze
                    pass
                elif manage_state[2].collidepoint(mouse_x, mouse_y): # Save Maze
                    pass
                    maze.show_board()

            # Click is on the Grid
            if mouse_y > 120:
                col = mouse_x // cell_size
                row = (mouse_y - 120) // cell_size

                # Left Click
                if py.mouse.get_pressed()[0] == True:
                    if maze.board[row][col] == 0:
                        maze.board[row][col] = 1

                # Middle click 
                if py.mouse.get_pressed()[1] == True:
                    if middle_click == 'start':
                        maze.set_start((row, col))
                    if middle_click == 'goal':
                        maze.set_goal((row, col))

                # Right Click
                if py.mouse.get_pressed()[2] == True:
                    if maze.board[row][col] == 1:
                        maze.board[row][col] = 0

        if event.type == py.MOUSEMOTION:
            mouse_x, mouse_y = py.mouse.get_pos()

            # Click is on Grid
            if mouse_y > 120:
                col = mouse_x // cell_size
                row = (mouse_y - 120) // cell_size

                # Ensure the click is within the bounds of the board
                if 0 <= row < maze.height and 0 <= col < maze.width:

                    # Left click
                    if py.mouse.get_pressed()[0] == True:
                        if maze.board[row][col] == 0:
                            maze.board[row][col] = 1

                    # Right Click
                    if py.mouse.get_pressed()[2] == True: 
                        if maze.board[row][col] == 1:
                            maze.board[row][col] = 0


py.quit()