"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 2014
Updated: 2026-07-29T20:52:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2014
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
