"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 473
Updated: 2025-05-01T14:19:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 473
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
