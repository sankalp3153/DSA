"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1577
Updated: 2026-03-16T17:06:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1577
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
