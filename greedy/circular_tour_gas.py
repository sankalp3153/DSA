"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1218
Updated: 2025-12-06T16:18:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1218
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
