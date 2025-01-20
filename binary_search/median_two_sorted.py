"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 78
Updated: 2025-01-20T16:47:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 78
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
