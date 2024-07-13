import turtle
import random

# Constants
GRID_SIZE = 31  # Must be an odd number for proper maze generation
CELL_SIZE = 20
WALL = '#'
PASSAGE = ' '
START = 'S'
END = 'E'

# Directions: up, down, left, right
DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Initialize the grid
def initialize_grid(size):
    return [[WALL for _ in range(size)] for _ in range(size)]

# Check if a cell is within the grid and is a wall
def is_valid(x, y, size, grid):
    return 0 <= x < size and 0 <= y < size and grid[x][y] == WALL

# Create a maze using DFS
def create_maze(grid, size):
    stack = [(1, 1)]
    grid[1][1] = PASSAGE

    while stack:
        cx, cy = stack[-1]
        neighbors = []

        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, size, grid):
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            grid[cx + (nx - cx) // 2][cy + (ny - cy) // 2] = PASSAGE
            grid[nx][ny] = PASSAGE
            stack.append((nx, ny))
        else:
            stack.pop()

# Add start and end points to the maze
def add_start_end(grid, size):
    grid[1][1] = START
    grid[size - 2][size - 2] = END

# Draw the maze using Turtle
def draw_maze(grid, size, cell_size):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.tracer(0, 0)
    start_x = -size // 2 * cell_size
    start_y = size // 2 * cell_size
    for i in range(size):
        for j in range(size):
            x = start_x + j * cell_size
            y = start_y - i * cell_size
            if grid[i][j] == WALL:
                turtle.goto(x, y)
                turtle.pendown()
                turtle.begin_fill()
                for _ in range(4):
                    turtle.forward(cell_size)
                    turtle.right(90)
                turtle.end_fill()
                turtle.penup()
            elif grid[i][j] == START:
                turtle.goto(x + cell_size // 4, y - cell_size // 2)
                turtle.write("S", align="center", font=("Arial", 12, "bold"))
            elif grid[i][j] == END:
                turtle.goto(x + cell_size // 4, y - cell_size // 2)
                turtle.write("E", align="center", font=("Arial", 12, "bold"))
    turtle.update()

# Main function to generate and display the maze
def main():
    size = GRID_SIZE
    grid = initialize_grid(size)
    create_maze(grid, size)
    add_start_end(grid, size)
    draw_maze(grid, size, CELL_SIZE)
    turtle.done()

if __name__ == "__main__":
    main()
