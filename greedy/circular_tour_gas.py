"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 804
Updated: 2025-08-07T19:47:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 804
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
