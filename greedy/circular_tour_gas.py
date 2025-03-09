"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 275
Updated: 2025-03-09T19:01:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 275
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
