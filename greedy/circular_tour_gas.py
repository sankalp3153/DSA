"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2115
Updated: 2026-08-27T14:43:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2115
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
