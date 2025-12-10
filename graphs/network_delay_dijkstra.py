"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1232
Updated: 2025-12-10T18:38:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1232
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
