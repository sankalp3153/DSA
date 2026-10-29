"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 2299
Updated: 2026-10-29T14:32:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2299
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
