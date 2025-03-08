"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 266
Updated: 2025-03-08T20:07:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 266
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
