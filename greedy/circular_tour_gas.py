"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2000
Updated: 2026-07-25T16:35:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2000
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
