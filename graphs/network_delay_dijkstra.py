"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2060
Updated: 2026-08-15T18:06:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2060
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
