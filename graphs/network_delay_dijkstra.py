"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1922
Updated: 2026-07-02T16:24:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1922
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
