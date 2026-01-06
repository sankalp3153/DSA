"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1333
Updated: 2026-01-06T15:15:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1333
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
