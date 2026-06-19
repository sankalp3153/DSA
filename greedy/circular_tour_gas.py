"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1885
Updated: 2026-06-19T19:21:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1885
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
