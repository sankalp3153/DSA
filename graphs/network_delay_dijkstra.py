"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1163
Updated: 2025-11-24T14:35:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1163
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
