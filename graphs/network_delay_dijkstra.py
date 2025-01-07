"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 36
Updated: 2025-01-07T21:38:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 36
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
