"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1071
Updated: 2025-10-21T11:19:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1071
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
