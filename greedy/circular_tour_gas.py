"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1609
Updated: 2026-03-25T10:06:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1609
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
