"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 45
Updated: 2025-01-09T13:30:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 45
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
