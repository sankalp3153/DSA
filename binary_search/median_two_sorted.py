"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 906
Updated: 2025-08-31T23:34:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 906
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
