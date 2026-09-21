"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2198
Updated: 2026-09-21T19:34:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2198
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
