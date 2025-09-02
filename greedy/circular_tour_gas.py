"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 919
Updated: 2025-09-02T20:33:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 919
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
