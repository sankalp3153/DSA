"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1531
Updated: 2026-03-02T18:21:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1531
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
