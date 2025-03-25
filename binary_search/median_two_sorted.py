"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 354
Updated: 2025-03-25T19:46:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 354
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
