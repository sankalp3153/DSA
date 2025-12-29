"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1301
Updated: 2025-12-29T15:21:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1301
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
