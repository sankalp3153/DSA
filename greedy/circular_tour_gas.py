"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1241
Updated: 2025-12-12T21:05:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1241
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
