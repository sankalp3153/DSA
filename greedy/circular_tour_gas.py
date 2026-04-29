"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1724
Updated: 2026-04-29T16:09:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1724
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
