"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1655
Updated: 2026-04-10T13:58:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1655
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
