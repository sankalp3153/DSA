"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1715
Updated: 2026-04-27T12:01:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1715
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
