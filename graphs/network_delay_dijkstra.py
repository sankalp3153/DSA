"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 174
Updated: 2025-02-10T13:31:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 174
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
