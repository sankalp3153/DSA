"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 321
Updated: 2025-03-20T12:03:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 321
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
