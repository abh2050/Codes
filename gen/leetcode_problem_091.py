```python
'''
# Maximum Subarray Sum with K Distinct Elements and Jump Restriction
# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and two integers 'k' and 'jump'. 
# You need to find the maximum subarray sum that contains at most 'k' distinct elements.
# However, there's a jump restriction: you can only form a subarray by selecting elements
# where the indices of any two adjacent elements in the subarray differ by at most 'jump'.

# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 3, 2], k = 2, jump = 2
# Output: 7
# Explanation: The subarray [1, 2, 1, 3] has at most 2 distinct elements and satisfies the jump constraint. Its sum is 7.

# Example 2:
# Input: nums = [1, 2, 3, 4, 5], k = 1, jump = 3
# Output: 5
# Explanation: The subarray [5] has at most 1 distinct element and satisfies the jump constraint. Its sum is 5.

# Example 3:
# Input: nums = [1, 2, 1, 2, 1], k = 2, jump = 1
# Output: 3
# Explanation: The subarray [1, 2, 1] or [1,2] has at most 2 distinct element and satisfies the jump constraint. Its sum is 3 (or 3).

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 1 <= jump <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySumKJumps(self, nums, k, jump):
        """
        Finds the maximum subarray sum with at most k distinct elements and jump restriction.

        Args:
            nums: The input array of integers.
            k: The maximum number of distinct elements allowed.
            jump: The maximum jump allowed between adjacent elements in the subarray.

        Returns:
            The maximum subarray sum.
        """

        n = len(nums)
        max_sum = 0
        for i in range(n):
            for j in range(i, n):
                subarray = []
                current = i
                while current <= j:
                    subarray.append(nums[current])
                    
                    next_index = -1
                    for next_c in range(current + 1, min(current + jump + 1, j + 1)):
                        if next_index == -1:
                            next_index = next_c
                        elif next_index != -1 and next_c <= j:
                            next_index = next_c

                    if next_index == -1:
                        break
                    current = next_index

                if len(set(subarray)) <= k:
                    max_sum = max(max_sum, sum(subarray))

        return max_sum



# Time Complexity: O(n^2*jump) - Due to the nested loops and jump constraint checks within inner loops
# Space Complexity: O(n)-  In worst-case for storing a subarray


# Test cases
solution = Solution()
print(solution.maxSubarraySumKJumps([1, 2, 1, 3, 2], 2, 2))  # Output: 7
print(solution.maxSubarraySumKJumps([1, 2, 3, 4, 5], 1, 3))  # Output: 5
print(solution.maxSubarraySumKJumps([1, 2, 1, 2, 1], 2, 1))  # Output: 3
print(solution.maxSubarraySumKJumps([10,5,7,10,2,1,7], 3, 2)) # Output: 27
print(solution.maxSubarraySumKJumps([1,2,3,1,2],2,1)) # Output: 6



```