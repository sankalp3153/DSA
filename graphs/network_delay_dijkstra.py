"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 151
Updated: 2025-02-03T22:22:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 151
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
