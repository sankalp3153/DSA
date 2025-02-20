"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 216
Updated: 2025-02-20T22:06:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 216
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
