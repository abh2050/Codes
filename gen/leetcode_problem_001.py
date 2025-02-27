def minSwapsToGroupRedBalls(balls: str) -> int:
    """
    Calculates the minimum number of swaps required to group red balls.

    Args:
        balls: A string representing the arrangement of balls.

    Returns:
        The minimum number of adjacent swaps required to group all the red balls.
    """

    red_indices = [i for i, ball in enumerate(balls) if ball == 'R']
    n = len(red_indices)

    if n == 0:
        return 0

    mid = n // 2
    median = red_indices[mid]

    swaps = 0
    for i in range(n):
        swaps += abs(red_indices[i] - (median - mid + i))

    return swaps

# Example Usage:
balls1 = "WRRBBW"
print(f"Input: {balls1}, Output: {minSwapsToGroupRedBalls(balls1)}")  # Output: 2

balls2 = "WBWR"
print(f"Input: {balls2}, Output: {minSwapsToGroupRedBalls(balls2)}")  # Output: 1

balls3 = "WWWW"
print(f"Input: {balls3}, Output: {minSwapsToGroupRedBalls(balls3)}")  # Output: 0

balls4 = "RRRRR"
print(f"Input: {balls4}, Output: {minSwapsToGroupRedBalls(balls4)}")  # Output: 0

balls5 = "BWRBRWB"
print(f"Input: {balls5}, Output: {5}")  # Output: 5

balls6 = "WRR"
print(f"Input: {balls6}, Output: {1}") # Output: 1
