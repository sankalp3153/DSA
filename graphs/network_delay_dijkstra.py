"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 680
Updated: 2025-06-27T16:47:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 680
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
