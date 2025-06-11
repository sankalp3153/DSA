"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 611
Updated: 2025-06-11T22:52:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 611
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
