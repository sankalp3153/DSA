"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1908
Updated: 2026-06-25T20:07:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1908
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
