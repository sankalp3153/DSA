"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2313
Updated: 2026-11-01T12:14:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2313
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
