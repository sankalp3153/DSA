"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1945
Updated: 2026-07-08T21:10:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1945
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
