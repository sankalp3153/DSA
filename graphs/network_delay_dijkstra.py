"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 312
Updated: 2025-03-19T10:22:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 312
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
