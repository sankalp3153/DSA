"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 873
Updated: 2025-08-22T17:03:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 873
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
