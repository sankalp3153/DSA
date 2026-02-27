"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1517
Updated: 2026-02-27T21:28:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1517
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
