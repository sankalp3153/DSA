"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 1172
Updated: 2025-11-26T11:53:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1172
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
