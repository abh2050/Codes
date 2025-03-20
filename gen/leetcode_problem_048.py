```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element),
# find the maximum sum of a non-adjacent subset of elements.  A subset is non-adjacent if no two elements in the subset are adjacent to each other in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: Choose elements at index 0 (2) and index 2 (4) and index 3 (9). The sum is 2 + 4 + 9 = 11.  Note that 0 and 3 are technically adjacent in a circular array, but the problem specifies *adjacent pairs* must be excluded. So [2,9] is fine but [9,1] is not, and neither is [2,1].


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at index 0 (1) and index 2 (3). The sum is 1 + 3 = 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: The array contains only one element, so the maximum sum is 1.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Calculate the maximum sum considering both including and excluding the first element.
        def rob_linear(arr):
            n = len(arr)
            if n == 0: return 0
            if n == 1: return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[n - 1]


        # Consider two cases:
        # 1. Exclude the last element (equivalent to a standard non-circular array problem).
        # 2. Exclude the first element.
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



# Test cases
solution = Solution()

print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 3, 1, 3, 100]))  # Output: 103
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12


'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in rob_linear.
Space Complexity: O(N) for the dp array in rob_linear. Can be optimized to O(1) by storing only the previous two values.

'''

```