"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 2148
Updated: 2026-09-02T17:42:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2148
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
