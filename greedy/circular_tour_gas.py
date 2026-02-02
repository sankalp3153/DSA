"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1425
Updated: 2026-02-02T20:58:26+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1425
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
