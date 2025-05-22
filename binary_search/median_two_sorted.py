"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 538
Updated: 2025-05-22T18:59:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 538
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
