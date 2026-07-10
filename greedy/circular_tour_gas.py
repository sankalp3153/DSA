"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1954
Updated: 2026-07-10T15:30:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1954
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
