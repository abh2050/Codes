```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Choose elements at indices 0, 2, and 4 (2 + 9 + 1 = 12) or 1 and 3 (7+3 = 10)
# In this circular array we can't select both index 0 and index 4 as they are now adjacent. So Max will be (7+9 = 16) or (2+9+1=12)

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums)
        
        # Consider two scenarios:
        # 1. Excluding the last element (same as standard house robber problem)
        # 2. Excluding the first element (same as standard house robber, but on a subarray)

        def house_robber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))




# Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the house_robber function.
# Space Complexity: O(n) for the dp array in the house_robber function. Can be optimized to O(1) by using variables instead of the dp array.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [2, 7, 9, 3, 1]
print(f"Test Case 1: {solution.rob(nums1)}")  # Expected Output: 12

# Test Case 2
nums2 = [1, 2, 3, 1]
print(f"Test Case 2: {solution.rob(nums2)}")  # Expected Output: 4

# Test Case 3 (Edge case: empty array)
nums3 = []
print(f"Test Case 3: {solution.rob(nums3)}")  # Expected Output: 0

# Test Case 4 (Edge case: single element)
nums4 = [5]
print(f"Test Case 4: {solution.rob(nums4)}")  # Expected Output: 5

# Test Case 5 (Example from problem description)
nums5 = [2,7,9,3,1]
print(f"Test Case 5: {solution.rob(nums5)}") # Expected Output 16


# Test Case 6
nums6 = [1,3,1,3,100]
print(f"Test Case 6: {solution.rob(nums6)}") # Expected Output 103
```