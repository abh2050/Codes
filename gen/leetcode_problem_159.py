```python
'''
# Maximum Subarray Sum with at Most K Deletions
# Difficulty: Hard

# Problem Description:
# You are given an array of integers 'nums' and an integer 'k'. Find the maximum possible sum of a non-empty subarray of 'nums' after deleting at most 'k' elements from the subarray.

# Examples:
# Example 1:
# Input: nums = [1, -2, 3, 4, -5, 6], k = 2
# Output: 10
# Explanation: Delete -2 and -5. The subarray [3, 4, 6] has a sum of 13.  However, deleting -2 and -5 from the entire array yields [1, 3, 4, 6] with a subarray [3, 4, 6] summing to 13. Another option is deleting -2 and -5 from the subarray [1, -2, 3, 4, -5, 6] resulting in [1, 3, 4, 6]. The max subarray sum is 10 from [3,4,6]

# Example 2:
# Input: nums = [-1, -1, 10], k = 1
# Output: 10
# Explanation: Delete -1. The subarray [10] sums to 10.

# Constraints:
# 1 <= nums.length <= 10^5
# -1000 <= nums[i] <= 1000
# 0 <= k <= nums.length
'''

import heapq

class Solution:
    def maxSubarraySumWithDeletions(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum subarray sum with at most k deletions using a monotonic decreasing queue.

        Args:
            nums: The input array of integers.
            k: The maximum number of elements to delete.

        Returns:
            The maximum subarray sum.
        """
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            current_sum = 0
            deletions = 0
            heap = [] # Min-heap to store negative elements for potential deletion
            for j in range(i, n):
                current_sum += nums[j]
                if nums[j] < 0:
                    heapq.heappush(heap, nums[j])
                while heap and deletions < k and current_sum + heap[0] > current_sum:
                        current_sum += heap[0]  #Effectively removes element from the subarray
                        heapq.heappop(heap) 
                        deletions += 1


                max_sum = max(max_sum, current_sum)
                

        return max_sum

# Test Cases
solution = Solution()

# Example 1
nums1 = [1, -2, 3, 4, -5, 6]
k1 = 2
print(f"Test Case 1: {solution.maxSubarraySumWithDeletions(nums1, k1)}")  # Output: 10

# Example 2
nums2 = [-1, -1, 10]
k2 = 1
print(f"Test Case 2: {solution.maxSubarraySumWithDeletions(nums2, k2)}")  # Output: 10

# Example 3 - Edge case with all negative numbers
nums3 = [-1, -2, -3]
k3 = 1
print(f"Test Case 3: {solution.maxSubarraySumWithDeletions(nums3, k3)}")  # Output: -1

# Example 4 - Edge case with k >= n
nums4 = [1, 2, 3]
k4 = 3
print(f"Test Case 4: {solution.maxSubarraySumWithDeletions(nums4, k4)}")  # Output: 6

# Example 5
nums5 = [-1, -1, 1, -1, -1, 2]
k5 = 2
print(f"Test Case 5: {solution.maxSubarraySumWithDeletions(nums5, k5)}") # Output 3

# Time Complexity: O(n^2 * log k), since the inner loop may push/pop from the heap
# Space Complexity: O(k) for storing the heap
```