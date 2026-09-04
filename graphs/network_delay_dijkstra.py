"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2152
Updated: 2026-09-04T16:21:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2152
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
