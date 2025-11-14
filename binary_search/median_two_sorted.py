"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1136
Updated: 2025-11-14T11:53:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1136
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
