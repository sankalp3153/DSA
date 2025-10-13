"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1048
Updated: 2025-10-13T19:59:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1048
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
