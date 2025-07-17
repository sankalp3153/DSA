"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 726
Updated: 2025-07-17T18:49:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 726
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
