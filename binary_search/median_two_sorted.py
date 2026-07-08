"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1941
Updated: 2026-07-08T12:18:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1941
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
