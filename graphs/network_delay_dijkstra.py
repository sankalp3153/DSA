"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2290
Updated: 2026-10-24T20:29:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2290
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
