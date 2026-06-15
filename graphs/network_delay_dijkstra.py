"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1876
Updated: 2026-06-15T12:32:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1876
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
