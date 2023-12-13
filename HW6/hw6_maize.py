import random

def initialize_maze(rows, cols):
    # Initialize the maze with walls
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    # Set start and destination
    maze[1][0] = '.'
    maze[rows - 2][cols - 1] = '.'
    return maze

def add_path_to_maze(maze, rows, cols):
    # Directions (north, east, south, west)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def is_valid_move(x, y):
        # Check if the move is within the maze bounds and not a wall
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == '#'

    def carve_path(x, y):
        # Randomize the directions
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + dx*2, y + dy*2

            if is_valid_move(new_x, new_y):
                # Carve out the path
                maze[x + dx][y + dy] = '.'
                maze[new_x][new_y] = '.'
                carve_path(new_x, new_y)

    # Start carving the path from the start position
    carve_path(1, 0)

def generate_maze(rows, cols):
    maze = initialize_maze(rows, cols)
    add_path_to_maze(maze, rows, cols)
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Example usage
rows, cols = 11, 21  # Maze dimensions
maze = generate_maze(rows, cols)
print_maze(maze)
