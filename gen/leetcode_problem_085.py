```python
'''
# Maximum Subarray Sum with K Distinct Rotations

# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and an integer 'k'.  Find the maximum possible sum of a subarray after performing at most 'k' rotations.

# A rotation involves moving the last element of the array to the beginning.  For example, rotating [1,2,3] once results in [3,1,2]. Rotating it twice results in [2,3,1].

# A subarray is a contiguous non-empty sequence of elements within an array.

# Examples:
# Example 1:
# Input: nums = [1,5,-2,3,2], k = 2
# Output: 8
# Explanation: Rotate once to get [2,1,5,-2,3]. The subarray [1,5,-2,3] has the maximum sum of 7.
# Rotate twice to get [3,2,1,5,-2]. The subarray [3,2,1,5] has the maximum sum of 11. Return the maximum, which is 11.


# Example 2:
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: Rotate once to get [-3,-1,-2]. Maximum subarray sum is -1.  Original max subarray sum is also -1.


# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 0 <= k <= nums.length
'''

class Solution:
    def maxSubarraySumAfterRotations(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum subarray sum after at most k rotations.

        Args:
            nums: The input array of integers.
            k: The maximum number of rotations allowed.

        Returns:
            The maximum subarray sum.
        """
        n = len(nums)
        max_sum = -float('inf')

        for rotations in range(min(k + 1, n)):  # Iterate through possible rotations
            rotated_nums = nums[-rotations:] + nums[:-rotations] # Rotate the array

            current_max = -float('inf')
            current_sum = 0
            for num in rotated_nums:
                current_sum = max(num, current_sum + num) # Kadane's algorithm for max subarray sum
                current_max = max(current_max, current_sum)
            
            max_sum = max(max_sum, current_max) # Update overall maximum sum

        return max_sum
        


# Time Complexity: O(n * min(k,n)), where n is the length of nums. We iterate through at most k rotations (or n if k is larger), and in each rotation, we iterate through the entire array using Kadane's algorithm.
# Space Complexity: O(n) in the worst case when k >= n, because of the rotated array. If k << n, the space complexity can be considered O(k), or even O(1) if we rotate in-place, although this might make the code more complex.


# Test Cases
solution = Solution()

print(solution.maxSubarraySumAfterRotations([1, 5, -2, 3, 2], 2))  # Output: 11
print(solution.maxSubarraySumAfterRotations([-1, -2, -3], 1))  # Output: -1
print(solution.maxSubarraySumAfterRotations([10, -5, 15, -20, 25], 3))  # Output: 25
print(solution.maxSubarraySumAfterRotations([1, 2, 3, 4, 5], 0))  # Output: 15
print(solution.maxSubarraySumAfterRotations([5], 2)) # Output: 5
print(solution.maxSubarraySumAfterRotations([-1, -5, -2, -3, -2], 2))  # Output: -1
```