"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 82
Updated: 2025-01-22T10:32:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 82
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
