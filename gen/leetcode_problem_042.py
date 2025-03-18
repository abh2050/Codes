```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is "non-adjacent" if no two elements
# in the subset are directly adjacent to each other in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick the elements at indices 0, 2, and 4 (2 + 9 + 1 = 12). Alternatively you can select 7 and 3 for a sum of 10 or 7 and 1 for a sum of 8.
# However the maximum sum is 11 (7+3+1)

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
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

        # Consider two scenarios:
        # 1. Excluding the last element: Standard house robber problem on nums[:-1]
        # 2. Excluding the first element: Standard house robber problem on nums[1:]

        def house_robber(arr):
            # Standard house robber using dynamic programming
            n = len(arr)
            dp = [0] * (n + 1)  
            dp[1] = arr[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i-1])  # rob or not rob the current house
            return dp[n]


        return max(house_robber(nums[:-1]), house_robber(nums[1:]))

    # Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
    # Space Complexity: O(n) -  For the dp array in house_robber. Can be optimized to O(1).



# Test Cases
solution = Solution()

# Test case 1
nums1 = [2, 7, 9, 3, 1]
print(f"Input: {nums1}, Output: {solution.rob_circular(nums1)} (Expected: 12)")  # 7+3+1 = 11, 2+9+1=12

# Test case 2
nums2 = [1, 2, 3, 1]
print(f"Input: {nums2}, Output: {solution.rob_circular(nums2)} (Expected: 4)")

# Test case 3 - Empty array
nums3 = []
print(f"Input: {nums3}, Output: {solution.rob_circular(nums3)} (Expected: 0)")

# Test case 4 - Single element array
nums4 = [5]
print(f"Input: {nums4}, Output: {solution.rob_circular(nums4)} (Expected: 5)")

# Test Case 5
nums5 = [1,3,1,3,100]
print(f"Input: {nums5}, Output: {solution.rob_circular(nums5)} (Expected: 103)")


```