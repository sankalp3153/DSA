"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 160
Updated: 2025-02-06T19:20:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 160
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
