"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 689
Updated: 2025-07-01T15:21:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 689
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
