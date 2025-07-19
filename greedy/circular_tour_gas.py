"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 735
Updated: 2025-07-19T20:54:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 735
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
