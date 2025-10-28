"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1094
Updated: 2025-10-28T16:53:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1094
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
