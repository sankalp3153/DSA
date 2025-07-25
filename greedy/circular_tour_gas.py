"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 758
Updated: 2025-07-25T12:21:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 758
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
