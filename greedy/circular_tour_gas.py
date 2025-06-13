"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 620
Updated: 2025-06-13T19:13:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 620
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
