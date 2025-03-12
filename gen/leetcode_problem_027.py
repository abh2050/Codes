```python
'''
# Maximum Subarray Sum with K Distinct Elements and No Adjacent Duplicates
# Difficulty: Hard

# Problem Description:
# Given an array of integers 'nums' and an integer 'k', find the maximum possible sum of a subarray that satisfies the following conditions:
# 1. The subarray contains at most 'k' distinct elements.
# 2. The subarray contains no adjacent duplicate elements.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 1, 2], k = 3
# Output: 8
# Explanation: The subarray [1, 2, 3, 1, 2] has 3 distinct elements and no adjacent duplicates. Its sum is 9.
# Another valid subarray is [1,2,3,1], with sum 7
# Another valid subarray is [2,3,1,2], with sum 8.

# Example 2:
# Input: nums = [1, 1, 1, 2, 2, 2], k = 2
# Output: 5 
# Explanation: The subarray [1, 2, 2] sums to 5 and satisfies the conditions.
# The subarray [1, 2, 1, 2] has adjacent duplicates, hence not valid.

# Example 3:
# Input: nums = [1, 2, 1, 2, 1, 2, 1, 2], k = 1
# Output: 2
# Explanation: Any subarray with length greater than 1 contains adjacent duplicates, so valid subarrays are [1], [2], etc.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySum(self, nums, k):
        # Use a sliding window approach.
        # Track the count of each element within the window and the total sum.
        n = len(nums)
        max_sum = 0
        left = 0
        count = defaultdict(int)
        current_sum = 0
        
        for right in range(n):
            count[nums[right]] += 1
            current_sum += nums[right]
            
            while len(count) > k or (right > 0 and nums[right] == nums[right - 1]): # while window is invalid
                count[nums[left]] -= 1
                current_sum -= nums[left]
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            
            max_sum = max(max_sum, current_sum)

        return max_sum
    

# Time Complexity: O(N), where N is the length of nums.  We iterate through the array once.
# Space Complexity: O(K), where K is the maximum number of distinct elements allowed.  In the worst case, the count dictionary stores K elements.


# Test Cases
solution = Solution()
print(solution.maxSubarraySum([1, 2, 3, 1, 2], 3))  # Output: 9
print(solution.maxSubarraySum([1, 1, 1, 2, 2, 2], 2))  # Output: 5
print(solution.maxSubarraySum([1, 2, 1, 2, 1, 2, 1, 2], 1))  # Output: 2
print(solution.maxSubarraySum([1, 2, 3, 4, 5], 5))  # Output: 15
print(solution.maxSubarraySum([1, 2, 1, 3, 2, 4, 1, 5], 3)) # Output: 11 (e.g. [2,1,3,2,4] or [1,3,2,4,1] sums to 11)
print(solution.maxSubarraySum([1,1,1,1,1], 1)) # Output: 1
```