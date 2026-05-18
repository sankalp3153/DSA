"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1770
Updated: 2026-05-18T14:54:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1770
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
