"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 193
Updated: 2025-02-16T10:04:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 193
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
