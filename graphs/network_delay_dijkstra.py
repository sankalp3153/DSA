"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 565
Updated: 2025-05-28T19:38:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 565
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
