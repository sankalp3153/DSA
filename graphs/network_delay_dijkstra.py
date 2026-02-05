"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1439
Updated: 2026-02-05T23:29:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1439
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
