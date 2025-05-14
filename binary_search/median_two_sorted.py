"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 515
Updated: 2025-05-14T10:13:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 515
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
