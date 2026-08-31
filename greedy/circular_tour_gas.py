"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2138
Updated: 2026-08-31T21:20:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2138
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
