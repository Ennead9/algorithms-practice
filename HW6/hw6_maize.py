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

def print_maze(maze, player_pos, show_hint=False):
    x, y = player_pos
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
                char = maze[i][j]
                if char == '+' and not show_hint:
                    char = '.'  # Hide the '+' if hint is not requested
                print(char, end=' ')
            else:
                # Print a space if outside the maze bounds
                print(' ', end=' ')  
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

def play_maze_game(maze):
    player_pos = (1, 0)
    maze[1][0] = '@'
    show_hint = False

    while True:
        print_maze(maze, player_pos, show_hint)
        move = input("Enter your move (W/A/S/D) or 'H' for a hint: ").upper()

        if move == 'H':
            show_hint = True
        elif move in ['W', 'A', 'S', 'D']:
            show_hint = False  # Hide the hint when the player moves
            maze, player_pos = update_player_position(maze, player_pos, move)
        
        # Check for win condition
        if player_pos == (len(maze) - 2, len(maze[0]) - 1):
            print("Congratulations, you've reached the destination!")
            break


def main():
    rows, cols = 11, 21  # Maze dimensions
    print_game_instructions()  # Print game instrunctions
    input()   # Wait for user input to continue
    maze = generate_maze(rows, cols)
    play_maze_game(maze)


if __name__ == "__main__":
    main()