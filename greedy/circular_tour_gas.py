"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1816
Updated: 2026-06-03T12:19:22+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1816
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
