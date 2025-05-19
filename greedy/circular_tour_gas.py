"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 528
Updated: 2025-05-19T13:31:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 528
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
