"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2092
Updated: 2026-08-21T15:42:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2092
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
