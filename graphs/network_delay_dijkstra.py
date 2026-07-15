"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1968
Updated: 2026-07-15T11:43:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1968
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
