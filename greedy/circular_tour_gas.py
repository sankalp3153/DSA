"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2184
Updated: 2026-09-18T21:27:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2184
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
