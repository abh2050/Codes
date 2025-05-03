```python
'''
# Maximum Submatrix Sum with Rotation
# Difficulty: Hard

# Problem Description:
# You are given an N x N matrix of integers. You can rotate the matrix by 90 degrees clockwise any number of times.
# Find the maximum possible sum of elements in a submatrix after performing any number of rotations.
# A submatrix is a contiguous block of elements within the matrix.

# Examples:
# Example 1:
# Input: matrix = [[1, 2], [3, 4]]
# Output: 10
# Explanation: Rotating the matrix 0 times yields the maximum sum submatrix with sum 1+2+3+4 = 10.

# Example 2:
# Input: matrix = [[-1, -2], [-3, -4]]
# Output: -1
# Explanation: The maximum sum submatrix is formed by the element -1 itself.

# Example 3:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 45


# Constraints:
# 1 <= N <= 200
# -1000 <= matrix[i][j] <= 1000
'''

class Solution:
    def maxSubmatrixSum(self, matrix: list[list[int]]) -> int:
        # Time Complexity: O(N^2 * min(N,4)) since there are 4 possible rotations.
        # Space Complexity: O(N^2). For a copy of the original Matrix.
        
        n = len(matrix)
        max_sum = -float('inf')

        for _ in range(4):  # Iterate through all 4 possible rotations
            
            # Kadane's algorithm for maximum subarray sum
            for left in range(n):
                current_sum = [0] * n
                for right in range(left, n):
                    for i in range(n):
                        current_sum[i] += matrix[i][right]
                    
                    max_so_far = 0
                    current_max = -float('inf')
                    for x in current_sum:
                        max_so_far += x
                        current_max = max(current_max, max_so_far)
                        max_so_far = max(0, max_so_far)
                        
                    max_sum = max(max_sum, current_max)


            # Rotate the matrix 90 degrees clockwise
            rotated_matrix = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated_matrix[j][n - 1 - i] = matrix[i][j]
            matrix = rotated_matrix

        return max_sum


# Test Cases
sol = Solution()
print(sol.maxSubmatrixSum([[1, 2], [3, 4]]))  # Output: 10
print(sol.maxSubmatrixSum([[-1, -2], [-3, -4]]))  # Output: -1
print(sol.maxSubmatrixSum([[1,2,3],[4,5,6],[7,8,9]])) # Output: 45
print(sol.maxSubmatrixSum([[1,-2,3],[4,-5,-6],[-7,8,-9]])) # Output: 8
print(sol.maxSubmatrixSum([[-10]])) # Output -10
```