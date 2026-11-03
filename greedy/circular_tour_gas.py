"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2322
Updated: 2026-11-03T15:50:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2322
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
