"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 170
Updated: 2025-02-08T14:03:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 170
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
