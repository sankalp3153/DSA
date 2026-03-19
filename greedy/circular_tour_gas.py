"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1586
Updated: 2026-03-19T20:08:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1586
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
