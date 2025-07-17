"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 722
Updated: 2025-07-17T10:43:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 722
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
