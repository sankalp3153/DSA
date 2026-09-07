"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2161
Updated: 2026-09-07T15:21:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2161
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
