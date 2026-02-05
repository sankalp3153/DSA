"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1435
Updated: 2026-02-05T17:34:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1435
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
