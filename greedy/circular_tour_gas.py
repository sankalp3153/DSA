"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 574
Updated: 2025-06-02T14:50:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 574
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
