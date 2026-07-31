"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2023
Updated: 2026-07-31T22:29:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2023
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
