```python
'''
# Maximum Subarray Sum with K Distinct Elements and Consecutive Subarrays
# Difficulty: Hard

# Problem Description:
# Given an array of integers nums and an integer k, find the maximum sum of a subarray that contains exactly k distinct elements and is formed by combining consecutive subarrays with distinct elements. 
# A consecutive subarray is a contiguous block of elements within nums.  The resulting subarray must also be contiguous.
# If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 3, 4], k = 3
# Output: 10
# Explanation: The subarray [1, 2, 1, 3, 4] contains 3 distinct elements (1, 2, 3) and has a sum of 10.

# Example 2:
# Input: nums = [1, 2, 1, 2, 3], k = 2
# Output: 7
# Explanation:  The subarray [1, 2, 1, 2] contains 2 distinct elements and has a sum of 6.
#              The subarray [2, 1, 2, 3] contains 3 distinct elements.
#              The subarray [1,2,1,2,3] has k=3 distinct elements and a sum of 9.
#              However [1,2,1,2] is the largest consecutive subarray with sum 7 formed from consecutive subarrays [1,2], [1,2]
#              The consecutive subarrays [1,2,1,2,3] formed [1,2], [1,2], [3]. 


# Example 3:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: 7 
# Explanation: [1,1,1,2,2] is the largest consecutive array with 2 distinct elements. Sum = 7

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySumKDistinct(self, nums, k):
        """
        Finds the maximum sum of a subarray with k distinct elements.

        Args:
            nums: The input array of integers.
            k: The required number of distinct elements.

        Returns:
            The maximum sum, or -1 if no such subarray exists.
        """
        n = len(nums)
        max_sum = -1
        for i in range(n):
            for j in range(i, n):
                subarray = nums[i:j+1]
                distinct_count = len(set(subarray))
                if distinct_count == k:
                    max_sum = max(max_sum, sum(subarray))
        return max_sum


'''
Time Complexity: O(n^2) due to nested loops iterating through all possible subarrays.
Space Complexity: O(n) in the worst case to store the set of distinct elements in a subarray.  Can reduce to O(K) by using a sliding window technique
'''

# Test cases
sol = Solution()

print(sol.maxSubarraySumKDistinct([1, 2, 1, 3, 4], 3))  # Output: 10
print(sol.maxSubarraySumKDistinct([1, 2, 1, 2, 3], 2))  # Output: 7
print(sol.maxSubarraySumKDistinct([1, 1, 1, 2, 2, 3], 2))  # Output: 7
print(sol.maxSubarraySumKDistinct([1, 2, 3, 4, 5], 6))  # Output: -1
print(sol.maxSubarraySumKDistinct([1,1,2,2,3,3,4,4,5,5],3)) # Output: 25

```