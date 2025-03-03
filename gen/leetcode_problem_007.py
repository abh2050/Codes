def islandPerimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid: A list of lists representing the grid where 1 is land and 0 is water.

    Returns:
        The perimeter of the island.
    """

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Count the number of sides that are touching water or the edge of the grid

                # Check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

# Example Usage:
grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(f"Perimeter of grid1: {islandPerimeter(grid1)}") # Output: 16

grid2 = [[1]]
print(f"Perimeter of grid2: {islandPerimeter(grid2)}") # Output: 4

grid3 = [[1,0]]
print(f"Perimeter of grid3: {islandPerimeter(grid3)}") # Output: 4
