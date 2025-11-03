"""
Module: median_two_sorted
Approach: logarithmic partition cut
Revision: 1113
Updated: 2025-11-03T17:31:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1113
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
