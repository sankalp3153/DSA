"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 551
Updated: 2025-05-24T15:24:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 551
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
