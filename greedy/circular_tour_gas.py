"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 597
Updated: 2025-06-07T22:23:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 597
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
