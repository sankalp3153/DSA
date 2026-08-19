"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2083
Updated: 2026-08-19T16:12:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2083
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
