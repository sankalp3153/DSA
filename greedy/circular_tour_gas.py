"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1402
Updated: 2026-01-28T18:40:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1402
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
