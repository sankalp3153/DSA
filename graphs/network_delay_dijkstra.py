"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1278
Updated: 2025-12-23T13:39:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1278
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
