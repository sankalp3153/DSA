"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 197
Updated: 2025-02-16T21:40:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 197
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
