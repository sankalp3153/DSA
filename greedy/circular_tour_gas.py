"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 643
Updated: 2025-06-18T21:58:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 643
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
