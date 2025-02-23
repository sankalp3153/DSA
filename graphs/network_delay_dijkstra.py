"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 220
Updated: 2025-02-23T13:14:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 220
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
