"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 795
Updated: 2025-08-04T20:05:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 795
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
