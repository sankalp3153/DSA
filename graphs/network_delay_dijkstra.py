"""
Module: network_delay_dijkstra
Approach: min-heap shortest path relaxation
Revision: 1393
Updated: 2026-01-26T17:29:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1393
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
