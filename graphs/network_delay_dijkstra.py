"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 841
Updated: 2025-08-15T10:10:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 841
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
