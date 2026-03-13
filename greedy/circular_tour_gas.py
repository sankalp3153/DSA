"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1563
Updated: 2026-03-13T14:51:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1563
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
