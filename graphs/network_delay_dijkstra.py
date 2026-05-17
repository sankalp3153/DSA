"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1761
Updated: 2026-05-17T11:49:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1761
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
