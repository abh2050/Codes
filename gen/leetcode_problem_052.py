```python
'''
# Maximum Subarray Sum with K Distinct Prime Factors

# Difficulty: Hard

# Problem Description:
# Given an array of positive integers 'nums' and an integer 'k', find the maximum sum of a subarray where each element in the subarray has exactly 'k' distinct prime factors. If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [10, 15, 7, 14, 21, 2, 5], k = 2
# Output: 40 
# Explanation: The subarray [10, 15, 7, 14] has the maximum sum (10 + 15 + 7 + 14 = 46). However, 7 does not have 2 distinct prime factors.
# The subarray [10,15, 14, 21] has a sum of 60, but 21 has 2 prime factors (3, 7).
# The subarray [10,15,14] has a sum of 40. Each element has 2 distinct prime factors.
# Therefore, the answer is 40

# Example 2:
# Input: nums = [2, 3, 5, 7, 11, 13], k = 1
# Output: 36
# Explanation: Each element in the input array has 1 distinct prime factor. So, the sum of all the elements is returned.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 5
'''

class Solution:
    def maxSubarraySumKPrime(self, nums, k):
        """
        Finds the maximum sum of a subarray where each element has exactly k distinct prime factors.

        Args:
            nums: A list of positive integers.
            k: The required number of distinct prime factors.

        Returns:
            The maximum subarray sum, or -1 if no such subarray exists.
        """

        def count_prime_factors(n):
            count = 0
            i = 2
            while i * i <= n:
                if n % i == 0:
                    count += 1
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                count += 1
            return count

        n = len(nums)
        max_sum = -1
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                valid_subarray = True
                if count_prime_factors(nums[j]) != k:
                    valid_subarray = False

                if valid_subarray:
                    current_sum += nums[j]
                    max_sum = max(max_sum, current_sum)
                else:
                    current_sum=0


        return max_sum
    


# Time Complexity: O(n^2 * sqrt(M)) where n is the length of nums and M is the maximum value in nums.
# We iterate through all possible subarrays (O(n^2)), and for each element, we potentially calculate its prime factors (O(sqrt(M))).
# Space Complexity: O(1) as we only use constant extra space.



# Test cases
sol = Solution()
print(sol.maxSubarraySumKPrime([10, 15, 7, 14, 21, 2, 5], 2))  # Output: 40
print(sol.maxSubarraySumKPrime([2, 3, 5, 7, 11, 13], 1))  # Output: 36
print(sol.maxSubarraySumKPrime([6,10, 15, 14], 2)) # Output: 45
print(sol.maxSubarraySumKPrime([30, 42, 70, 105, 210, 21], 3)) # Output: 498
print(sol.maxSubarraySumKPrime([14],1 )) # Output: -1



```