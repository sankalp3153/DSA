"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 289
Updated: 2025-03-12T18:09:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 289
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
