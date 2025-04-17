```python
'''
# Maximum Sum Submatrix with Rotation
# Difficulty: Hard

# Problem Description:
# You are given a square matrix `matrix` of integers with dimensions n x n. You can rotate the matrix by 90 degrees clockwise any number of times.
# Find the maximum possible sum of a submatrix within the matrix after performing any number of rotations. A submatrix is defined as a contiguous block of cells within the matrix.

# Examples:
# Example 1:
# Input: matrix = [[1, 2], [3, 4]]
# Output: 10
# Explanation: Rotating the matrix 0 times yields a maximum submatrix sum of 10 (the entire matrix).

# Example 2:
# Input: matrix = [[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]]
# Output: 15
# Explanation: Rotating the matrix by 90 degrees clockwise once yields a matrix [[0, 9, -4, -1], [-2, 2, 1, 8], [-7, -6, -4, 0], [0, 2, 1, -2]]. The maximum submatrix sum is 15 (the submatrix formed by rows 0 and 1, and columns 1, 2, and 3).


# Constraints:
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
'''

class Solution:
    def maxSubmatrixSumAfterRotation(self, matrix: list[list[int]]) -> int:
        # Time Complexity: O(n^2) - We iterate through the matrix multiple times for rotations and Kadane's algorithm.
        # Space Complexity: O(n) - We use extra space to store rotated matrices and temporary arrays for Kadane's algorithm.
        def rotate(mat):
            n = len(mat)
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = mat[i][j]
            return rotated
        
        def kadane(arr):
            max_so_far = float('-inf')
            current_max = 0
            for x in arr:
                current_max += x
                if current_max > max_so_far:
                    max_so_far = current_max
                if current_max < 0:
                    current_max = 0
            return max_so_far
        
        n = len(matrix)
        max_sum = float('-inf')
        
        for _ in range(4): # Try all 4 rotations
            for i in range(n):
                temp = [0] * n
                for j in range(i, n):
                    for k in range(n):
                        temp[k] += matrix[j][k]
                    max_sum = max(max_sum, kadane(temp))
            matrix = rotate(matrix) # Rotate 90 degrees clockwise
        
        return max_sum

# Test Cases
solution = Solution()

matrix1 = [[1, 2], [3, 4]]
print(f"Input: {matrix1}, Output: {solution.maxSubmatrixSumAfterRotation(matrix1)} (Expected: 10)")

matrix2 = [[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]]
print(f"Input: {matrix2}, Output: {solution.maxSubmatrixSumAfterRotation(matrix2)} (Expected: 15)")

matrix3 = [[-1,-2],[-3,-4]]
print(f"Input: {matrix3}, Output: {solution.maxSubmatrixSumAfterRotation(matrix3)} (Expected: -1)")

matrix4 = [[1]]
print(f"Input: {matrix4}, Output: {solution.maxSubmatrixSumAfterRotation(matrix4)} (Expected: 1)")



```