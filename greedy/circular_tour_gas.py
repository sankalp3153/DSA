"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2069
Updated: 2026-08-17T21:49:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2069
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
