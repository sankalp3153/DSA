"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 791
Updated: 2025-08-03T23:19:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 791
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
