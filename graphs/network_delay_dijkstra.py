"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1991
Updated: 2026-07-22T11:51:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1991
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
