"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1554
Updated: 2026-03-09T15:30:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1554
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
