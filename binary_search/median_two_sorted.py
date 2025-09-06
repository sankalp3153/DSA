"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 929
Updated: 2025-09-06T15:43:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 929
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
