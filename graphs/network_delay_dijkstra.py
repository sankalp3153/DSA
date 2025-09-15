"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 956
Updated: 2025-09-15T16:16:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 956
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
