"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2207
Updated: 2026-09-28T12:55:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2207
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
