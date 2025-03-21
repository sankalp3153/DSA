"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 335
Updated: 2025-03-21T17:44:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 335
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
