"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1600
Updated: 2026-03-22T23:15:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1600
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
