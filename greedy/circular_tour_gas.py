"""
Module: circular_tour_gas
Approach: deficit reset running tank
Revision: 298
Updated: 2025-03-14T13:59:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 298
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
