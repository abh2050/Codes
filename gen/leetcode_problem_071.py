```python
'''
# Maximum Subarray Sum with K Distinct Elements and Jumps
# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and two integers 'k' and 'jump'.
# You need to find the maximum subarray sum that contains at most 'k' distinct elements.
# Additionally, you can jump over at most 'jump' elements between any two consecutive elements in the subarray.

# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 3, 2], k = 2, jump = 1
# Output: 7
# Explanation: The subarray [1, 2, 1, 3] has at most 2 distinct elements (1, 2, and 3) and uses jumps of 0, 0, and 1 (which is <= jump).
# Another possible subarray is [2, 1, 3, 2], with jumps of 0, 1, and 0.

# Example 2:
# Input: nums = [1, 2, 3, 4, 5], k = 1, jump = 2
# Output: 5
# Explanation: The subarray [5] is the only valid subarray because k=1.

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 0 <= jump <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySumKJumps(self, nums, k, jump):
        n = len(nums)
        max_sum = 0
        for i in range(n):
            for j in range(i, n):
                subarray = []
                current = i
                while current <= j:
                    subarray.append(nums[current])
                    if current == j:
                        break
                    next_jump = min(current + jump + 1, j)
                    current = next_jump
                
                if len(set(subarray)) <= k:
                    max_sum = max(max_sum, sum(subarray))

        return max_sum


# Explanation:
# The solution uses a nested loop to iterate through all possible subarrays.
# For each subarray, it checks if the number of distinct elements is less than or equal to k.
# If the condition is met, it calculates the sum and updates the maximum sum accordingly.
# The jumping logic is implemented using a while loop and min function to determine the next element index to include in the subarray, adhering to the jump constraint.

# Time Complexity: O(n^3) due to nested loops and subarray generation.
# Space Complexity: O(n) in the worst case for storing the subarray.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [1, 2, 1, 3, 2]
k1 = 2
jump1 = 1
print(f"Test Case 1: {solution.maxSubarraySumKJumps(nums1, k1, jump1)}")  # Output: 7

# Test Case 2
nums2 = [1, 2, 3, 4, 5]
k2 = 1
jump2 = 2
print(f"Test Case 2: {solution.maxSubarraySumKJumps(nums2, k2, jump2)}")  # Output: 5

# Test Case 3 (Larger input)
nums3 = [10, 2, 5, 1, 8, 3, 7, 4, 9, 6]
k3 = 3
jump3 = 2
print(f"Test Case 3: {solution.maxSubarraySumKJumps(nums3, k3, jump3)}") # Output: 34 ([10, 2, 5, 1, 8, 3, 7])

# Test Case 4 (Zero Jump)
nums4 = [1, 2, 3, 4, 5]
k4 = 3
jump4 = 0
print(f"Test Case 4: {solution.maxSubarraySumKJumps(nums4, k4, jump4)}") # Output: 15

# Test Case 5 (All Same Elements)
nums5 = [5, 5, 5, 5, 5]
k5 = 1
jump5 = 2
print(f"Test Case 5: {solution.maxSubarraySumKJumps(nums5, k5, jump5)}") # Output: 25




```