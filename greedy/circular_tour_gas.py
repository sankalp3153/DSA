"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 827
Updated: 2025-08-11T22:30:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 827
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
