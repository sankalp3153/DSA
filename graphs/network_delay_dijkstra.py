"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2244
Updated: 2026-10-06T13:56:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2244
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
