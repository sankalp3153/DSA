"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 239
Updated: 2025-03-02T16:08:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 239
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
