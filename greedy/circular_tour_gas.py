"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 137
Updated: 2025-02-01T14:56:03+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 137
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
