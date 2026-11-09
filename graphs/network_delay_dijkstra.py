"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2336
Updated: 2026-11-09T14:25:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2336
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
