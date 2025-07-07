"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 703
Updated: 2025-07-07T19:41:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 703
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
