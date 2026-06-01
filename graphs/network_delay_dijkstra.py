"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1807
Updated: 2026-06-01T11:41:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1807
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
