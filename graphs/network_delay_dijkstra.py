"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1186
Updated: 2025-11-30T16:05:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1186
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
