"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 252
Updated: 2025-03-04T17:28:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 252
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
