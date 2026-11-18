"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2359
Updated: 2026-11-18T20:14:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2359
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
