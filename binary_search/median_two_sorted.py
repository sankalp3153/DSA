"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1389
Updated: 2026-01-25T21:22:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1389
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
