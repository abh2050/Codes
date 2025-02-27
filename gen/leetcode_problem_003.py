from collections import deque

def updateMatrix(matrix):
    """
    Finds the distance of the nearest 0 for each cell in the matrix.

    Args:
        matrix: A 2D list of integers representing the matrix.

    Returns:
        A 2D list of integers representing the distance to the nearest 0 for each cell.
    """

    m, n = len(matrix), len(matrix[0])
    dist = [[float('inf')] * n for _ in range(m)]  # Initialize distances to infinity
    queue = deque()

    # Add all 0s to the queue and set their distance to 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))

    # BFS to find the shortest distance to the nearest 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < m and 0 <= new_col < n and dist[new_row][new_col] > dist[row][col] + 1:
                dist[new_row][new_col] = dist[row][col] + 1
                queue.append((new_row, new_col))

    return dist

# Example usage:
matrix1 = [[0,0,0],[0,1,0],[0,0,0]]
print(updateMatrix(matrix1))  # Output: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

matrix2 = [[0,0,0],[0,1,0],[1,1,1]]
print(updateMatrix(matrix2))  # Output: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
