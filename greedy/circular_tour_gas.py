"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1448
Updated: 2026-02-07T22:14:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1448
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
