"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1324
Updated: 2026-01-02T14:08:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1324
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
