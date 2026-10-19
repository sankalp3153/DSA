"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2276
Updated: 2026-10-19T15:55:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2276
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
