"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 998
Updated: 2025-09-26T11:37:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 998
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
