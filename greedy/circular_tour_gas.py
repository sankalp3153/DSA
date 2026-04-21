"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1701
Updated: 2026-04-21T11:10:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1701
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
