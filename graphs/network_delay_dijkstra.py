"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 427
Updated: 2025-04-16T22:16:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 427
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
