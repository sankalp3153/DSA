"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 243
Updated: 2025-03-02T20:39:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 243
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
