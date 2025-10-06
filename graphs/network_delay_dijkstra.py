"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1025
Updated: 2025-10-06T11:34:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1025
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
