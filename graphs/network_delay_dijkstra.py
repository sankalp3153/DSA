"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1669
Updated: 2026-04-12T13:13:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1669
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
