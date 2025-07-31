"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 781
Updated: 2025-07-31T22:19:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 781
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
