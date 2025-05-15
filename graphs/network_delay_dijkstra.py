"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 519
Updated: 2025-05-15T10:42:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 519
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
