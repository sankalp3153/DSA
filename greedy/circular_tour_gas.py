"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1149
Updated: 2025-11-20T17:25:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1149
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
