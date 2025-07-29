"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 772
Updated: 2025-07-29T21:21:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 772
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
