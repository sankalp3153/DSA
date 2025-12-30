"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1310
Updated: 2025-12-30T18:07:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1310
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
