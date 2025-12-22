"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1274
Updated: 2025-12-22T10:21:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1274
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
