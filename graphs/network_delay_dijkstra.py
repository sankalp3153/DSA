"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 450
Updated: 2025-04-21T15:59:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 450
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
