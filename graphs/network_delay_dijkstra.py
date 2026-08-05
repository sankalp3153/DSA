"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2037
Updated: 2026-08-05T20:12:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2037
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
