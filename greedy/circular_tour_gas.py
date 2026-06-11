"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1862
Updated: 2026-06-11T18:44:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1862
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
