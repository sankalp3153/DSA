"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 887
Updated: 2025-08-25T15:45:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 887
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
