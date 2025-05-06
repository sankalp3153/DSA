"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 482
Updated: 2025-05-06T19:32:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 482
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
