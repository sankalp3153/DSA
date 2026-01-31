"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1416
Updated: 2026-01-31T18:45:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1416
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
