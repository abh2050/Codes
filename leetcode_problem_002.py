from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Calculates the minimum cost to connect all points.

        Args:
            points: A list of points where each point is a list [x, y].

        Returns:
            The minimum cost to connect all points.
        """
        # Implementation goes here
        pass


# Example 1:
points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
#
# We can connect the points as follows:
# - Connect [0, 0] to [2, 2] with cost 2 + 2 = 4.
# - Connect [2, 2] to [5, 2] with cost 3 + 0 = 3.
# - Connect [5, 2] to [7, 0] with cost 2 + 2 = 4.
# - Connect [2, 2] to [3, 10] with cost 1 + 8 = 9.
# The total cost of this way is 4 + 3 + 4 + 9 = 20.

# Example 2:
points2 = [[3,12],[-2,5],[-4,1]]
# Output: 18

# Example 3:
points3 = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4


from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Calculates the minimum cost to connect all points.

        Args:
            points: A list of points where each point is a list [x, y].

        Returns:
            The minimum cost to connect all points.
        """
        n = len(points)
        if n <= 1:
            return 0

        # Adjacency List: {node: [(cost, neighbor), ...]}
        adj_list = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[i].append((cost, j))
                adj_list[j].append((cost, i))

        # Prim's Algorithm
        visited = set()
        min_cost = 0
        priority_queue = [(0, 0)]  # (cost, node)

        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if node in visited:
                continue

            visited.add(node)
            min_cost += cost

            for neighbor_cost, neighbor in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (neighbor_cost, neighbor))

        return min_cost
