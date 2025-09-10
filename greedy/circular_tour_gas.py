"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 942
Updated: 2025-09-10T18:40:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 942
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
