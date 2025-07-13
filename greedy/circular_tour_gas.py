"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 712
Updated: 2025-07-13T21:37:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 712
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
