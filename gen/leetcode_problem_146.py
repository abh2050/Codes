```python
'''
# Maximum Submatrix Sum with Rotation
# Difficulty: Hard

# Problem Description:
# You are given an N x N matrix of integers. You can rotate the matrix by 90 degrees clockwise any number of times.
# Find the maximum possible sum of a submatrix after performing any number of rotations.
# A submatrix is defined as a contiguous block of cells within the matrix.

# Examples:
# Example 1:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: 45
# Explanation: The original matrix already has the maximum submatrix sum (1+2+3+4+5+6+7+8+9 = 45).

# Example 2:
# Input: matrix = [[-1, -2], [-3, -4]]
# Output: -1
# Explanation: The maximum submatrix sum is -1.

# Example 3:
# Input: matrix = [[1, 2], [3, 4]]
# Output: 10
# Explanation: Rotating the matrix once gives [[3, 1], [4, 2]], with maximum submatrix sum 10.

# Constraints:
# 1 <= N <= 500
# -1000 <= matrix[i][j] <= 1000
'''

class Solution:
    def maxSubmatrixSum(self, matrix: list[list[int]]) -> int:
        # Time Complexity: O(N^3) -  We rotate and calculate Kadane's algorithm O(N^2) times.
        # Space Complexity: O(N^2) - Space for the rotated matrix.
        n = len(matrix)
        max_sum = -float('inf')

        for _ in range(4):  # Try all 4 rotations
            # Kadane's algorithm for maximum subarray sum in 2D
            for left in range(n):
                current_sum = [0] * n
                for right in range(left, n):
                    for i in range(n):
                        current_sum[i] += matrix[i][right]
                    
                    # 1D Kadane's Algorithm
                    max_so_far = 0
                    current_max = -float('inf')
                    for x in current_sum:
                        max_so_far += x
                        current_max = max(current_max, max_so_far)
                        max_so_far = max(0, max_so_far) # Reset if sum becomes negative
                    max_sum = max(max_sum, current_max)
            
            # Rotate the matrix 90 degrees clockwise
            rotated_matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated_matrix[j][n - 1 - i] = matrix[i][j]
            matrix = rotated_matrix

        return max_sum


# Test Cases
solution = Solution()

# Example 1
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Example 1 Output: {solution.maxSubmatrixSum(matrix1)}")  # Expected Output: 45

# Example 2
matrix2 = [[-1, -2], [-3, -4]]
print(f"Example 2 Output: {solution.maxSubmatrixSum(matrix2)}")  # Expected Output: -1

# Example 3
matrix3 = [[1, 2], [3, 4]]
print(f"Example 3 Output: {solution.maxSubmatrixSum(matrix3)}")  # Expected Output: 10

# Additional Test Case with rotations making a difference
matrix4 = [[1, -2], [3, 4]]
print(f"Example 4 Output: {solution.maxSubmatrixSum(matrix4)}") # Expected Output: 7


```