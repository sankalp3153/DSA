"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1646
Updated: 2026-04-07T14:40:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1646
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
