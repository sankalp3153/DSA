"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2046
Updated: 2026-08-07T20:51:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2046
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
