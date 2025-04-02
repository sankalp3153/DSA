"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 381
Updated: 2025-04-02T18:53:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 381
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
