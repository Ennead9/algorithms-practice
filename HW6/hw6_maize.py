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

def print_maze(maze, player_pos, path_cache, show_hint=False):
    x, y = player_pos
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
                if show_hint and path_cache[i][j]:
                    print('+', end=' ')
                else:
                    print(maze[i][j] if maze[i][j] != '+' else '.', end=' ')
            else:
                print(' ', end=' ')  # Print a space if outside the maze bounds
        print()

# Print entire maze for debugging help issue
def print_full_maze(maze, path_cache, show_hint=False):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if show_hint and path_cache[i][j]:
                print('+', end=' ')
            else:
                print(maze[i][j], end=' ')
        print()


# Game overview and instructions
def print_game_instructions():
    print("Welcome to the Maze Game!")
    print("Your goal is to navigate from the start (top-left corner) to the destination (bottom-right corner).")
    print("Instructions:")
    print("  - Use 'W' to move up (north).")
    print("  - Use 'S' to move down (south).")
    print("  - Use 'A' to move left (west).")
    print("  - Use 'D' to move right (east).")
    print("  - Press 'H' for a hint.")
    print("\nPress any key to start the game...")


def update_player_position(maze, player_pos, move):
    x, y = player_pos
    maze[x][y] = '.'  # Clear the old position
    if move == 'W': x -= 1
    elif move == 'S': x += 1
    elif move == 'A': y -= 1
    elif move == 'D': y += 1

    # Ensure the new position is valid
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
        player_pos = (x, y)
    
    maze[x][y] = '@'  # Place the player in the new position
    return maze, player_pos


# DFS function with memoization
def dfs_find_path(maze, x, y, destination, path_cache, visited):
    if (x, y) == destination:
        path_cache[x][y] = True
        return True
    if not (0 <= x < len(maze) and 0 <= y < len(maze[0])) or maze[x][y] == '#' or (x, y) in visited:
        return False

    visited.add((x, y))

    if path_cache[x][y] is not None:
        return path_cache[x][y]

    # Explore all possible directions
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if dfs_find_path(maze, nx, ny, destination, path_cache, visited):
            path_cache[x][y] = True
            return True

    visited.remove((x, y))
    return False



def initialize_cache(rows, cols):
    # Initialize the cache with None values
    return [[None for _ in range(cols)] for _ in range(rows)]

def copy_maze(maze):
    # Create a deep copy of the maze
    return [row[:] for row in maze]


def play_maze_game(maze, cache):
    player_pos = (1, 0)
    maze[1][0] = '@'
    destination = (len(maze) - 2, len(maze[0]) - 1)
    path_cache = copy_maze(cache)  # Use a local copy of the cache

    while True:
        # print_maze(maze, player_pos, path_cache, show_hint=False)
        print_full_maze(maze, cache, show_hint=False)  # For debugging, print the full maze
        move = input("Enter your move (W/A/S/D) or 'H' for a hint: ").upper()

        if move == 'H':
            hint_maze = copy_maze(maze)
            visited = set()  # Initialize the visited set
            if dfs_find_path(hint_maze, player_pos[0], player_pos[1], destination, path_cache, visited):
                print_maze(hint_maze, player_pos, path_cache, show_hint=True)
            else:
                print("No path found.")  # For debugging, remove this later
        elif move in ['W', 'A', 'S', 'D']:
            maze, player_pos = update_player_position(maze, player_pos, move)
        
        # Check for win condition
        if player_pos == destination:
            print("Congratulations, you've reached the destination!")
            break


def main():
    rows, cols = 11, 21  # Maze dimensions
    cache = initialize_cache(rows, cols)  # Global cache for memoization

    print_game_instructions()  # Print game instrunctions
    input()   # Wait for user input to continue
    maze = generate_maze(rows, cols)
    play_maze_game(maze, cache)


if __name__ == "__main__":
    main()