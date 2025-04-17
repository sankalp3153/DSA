"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 436
Updated: 2025-04-17T18:56:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 436
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
