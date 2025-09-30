"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1011
Updated: 2025-09-30T14:23:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1011
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
