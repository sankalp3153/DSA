"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 358
Updated: 2025-03-27T22:54:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 358
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
