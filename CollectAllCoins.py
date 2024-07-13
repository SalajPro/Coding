import random

# Constants
GRID_SIZE = 10
NUM_ITEMS = 5
NUM_OBSTACLES = 10

# Directions
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

# Initialize the grid
def initialize_grid(size):
    return [['.' for _ in range(size)] for _ in range(size)]

# Place the player on the grid
def place_player(grid):
    player_pos = (0, 0)
    grid[player_pos[0]][player_pos[1]] = 'P'
    return player_pos

# Place items on the grid
def place_items(grid, num_items):
    items = []
    for _ in range(num_items):
        while True:
            item_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            if grid[item_pos[0]][item_pos[1]] == '.':
                grid[item_pos[0]][item_pos[1]] = 'I'
                items.append(item_pos)
                break
    return items

# Place obstacles on the grid
def place_obstacles(grid, num_obstacles):
    for _ in range(num_obstacles):
        while True:
            obstacle_pos = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
            if grid[obstacle_pos[0]][obstacle_pos[1]] == '.':
                grid[obstacle_pos[0]][obstacle_pos[1]] = 'O'
                break

# Display the grid
def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

# Move the player
def move_player(grid, player_pos, direction):
    x, y = player_pos
    grid[x][y] = '.'
    if direction == UP and x > 0:
        x -= 1
    elif direction == DOWN and x < GRID_SIZE - 1:
        x += 1
    elif direction == LEFT and y > 0:
        y -= 1
    elif direction == RIGHT and y < GRID_SIZE - 1:
        y += 1
    new_pos = (x, y)
    if grid[x][y] == 'I':
        print("You found an item!")
    elif grid[x][y] == 'O':
        print("You hit an obstacle! Game over.")
        return player_pos, True
    grid[x][y] = 'P'
    return new_pos, False

# Check if all items are collected
def check_victory(grid, num_items):
    count = sum(row.count('I') for row in grid)
    return count == 0

# Main game loop
def main():
    grid = initialize_grid(GRID_SIZE)
    player_pos = place_player(grid)
    items = place_items(grid, NUM_ITEMS)
    place_obstacles(grid, NUM_OBSTACLES)
    game_over = False

    while not game_over:
        display_grid(grid)
        move = input("Move (w/a/s/d): ")
        if move in [UP, DOWN, LEFT, RIGHT]:
            player_pos, game_over = move_player(grid, player_pos, move)
        if check_victory(grid, NUM_ITEMS):
            print("Congratulations! You collected all items!")
            break

    print("Game Over")

if __name__ == "__main__":
    main()
