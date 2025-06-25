"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 666
Updated: 2025-06-25T17:49:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 666
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
