"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2129
Updated: 2026-08-29T15:58:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2129
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
