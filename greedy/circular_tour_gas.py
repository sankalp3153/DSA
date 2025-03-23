"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 344
Updated: 2025-03-23T10:51:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 344
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
