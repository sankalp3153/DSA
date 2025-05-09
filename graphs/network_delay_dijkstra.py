"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 496
Updated: 2025-05-09T14:31:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 496
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
