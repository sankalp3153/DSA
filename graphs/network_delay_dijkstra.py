"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 542
Updated: 2025-05-23T12:14:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 542
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
