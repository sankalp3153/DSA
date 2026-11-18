"""
Dijkstra's Single-Source Shortest Path using a binary min-heap.
Time: O((V + E) log V) | Space: O(V + E)
"""

import heapq
from typing import Dict, List, Tuple


def network_delay_time(times: List[Tuple[int, int, int]], n: int, source: int) -> int:
    graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(1, n + 1)}
    for u, v, weight in times:
        graph[u].append((v, weight))

    dist: Dict[int, int] = {}
    heap: List[Tuple[int, int]] = [(0, source)]

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = cost
        for nxt, weight in graph[node]:
            if nxt not in dist:
                heapq.heappush(heap, (cost + weight, nxt))

    return max(dist.values()) if len(dist) == n else -1
