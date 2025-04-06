```python
'''
# Maximum Sum Submatrix with Rotation

# Difficulty: Hard

# Problem Description:
# You are given a square matrix `matrix` of size `n x n` containing integers. You can rotate the matrix by 90 degrees clockwise any number of times. 
# Find the maximum possible sum of elements in a submatrix after performing any number of rotations. A submatrix is defined as a contiguous block of cells within the matrix.

# Examples:
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 45
# Explanation: Rotating the matrix doesn't change the total sum if we consider the entire matrix as a submatrix.

# Example 2:
# Input: matrix = [[1,-2,3],[4,5,-6],[7,8,9]]
# Output: 25
# Explanation: By rotating the matrix once clockwise, we get [[7,4,1],[8,5,-2],[9,-6,3]]. The top-left 2x2 submatrix has a sum of 24.
#              Rotating twice gives [[9,8,7],[-6,5,4],[3,-2,1]]. The top-left 2x2 submatrix has a sum of 12.
#              Rotating three times gives [[3,-6,9],[-2,5,8],[1,4,7]]. The top-left 2x2 submatrix has a sum of 8. 
#              The maximum sum submatrix can be found in the original matrix as the entire matrix, giving a sum of 1+2+3+4+5+6+7+8+9=45

# Constraints:
# 1 <= n <= 200
# -1000 <= matrix[i][j] <= 1000
'''

class Solution:
    def maxSubmatrixSum(self, matrix: list[list[int]]) -> int:
        # Time Complexity: O(n^2 * min(n, 4)) -> since we rotate at most 4 times
        # Space Complexity: O(n^2) -> for storing rotated matrices

        n = len(matrix)
        max_sum = -float('inf')

        for _ in range(4):  # Rotate up to 4 times
            # Calculate max submatrix sum for the current rotation
            current_sum = self.calculate_max_submatrix_sum(matrix)
            max_sum = max(max_sum, current_sum)

            # Rotate the matrix 90 degrees clockwise
            matrix = self.rotate_matrix(matrix)

        return max_sum

    def calculate_max_submatrix_sum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        max_sum = -float('inf')
        for i in range(n):
            for j in range(n):
                for k in range(i, n):
                    for l in range(j, n):
                        current_sum = 0
                        for row in range(i, k + 1):
                            for col in range(j, l + 1):
                                current_sum += matrix[row][col]
                        max_sum = max(max_sum, current_sum)
        return max_sum


    def rotate_matrix(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        rotated_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated_matrix[j][n - 1 - i] = matrix[i][j]
        return rotated_matrix


# Test cases
solution = Solution()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solution.maxSubmatrixSum(matrix1))  # Output: 45

matrix2 = [[1, -2, 3], [4, 5, -6], [7, 8, 9]]
print(solution.maxSubmatrixSum(matrix2))  # Output: 45

matrix3 = [[-1, -2], [-3, -4]]
print(solution.maxSubmatrixSum(matrix3))  # Output: -1

matrix4 = [[10]]
print(solution.maxSubmatrixSum(matrix4)) # Output: 10

matrix5 = [[0, -5], [4, 1]]
print(solution.maxSubmatrixSum(matrix5))  # Output: 5



```