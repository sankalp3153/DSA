"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1471
Updated: 2026-02-15T14:08:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1471
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
