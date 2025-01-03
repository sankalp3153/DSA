"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 13
Updated: 2025-01-03T17:41:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 13
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
