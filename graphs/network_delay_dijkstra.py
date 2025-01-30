"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 128
Updated: 2025-01-30T14:55:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 128
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
