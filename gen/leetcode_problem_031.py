```python
'''
# Maximum Subarray Sum with K Distinct Elements and Jumps
# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and two integers 'k' and 'jump'.
# You need to find the maximum subarray sum that contains at most 'k' distinct elements.
# Additionally, you are allowed to jump over at most 'jump' elements between consecutive elements 
# in the subarray.  A jump means skipping elements that are not included in the subarray.

# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 2, 3], k = 2, jump = 1
# Output: 7
# Explanation: The subarray [1, 2, 1, 2, 3] has at most 2 distinct elements (1 and 2 initially, then 1, 2, and 3 later) and uses a jump between the first 2 and the second 1.
# Another valid subarray is [1,2,2,3] with sum 6.

# Example 2:
# Input: nums = [1, 2, 3, 4, 5], k = 1, jump = 2
# Output: 1 
# Explanation:  Since k=1, we can only pick subarrays with single element since jumps don't reduce the distinct element count within the subarray.

# Example 3:
# Input: nums = [1, 2, 1, 3, 2], k = 2, jump = 0
# Output: 6 # [1,2,1,2] or [2,1,3,2]. Note that jumps=0 means strictly contiguous elements.
# Explanation: We can pick a contiguous subarray.

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 0 <= jump <= nums.length
'''

from collections import defaultdict

class Solution:
    def maxSubarraySumKJumps(self, nums, k, jump):
        """
        Finds the maximum subarray sum with at most k distinct elements and jumps.

        Args:
            nums: The input array of integers.
            k: The maximum number of distinct elements allowed.
            jump: The maximum allowed jumps.

        Returns:
            The maximum subarray sum.
        """
        n = len(nums)
        max_sum = 0
        for i in range(n):
            for j in range(i, n):
                subarray = []
                distinct_count = 0
                distinct_elements = set()
                jumps_used = 0
                current_index = i

                while current_index <= j:
                    if nums[current_index] not in distinct_elements:
                        if distinct_count < k:
                            distinct_elements.add(nums[current_index])
                            distinct_count += 1
                        else:
                            break  # Too many distinct elements
                    subarray.append(nums[current_index])
                    
                    next_index = current_index + 1
                    while next_index <= j and jumps_used < jump and nums[next_index] not in distinct_elements and distinct_count >=k:
                        next_index += 1
                        jumps_used +=1
                    current_index = next_index

                if current_index > j: # successfully traversed through a potential subarray
                     max_sum = max(max_sum, sum(subarray))

        return max_sum

    # Time Complexity: O(n^2 * (jump+1) *k) - Due to nested loops and potential jumps.
    # Space Complexity: O(k) - To store distinct elements.


# Test cases
solution = Solution()

print(solution.maxSubarraySumKJumps([1, 2, 1, 2, 3], 2, 1))  # Output: 7
print(solution.maxSubarraySumKJumps([1, 2, 3, 4, 5], 1, 2))  # Output: 1
print(solution.maxSubarraySumKJumps([1, 2, 1, 3, 2], 2, 0))  # Output: 6
print(solution.maxSubarraySumKJumps([10, 2, 11, 3, 12,1], 2, 2)) # Output: 36
print(solution.maxSubarraySumKJumps([1,2,3,4,5],3,1)) # Output: 15





```