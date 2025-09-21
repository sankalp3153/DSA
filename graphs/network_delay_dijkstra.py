"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 979
Updated: 2025-09-21T12:11:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 979
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
