import heapq

def minCostConnectPoints(points):
    """
    Finds the minimum cost to connect all points using Prim's algorithm.

    Args:
        points: A list of lists representing the coordinates of points.

    Returns:
        The minimum cost to connect all points.
    """

    n = len(points)
    adj = {i: [] for i in range(n)}

    # Build the adjacency list (graph)
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            adj[i].append((dist, j))
            adj[j].append((dist, i))

    # Prim's Algorithm
    mst_cost = 0
    visited = set()
    pq = [(0, 0)]  # (cost, node) - Start with node 0, cost 0

    while pq:
        cost, u = heapq.heappop(pq)

        if u in visited:
            continue

        mst_cost += cost
        visited.add(u)

        for neighbor_cost, v in adj[u]:
            if v not in visited:
                heapq.heappush(pq, (neighbor_cost, v))

    return mst_cost
