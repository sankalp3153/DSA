"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1931
Updated: 2026-07-05T14:38:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1931
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
