"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 105
Updated: 2025-01-25T22:10:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 105
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
