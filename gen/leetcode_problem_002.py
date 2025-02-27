import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        Finds the k closest points to the origin.

        Args:
            points: A list of points represented as [x, y] coordinates.
            k: The number of closest points to return.

        Returns:
            A list of the k closest points to the origin.
        """

        # Use a max heap to keep track of the k closest points seen so far.
        # The heap will store tuples of (-distance_squared, point).
        # We use negative distance_squared so the largest distance is at the top.
        heap = []

        for x, y in points:
            distance_squared = x*x + y*y

            # If the heap has fewer than k elements, add the current point.
            if len(heap) < k:
                heapq.heappush(heap, (-distance_squared, [x, y]))
            else:
                # If the current point is closer than the farthest point in the heap,
                # replace the farthest point with the current point.
                if distance_squared < -heap[0][0]:
                    heapq.heapreplace(heap, (-distance_squared, [x, y]))

        # Extract the points from the heap.  The distances are negative in the heap, so we don't need them anymore
        result = [point for _, point in heap]
        return result
