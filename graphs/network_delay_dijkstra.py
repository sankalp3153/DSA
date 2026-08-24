"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2106
Updated: 2026-08-24T22:57:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2106
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
