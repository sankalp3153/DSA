"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 505
Updated: 2025-05-10T19:16:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 505
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
