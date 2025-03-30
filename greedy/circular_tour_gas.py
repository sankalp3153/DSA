"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 367
Updated: 2025-03-30T21:31:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 367
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
