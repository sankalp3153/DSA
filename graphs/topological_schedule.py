"""
Kahn's BFS Topological Sort & DAG Cycle Detection.
Time: O(V + E) | Space: O(V + E)
"""

from collections import deque
from typing import Deque, List, Tuple


def topological_order(num_nodes: int, prerequisites: List[Tuple[int, int]]) -> List[int]:
    adj: List[List[int]] = [[] for _ in range(num_nodes)]
    indegree = [0] * num_nodes

    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1

    queue: Deque[int] = deque(i for i in range(num_nodes) if indegree[i] == 0)
    order: List[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return order if len(order) == num_nodes else []
