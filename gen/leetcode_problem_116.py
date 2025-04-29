```python
'''
# Maximum Sum Submatrix with Constraints
# Difficulty: Hard

# Problem Description:
# Given a 2D integer matrix 'matrix' and two integers 'k' and 'limit', find the maximum sum of a submatrix where the dimensions of the submatrix are exactly k x k.  
# However, there's an additional constraint: the maximum element within the chosen submatrix must not exceed 'limit'. 
# If no such submatrix exists (e.g., the matrix is too small or all submatrices violate the limit constraint), return -1.

# Examples:
# Example 1:
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], k = 2, limit = 6
# Output: 16 
# Explanation: The 2x2 submatrix [[1, 2], [4, 5]] has a sum of 12 and max element 5 (<= limit). The submatrix [[2, 3], [5, 6]] has a sum of 16 and max element 6 (<= limit).
# The submatrix [[4, 5], [7, 8]] violates the limit because it contains 8.
# 16 is the maximum valid sum.


# Example 2:
# Input: matrix = [[7, 8], [9, 10]], k = 2, limit = 7
# Output: -1
# Explanation: The only 2x2 submatrix has a maximum element greater than the limit.

# Example 3:
# Input: matrix = [[1, 2, 3], [4, 5, 6]], k = 2, limit = 10
# Output: -1
# Explanation: The matrix dimensions are not sufficient to form a 2x2 submatrix.


# Constraints:
# 1 <= matrix.length <= 100
# 1 <= matrix[i].length <= 100
# 1 <= k <= min(matrix.length, matrix[i].length)
# -100 <= matrix[i][j] <= 100
# -100 <= limit <= 100
'''

class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int, limit: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        if rows < k or cols < k:
            return -1

        max_sum = -1

        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                current_sum = 0
                max_element = -101  # Initialize below the minimum possible value

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        current_sum += matrix[x][y]
                        max_element = max(max_element, matrix[x][y])

                if max_element <= limit:
                    max_sum = max(max_sum, current_sum)

        return max_sum


# Test cases
solution = Solution()

# Example 1
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k1 = 2
limit1 = 6
print(f"Example 1 Output: {solution.maxSumSubmatrix(matrix1, k1, limit1)} (Expected: 16)")

# Example 2
matrix2 = [[7, 8], [9, 10]]
k2 = 2
limit2 = 7
print(f"Example 2 Output: {solution.maxSumSubmatrix(matrix2, k2, limit2)} (Expected: -1)")


# Example 3
matrix3 = [[1, 2, 3], [4, 5, 6]]
k3 = 2
limit3 = 10
print(f"Example 3 Output: {solution.maxSumSubmatrix(matrix3, k3, limit3)} (Expected: -1)")

# Example 4 (larger matrix)
matrix4 = [[1, -2, 3], [4, 5, -1], [-3, 2, 6], [1, 8, -5]]
k4 = 2
limit4 = 5
print(f"Example 4 Output: {solution.maxSumSubmatrix(matrix4, k4, limit4)} (Expected: 12)")


# Time Complexity: O(m * n * k^2), where m and n are the dimensions of the matrix.
# Space Complexity: O(1) - We use constant extra space.

```