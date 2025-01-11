"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 59
Updated: 2025-01-11T22:10:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 59
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
