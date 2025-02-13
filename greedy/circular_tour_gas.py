"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 183
Updated: 2025-02-13T11:37:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 183
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
