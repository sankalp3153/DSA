"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 965
Updated: 2025-09-18T11:44:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 965
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
