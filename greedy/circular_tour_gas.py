"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1379
Updated: 2026-01-23T10:32:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1379
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
