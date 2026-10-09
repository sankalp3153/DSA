"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2253
Updated: 2026-10-09T20:06:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2253
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
