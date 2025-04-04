"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 390
Updated: 2025-04-04T16:13:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 390
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
