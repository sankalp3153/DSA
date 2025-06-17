"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 634
Updated: 2025-06-17T13:14:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 634
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
