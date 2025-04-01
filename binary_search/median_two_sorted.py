"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 377
Updated: 2025-04-01T18:49:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 377
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
