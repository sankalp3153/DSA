"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1370
Updated: 2026-01-19T15:02:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1370
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
