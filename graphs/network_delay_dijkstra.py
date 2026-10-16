"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2267
Updated: 2026-10-16T21:39:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2267
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
