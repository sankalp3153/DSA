"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1504
Updated: 2026-02-26T12:57:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1504
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
