"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 818
Updated: 2025-08-10T22:57:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 818
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
