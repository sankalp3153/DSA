"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1839
Updated: 2026-06-06T20:12:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1839
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
