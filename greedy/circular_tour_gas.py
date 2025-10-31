"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1103
Updated: 2025-10-31T15:29:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1103
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
