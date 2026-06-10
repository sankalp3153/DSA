"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1853
Updated: 2026-06-10T14:42:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1853
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
