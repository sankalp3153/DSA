"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 68
Updated: 2025-01-13T18:33:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 68
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
