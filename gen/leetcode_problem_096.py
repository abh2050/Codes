```python
'''
# Maximum Subarray Sum with K Distinct Elements and Length Limit
# Difficulty: Hard

# Problem Description:
# Given an array of integers `nums` and two integers `k` and `limit`, find the maximum subarray sum 
# that contains at most `k` distinct elements and has a length less than or equal to `limit`.
# If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 3, 2], k = 2, limit = 3
# Output: 6
# Explanation: The subarray [1, 2, 1] has a sum of 4 and 2 distinct elements (1 and 2).
# The subarray [1, 3, 2] has a sum of 6 and 2 distinct elements (1, 3 and 2).
# The subarray [1, 2, 1, 3] has a sum of 7 but contains 3 distinct elements.
# Therefore, the maximum sum of a valid subarray is 6.


# Example 2:
# Input: nums = [1, 2, 3, 4, 5], k = 1, limit = 2
# Output: 3
# Explanation: The subarray [1, 2] contains 2 distinct elements.
# The subarray [1] has a sum of 1 and 1 distinct element.
# The subarray [2] has a sum of 2 and 1 distinct element.
# Therefore, the maximum sum of a valid subarray is 3. (Subarrays [2,3], [3,4], [4,5] are also valid)

# Example 3:
# Input: nums = [1, 2, 3, 4, 5], k = 1, limit = 0
# Output: -1
# Explanation: No subarrays can be formed.


# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 0 <= limit <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySum(self, nums, k, limit):
        """
        Finds the maximum subarray sum with at most k distinct elements and length <= limit.

        Args:
            nums: The input array of integers.
            k: The maximum number of distinct elements allowed.
            limit: The maximum length of the subarray.

        Returns:
            The maximum subarray sum, or -1 if no such subarray exists.
        """
        n = len(nums)
        if limit == 0:
            return -1

        max_sum = -1
        left = 0
        count = defaultdict(int)  # Stores frequency of each element in the current window
        current_sum = 0
        distinct_count = 0

        for right in range(n):
            # Add element to the window
            if count[nums[right]] == 0:
                distinct_count += 1
            count[nums[right]] += 1
            current_sum += nums[right]
            
            # Shrink the window until it becomes valid
            while left <= right and (distinct_count > k or (right - left + 1) > limit):
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    distinct_count -= 1
                current_sum -= nums[left]
                left += 1

            # Update max_sum
            if distinct_count <= k and (right - left + 1) <= limit:
                max_sum = max(max_sum, current_sum)

        return max_sum


# Time Complexity: O(N), where N is the length of nums. We iterate through nums twice in the worst case (left and right pointers).
# Space Complexity: O(K), where K is the maximum number of distinct elements. We store at most k elements in the count dictionary.



# Test Cases
solution = Solution()

print(solution.maxSubarraySum([1, 2, 1, 3, 2], 2, 3))  # Output: 6
print(solution.maxSubarraySum([1, 2, 3, 4, 5], 1, 2))  # Output: 3
print(solution.maxSubarraySum([1, 2, 3, 4, 5], 1, 0))  # Output: -1
print(solution.maxSubarraySum([1, 2, 1, 3, 2, 4, 5, 1], 3, 4)) # Output: 12
print(solution.maxSubarraySum([10,5,20,15,25], 2, 3)) # Output: 45


```