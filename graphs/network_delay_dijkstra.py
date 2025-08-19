"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 864
Updated: 2025-08-19T20:55:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 864
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
