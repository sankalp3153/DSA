"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1540
Updated: 2026-03-04T20:24:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1540
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
