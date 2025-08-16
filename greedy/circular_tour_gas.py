"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 850
Updated: 2025-08-16T12:14:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 850
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
