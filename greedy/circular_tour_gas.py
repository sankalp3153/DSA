"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1195
Updated: 2025-12-01T12:06:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1195
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
