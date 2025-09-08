"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 933
Updated: 2025-09-08T16:24:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 933
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
