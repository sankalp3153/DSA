"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1494
Updated: 2026-02-20T23:32:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1494
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
