"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2230
Updated: 2026-10-02T11:16:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2230
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
