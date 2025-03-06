def maxNonAdjacentSum(nums):
    """
    Calculates the maximum sum of non-adjacent elements in an array.

    Args:
        nums: A list of integers.

    Returns:
        The maximum sum of non-adjacent elements.
    """

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    # dp[i] stores the maximum sum achievable up to index i
    # either by including nums[i] or excluding it.
    include = nums[0]  # Max sum including the first element
    exclude = 0       # Max sum excluding the first element

    for i in range(1, len(nums)):
        # The current element can either be included or excluded.

        # If we include the current element, we cannot include the previous element.
        new_include = exclude + nums[i]

        # If we exclude the current element, we can either include or exclude the previous element.
        new_exclude = max(include, exclude)

        # Update include and exclude for the next iteration.
        include = new_include
        exclude = new_exclude

    # The maximum sum will be either include or exclude the last element.
    return max(include, exclude)

# Example Usage:
nums1 = [1, 2, 3, 1]
print(f"Input: {nums1}, Output: {maxNonAdjacentSum(nums1)}")  # Output: 4

nums2 = [2, 7, 9, 3, 1]
print(f"Input: {nums2}, Output: {maxNonAdjacentSum(nums2)}")  # Output: 12

nums3 = [2, 1, 4, 9]
print(f"Input: {nums3}, Output: {maxNonAdjacentSum(nums3)}")  # Output: 11

nums4 = []
print(f"Input: {nums4}, Output: {maxNonAdjacentSum(nums4)}")  # Output: 0

nums5 = [5]
print(f"Input: {nums5}, Output: {maxNonAdjacentSum(nums5)}")  # Output: 5
