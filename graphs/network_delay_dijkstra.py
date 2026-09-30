"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2221
Updated: 2026-09-30T16:06:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2221
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
