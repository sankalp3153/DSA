"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 413
Updated: 2025-04-11T18:29:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 413
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
