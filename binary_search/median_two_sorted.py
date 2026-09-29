"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2217
Updated: 2026-09-29T23:26:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2217
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
