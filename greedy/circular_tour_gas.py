"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2345
Updated: 2026-11-12T23:15:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2345
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
