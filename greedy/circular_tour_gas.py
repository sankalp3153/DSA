"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1678
Updated: 2026-04-15T13:16:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1678
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
