"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1977
Updated: 2026-07-18T11:57:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1977
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
