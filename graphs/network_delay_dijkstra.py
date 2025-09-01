"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 910
Updated: 2025-09-01T14:49:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 910
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
