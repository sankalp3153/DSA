"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 988
Updated: 2025-09-22T17:37:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 988
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
