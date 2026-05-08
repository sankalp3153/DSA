"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1747
Updated: 2026-05-08T18:32:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1747
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
