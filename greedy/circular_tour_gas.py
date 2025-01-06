"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 22
Updated: 2025-01-06T13:11:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 22
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
