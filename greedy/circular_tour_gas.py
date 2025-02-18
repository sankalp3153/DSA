"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 206
Updated: 2025-02-18T23:24:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 206
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
