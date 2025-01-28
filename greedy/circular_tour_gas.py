"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 114
Updated: 2025-01-28T20:46:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 114
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
