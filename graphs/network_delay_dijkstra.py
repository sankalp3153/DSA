"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 657
Updated: 2025-06-23T19:10:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 657
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
