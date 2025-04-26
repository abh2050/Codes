```python
'''
# Maximum Subarray Sum with K Distinct Elements and Length Constraint
# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and two integers 'k' and 'length'. 
# Find the maximum sum of a subarray that contains exactly 'k' distinct elements and has a length of at least 'length'.
# If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 2, 1, 4], k = 3, length = 3
# Output: 9
# Explanation: The subarray [2, 3, 2, 1] has 3 distinct elements (1, 2, 3) and a length of 4. Its sum is 8.
#              The subarray [3, 2, 1, 4] has 3 distinct elements (1, 2, 3, 4) and a length of 4. Its sum is 10.
#              The subarray [2, 1, 4] has 3 distinct elements (1, 2, 4) and a length of 3. Its sum is 7.
#              The maximum sum is 10.


# Example 2:
# Input: nums = [1, 1, 2, 2, 3], k = 2, length = 2
# Output: 7
# Explanation: The subarray [1, 1, 2, 2] has 2 distinct elements and a length of 4. Its sum is 6.
#              The subarray [1, 2, 2, 3] has 3 distinct elements and a length of 4. Its sum is 8. The subarray [2, 2, 3] has length 3 and sum 7, 2 distinct elements.
#              The subarray [1, 2, 2] has 2 distinct elements and a length of 3. Its sum is 5.


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 1 <= length <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySum(self, nums: list[int], k: int, length: int) -> int:
        n = len(nums)
        max_sum = -1
        for i in range(n):
            for j in range(i + length -1, n):
                subarray = nums[i:j+1]
                distinct_count = len(set(subarray))
                if distinct_count == k:
                    current_sum = sum(subarray)
                    max_sum = max(max_sum, current_sum)

        return max_sum



# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 2, 1, 4]
k1 = 3
length1 = 3
print(f"Example 1: {solution.maxSubarraySum(nums1, k1, length1)}")  # Output: 10

# Example 2
nums2 = [1, 1, 2, 2, 3]
k2 = 2
length2 = 2
print(f"Example 2: {solution.maxSubarraySum(nums2, k2, length2)}")  # Output: 7


# Example 3: Testing with no valid subarray.
nums3 = [1,2,3,4,5]
k3 = 6
length3 = 2
print(f"Example 3: {solution.maxSubarraySum(nums3, k3, length3)}") # Output: -1

# Example 4
nums4 = [1, 2, 1, 2, 1, 2]
k4 = 2
length4 = 2
print(f"Example 4: {solution.maxSubarraySum(nums4,k4,length4)}") # Output: 6



```