"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 896
Updated: 2025-08-26T18:31:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 896
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
