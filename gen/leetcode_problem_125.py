```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the first element is also considered adjacent to the last element), 
# find the maximum sum of a non-adjacent subset of elements. A subset is non-adjacent if no two elements in the 
# subset are adjacent to each other in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick numbers 2, 9, and 1. Their sum is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick numbers 1, 3. Their sum is 4.


# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        # We consider two cases:
        # 1. Include the first element, exclude the last element
        # 2. Exclude the first element, include the last element
        # Then take the maximum of the two cases.

        def house_robber(arr):
            # Standard house robber logic (without circularity).
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]

        # Case 1: Exclude the last element
        case1 = house_robber(nums[:-1])

        # Case 2: Exclude the first element
        case2 = house_robber(nums[1:])

        return max(case1, case2)


# Test cases
solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 3
print(solution.rob([1])) # Output: 1
print(solution.rob([])) # Output: 0
print(solution.rob([1,100,2])) # Output 100


"""
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice 
                 in the `house_robber` function.

Space Complexity: O(N) in the worst case due to the dp array in house_robber function.  Could be
                  optimized to O(1) by storing only the previous two dp values.
"""
```