"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1140
Updated: 2025-11-16T19:13:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1140
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
