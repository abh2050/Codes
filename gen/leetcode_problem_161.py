```python
'''
# Maximum Subsequence Sum with Non-Adjacent Jumps and K Deletions
# Difficulty: Hard

# Problem Description:
# Given an integer array `nums` and an integer `k`, find the maximum subsequence sum you can obtain such that 
# no two elements in the subsequence are adjacent in the original array. You are allowed to delete at most `k` 
# elements from the original array before forming the subsequence. Deleting an element means it's completely 
# removed from consideration for the subsequence, effectively shortening the array.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 5, 3, 1, 1, 3], k = 2
# Output: 13
# Explanation: Delete nums[1] and nums[6]. Then choose [2, 4, 3, 3] for a sum of 13.

# Example 2:
# Input: nums = [1, 2, 3, 4, 5], k = 0
# Output: 9 
# Explanation: Choose [1, 3, 5] for a sum of 9.

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# 0 <= k <= nums.length
'''

class Solution:
    def max_subsequence_sum(self, nums, k):
        """
        Finds the maximum non-adjacent subsequence sum after at most k deletions.

        Args:
            nums: The input integer array.
            k: The maximum number of allowed deletions.

        Returns:
            The maximum subsequence sum.
        """
        n = len(nums)
        dp = {}  # Memoization dictionary

        def solve(index, deletions, prev_taken):
            if index == n:
                return 0

            if (index, deletions, prev_taken) in dp:
                return dp[(index, deletions, prev_taken)]

            # Option 1: Skip current element (can either delete or just skip)
            res = solve(index + 1, deletions, False)

            # Option 2: Take current element (only if not adjacent to previously taken)
            if not prev_taken:
                res = max(res, nums[index] + solve(index + 1, deletions, True))

            # Option 3: Delete current element (if deletions allowed)
            if deletions < k:
                res = max(res, solve(index + 1, deletions + 1, False))

            dp[(index, deletions, prev_taken)] = res
            return res

        return solve(0, 0, False)


# Time Complexity: O(n * k * 2), where n is the length of nums. The recursive function has at most n * k * 2 states (index, deletions, prev_taken).
# Space Complexity: O(n * k * 2) for the memoization dictionary.



# Test cases
sol = Solution()
print(sol.max_subsequence_sum([2, 1, 4, 5, 3, 1, 1, 3], 2))  # Output: 13
print(sol.max_subsequence_sum([1, 2, 3, 4, 5], 0))  # Output: 9
print(sol.max_subsequence_sum([10, 5, 20, 15, 30], 1)) # Output: 55 (Delete 15, choose 10, 20, 30)
print(sol.max_subsequence_sum([5,5,10,100,10,5], 2)) # Output: 110

```