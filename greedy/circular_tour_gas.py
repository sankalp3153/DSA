"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 459
Updated: 2025-04-24T17:14:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 459
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
